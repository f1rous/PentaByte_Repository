#!/usr/bin/env python3
"""Sort incoming files into the CS AI Study module repository structure.

Examples:
  python module_sorter.py "CS AI Study module" "Downloads"             # preview
  python module_sorter.py "CS AI Study module" "Downloads" --apply     # move
  python module_sorter.py "CS AI Study module" "Downloads" --apply --copy
"""
import argparse
import re
import shutil
from pathlib import Path

IMAGE = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}
DOCUMENT = {'.md', '.txt', '.pdf', '.doc', '.docx', '.ppt', '.pptx'}


def choose_destination(file: Path, root: Path, members: list[str]) -> Path:
    name = file.stem.lower()
    suffix = file.suffix.lower()
    chapter = re.search(r'(?:chapter|ch)[ _-]*(\d+)', name, re.I)
    person = next((m for m in members if m.lower() in name), None)
    if suffix in IMAGE:
        if chapter:
            return root / 'Assets' / 'Chapter Assets' / f'Chapter_{chapter.group(1)}'
        if person:
            return root / 'Assets' / 'Personal Assets' / person
        return root / 'To Review' / 'Images'
    if suffix in DOCUMENT:
        if any(x in name for x in ('personal log', 'personal_log', 'personal-log')):
            return root / 'Logs' / 'Personal Logs'
        if any(x in name for x in ('team log', 'project log')):
            return root / 'Logs' / 'Team Log'
        if re.search(r'phase[ _-]*1|log[ _-]*[12]$', name):
            return root / 'Logs' / 'Phase1'
        if any(x in name for x in ('research', 'paper', 'bibliography')):
            return root / 'Docs' / 'Research'
        if any(x in name for x in ('outline', 'project plan', 'projectplan')):
            return root / 'Docs'
        if any(x in name for x in ('submission', 'final report', 'final_report')):
            return root / 'Submissions'
        if chapter:
            section = 'Introductory Chapter' if int(chapter.group(1)) <= 2 else 'Subsection Chapter'
            return root / 'Content' / section
    return root / 'To Review' / 'Other'


def unique_path(target: Path) -> Path:
    if not target.exists():
        return target
    index = 1
    while True:
        candidate = target.with_name(f'{target.stem} ({index}){target.suffix}')
        if not candidate.exists():
            return candidate
        index += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project', type=Path, help='Root directory of the CS AI Study module')
    parser.add_argument('incoming', type=Path, help='Folder containing new files to sort')
    parser.add_argument('--apply', action='store_true', help='Actually sort files (default: preview only)')
    parser.add_argument('--copy', action='store_true', help='Copy rather than move (requires --apply)')
    parser.add_argument('--recursive', action='store_true', help='Include files in incoming subfolders')
    args = parser.parse_args()
    root = args.project.expanduser().resolve()
    incoming = args.incoming.expanduser().resolve()
    if not root.is_dir() or not incoming.is_dir():
        parser.error('Both project and incoming must be existing folders. Extract the ZIP first.')
    if incoming == root or root in incoming.parents or incoming in root.parents:
        parser.error('Use a separate incoming folder outside the project tree to avoid unintended moves.')
    if args.copy and not args.apply:
        parser.error('--copy must be used with --apply')
    members_dir = root / 'Assets' / 'Personal Assets'
    members = sorted((p.name for p in members_dir.iterdir() if p.is_dir()), key=len, reverse=True) if members_dir.exists() else []
    files = sorted(p for p in (incoming.rglob('*') if args.recursive else incoming.iterdir()) if p.is_file())
    if not files:
        print('No files found in the incoming folder.')
        return
    for src in files:
        folder = choose_destination(src, root, members)
        dest = unique_path(folder / src.name)
        print(f'{"COPY" if args.copy else "MOVE" if args.apply else "PREVIEW"}: {src.name} -> {dest.relative_to(root)}')
        if args.apply:
            folder.mkdir(parents=True, exist_ok=True)
            if args.copy:
                shutil.copy2(src, dest)
            else:
                shutil.move(str(src), str(dest))
    print(f'\n{len(files)} file(s) {"processed" if args.apply else "previewed"}.')


if __name__ == '__main__':
    main()
