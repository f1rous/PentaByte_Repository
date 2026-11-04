# PentaByte — Detailed Learning Content (Version 3.0)

## Algorithms, Data Structures, and Connectionist AI

### A Beginner's Guide to Learning Through Problems

**Unit II:** Core Data Structures and Problem-Solving Algorithms  
**Chapters:** 4–8  
**Team:** PentaByte  
**Based on:** Focused Project Content Outline, 25 October 2026  
**Audience:** Beginning university students with little or no programming experience  
**Example language:** Python 3  
**Document type:** Detailed Markdown lesson draft; suitable for reuse in the study guide, PPT, and demonstrations

---

# Unit II — Core Data Structures and Problem-Solving Algorithms

## Unit Introduction

In Unit I, we described a problem, wrote its solution as an algorithm, implemented simple Python instructions, and considered algorithm efficiency. Yet solving a real problem also requires us to decide **how information should be stored**. Even a correct algorithm can be difficult to use if the data is organized poorly.

This unit continues with three connected classroom examples:

- **Student scores and IDs** help us understand lists, dictionaries, sets, and searching.  
- **Undo histories and help-desk waiting lines** show why stacks and queues behave differently.  
- **A five-location campus map** introduces graphs and a simple route-finding algorithm.

Chapters 4–6 explain ways to organize and connect information. Chapters 7–8 then use those structures to find, order, and explore information. The goal is not to memorize every computer-science data structure; it is to **recognize the problem, choose a suitable structure, and trace a working solution**.

**Learning pathway:**

`Store information → Choose a structure → Find/sort records → Represent connections → Explore a route`

**After completing Unit II, learners should be able to:**

1. Update an indexed Python list and describe what changes after an insertion or removal.  
2. Distinguish a stack, queue, dictionary, and set by the operations each supports.  
3. Identify a tree, heap, and graph from simple diagrams; represent a small graph with an adjacency list.  
4. Trace linear search, binary search, and insertion sort; state when binary search is valid.  
5. Trace breadth-first search (BFS) and explain its shortest-path guarantee in an **unweighted** graph.  
6. Read and modify the supplied Python examples rather than constructing every algorithm from scratch.

---

# Chapter 4 — Data Organization, Arrays, and Python Lists

**Starting problem:** *How should we store and update a class's scores?*

Imagine a teacher keeping a record of students' quiz scores. New students may join the class, a grade may need correction, and a registration may be removed. Writing a separate variable for each score would make these changes difficult. We need a collection that is easy to read and update.

**Learning objective:** Understand indexed collections and perform basic list operations while keeping student records meaningful.

## 4.1 Understand indexed collections: arrays and Python lists

A **data structure** is a way to organize data so that a program can work with it. A **collection** stores several values together. An **indexed collection** lets us refer to individual items by their positions.

A traditional **array** is an indexed sequence of elements; in many programming languages and contexts, arrays store elements of a common type. A **Python list** is also indexed, but it can grow or shrink dynamically and can hold values of different types. In this guide, we use Python lists rather than implementing a lower-level array.

Consider the list:

scores \= \[72, 85, 68, 91, 85\]

Each value has an **index**. Python starts counting positions from **zero**, not one.

Index:     0    1    2    3    4

           \|    \|    \|    \|    \|

Scores:  \[72,  85,  68,  91,  85\]

For example, `scores[0]` is `72`, while `scores[3]` is `91`. An index and the value at that index are not the same thing: the index tells us **where**, and the value tells us **what**.

**Read an item and inspect the length:**

scores \= \[72, 85, 68, 91, 85\]

print("First score:", scores\[0\])

print("Fourth score:", scores\[3\])

print("Number of scores:", len(scores))

**Expected output:**

First score: 72

Fourth score: 91

Number of scores: 5

A list preserves order, but scores alone do not identify which student earned which result. We will improve that later in this chapter.

## 4.2 Access, add, update, remove, and loop through list items

A Python list supports several everyday operations:

| Action | Python expression | Effect |
| :---- | :---- | :---- |
| Access | `scores[2]` | Read the third item |
| Update | `scores[2] = 78` | Replace the third item with `78` |
| Add at end | `scores.append(76)` | Add a new item at the end |
| Insert at position | `scores.insert(1, 90)` | Add an item at index 1; shift later items |
| Remove by index | `scores.pop(1)` | Remove and return the item at index 1 |
| Remove first matching value | `scores.remove(85)` | Remove the first occurrence of `85` |
| Visit items | `for score in scores:` | Process one score at a time |

**Important distinction:** `pop(index)` removes an item at a known *position*, whereas `remove(value)` removes the *first matching value*. When duplicate scores exist, removing a student based only on the score is unreliable.

**Worked example — Three changes to the class list**

Starting list: `[72, 85, 68, 91, 85]`.

1. **Add** a new score, `76`, at the end.  
2. **Correct** the original score `68` to `78` at index `2`.  
3. **Remove** the registration occupying index `1` (whose score is `85`).

| Stage | Operation | Resulting list |
| :---- | :---- | :---- |
| Original | — | `[72, 85, 68, 91, 85]` |
| Add | `append(76)` | `[72, 85, 68, 91, 85, 76]` |
| Correct | `scores[2] = 78` | `[72, 85, 78, 91, 85, 76]` |
| Remove | `pop(1)` | `[72, 78, 91, 85, 76]` |

**Runnable demonstration:**

scores \= \[72, 85, 68, 91, 85\]

scores.append(76)

print("After addition:", scores)

scores\[2\] \= 78

print("After correction:", scores)

removed\_score \= scores.pop(1)

print("Removed score:", removed\_score)

print("After removal:", scores)

print("Remaining scores:")

for score in scores:

    print(score)

**Expected first four output lines:**

After addition: \[72, 85, 68, 91, 85, 76\]

After correction: \[72, 85, 78, 91, 85, 76\]

Removed score: 85

After removal: \[72, 78, 91, 85, 76\]

Why do indexes change? When we remove an item, every item after that position shifts one index to the left. A position should not be treated as a permanent student identifier.

## 4.3 Store simple student records and choose update operations

To connect a score with a particular student, we can store simple **records**. Here, each record is a dictionary holding an ID and a score; Chapter 5 explains dictionaries more fully.

students \= \[

    {"id": "S01", "score": 72},

    {"id": "S02", "score": 85},

    {"id": "S03", "score": 68},

\]

\# Correct the record with ID S03.

for student in students:

    if student\["id"\] \== "S03":

        student\["score"\] \= 78

        break

\# Register a new student.

students.append({"id": "S04", "score": 76})

for student in students:

    print(student\["id"\], student\["score"\])

**Expected output:**

S01 72

S02 85

S03 78

S04 76

This is safer than relying on a student's current list position. A record's ID continues to identify the same student even if the list order changes.

**Choosing a useful operation:**

- Use an **index** when the intended position is known and meaningful.  
- Use **`append()`** when adding another record at the end.  
- Use a **student ID** to locate a particular record when the list might change order.  
- Do not delete a record just because its score equals another student's score.

**Reader action — Predict and modify:** Start from the original five-score list. Add `76`; correct `68` to `78`; then remove the item at index `1`. Write down the list after each operation *before* running the code. Why would `remove(85)` be a poor choice if we meant to delete a particular student's registration?

**Answer / hint:** The lists are shown in the trace table above. The value `85` appears twice, so the score itself is not a unique identifier. A student ID is more reliable.

**Chapter 4 takeaway:** A Python list is an ordered, indexed, changeable collection; selecting the correct update operation matters, especially when values repeat.

---

# Chapter 5 — Stacks, Queues, Dictionaries, and Sets

**Starting problem:** *How should we handle an undo history, a waiting line, and student-ID lookups?*

A single way of storing information is not ideal for every task. Undoing an action, serving people in arrival order, finding a student by ID, and removing duplicate IDs involve different rules. The **data structure** we choose should match those rules.

**Learning objective:** Recognize which structure fits a task and perform simple operations with Python's built-in tools.

## 5.1 Compare stacks and queues; recognize linked nodes

A **stack** uses **last in, first out (LIFO)** order. Imagine stacking books: the last book placed on top is the first one removed. A text editor's undo history follows a similar idea: the most recent action is undone first.

Stack — last in, first out

Add A, then B, then C:

  TOP → \[ C \]   ← removed first

        \[ B \]

        \[ A \]

Removal order: C → B → A

A **queue** uses **first in, first out (FIFO)** order. Imagine students waiting at an information desk: those who joined earlier are normally served earlier.

Queue — first in, first out

Front                         Back

  ↓                            ↓

\[ A \] → \[ B \] → \[ C \]

  ↑

removed first

Removal order: A → B → C

| Property | Stack | Queue |
| :---- | :---- | :---- |
| Rule | Last in, first out | First in, first out |
| Add operation | Push onto top | Enqueue at back |
| Remove operation | Pop from top | Dequeue from front |
| Common example | Undo history | Service waiting line |

We can represent a stack with a Python list and a queue with `collections.deque`, which is designed to support efficient additions and removals at both ends:

from collections import deque

\# Stack: last in, first out

undo\_stack \= \[\]

for task in \["A", "B", "C"\]:

    undo\_stack.append(task)

stack\_order \= \[\]

while undo\_stack:

    stack\_order.append(undo\_stack.pop())

\# Queue: first in, first out

help\_queue \= deque(\["A", "B", "C"\])

queue\_order \= \[\]

while help\_queue:

    queue\_order.append(help\_queue.popleft())

print("Stack removal:", stack\_order)

print("Queue removal:", queue\_order)

**Expected output:**

Stack removal: \['C', 'B', 'A'\]

Queue removal: \['A', 'B', 'C'\]

**A brief linked-list connection:** A linked list consists of **nodes**, each of which holds some data and a connection to another node. It is different from a Python list's ordinary indexed view.

Head

 ↓

\[A \| next\] → \[B \| next\] → \[C \| none\]

This illustration is enough for our guide. We will **not** implement a linked list from scratch, because our learning goal is to recognize the structure rather than study its internal memory management.

## 5.2 Use dictionaries, sets, and the basic idea of hashing

A **dictionary** stores **key–value pairs**. A key, such as a student ID, identifies a corresponding record. Rather than searching a score list to discover whose result we need, we can ask for the value associated with a known ID.

student\_scores \= {

    "S01": 72,

    "S02": 85,

    "S03": 68,

}

print("S02's score:", student\_scores\["S02"\])

print("Unknown student:", student\_scores.get("S99", "Not found"))

**Expected output:**

S02's score: 85

Unknown student: Not found

`student_scores["S02"]` retrieves the value for an existing key. `get("S99", "Not found")` lets us provide a clear default when a key is absent instead of causing a `KeyError`.

A Python dictionary is implemented using a **hash table**. At a beginner level, we can think of hashing as a technique that helps the program locate values from keys efficiently. Average dictionary lookup is typically **O(1)**, although this is not a guarantee for every possible situation. We do not need to study hash collisions or table implementation in this unit.

A **set** stores unique elements. This makes it convenient for tracking registered IDs or testing membership without allowing duplicates.

registrations \= \["S01", "S02", "S01"\]

unique\_ids \= set(registrations)

print("Unique IDs:", sorted(unique\_ids))

print("Number of unique IDs:", len(unique\_ids))

print("Is S02 registered?", "S02" in unique\_ids)

**Expected output:**

Unique IDs: \['S01', 'S02'\]

Number of unique IDs: 2

Is S02 registered? True

We use `sorted()` when displaying the set because a set itself **does not promise a meaningful order**.

**Important distinction:** A dictionary associates **one key with a value**; a set mainly answers **which distinct values belong to a collection**.

## 5.3 Choose the right structure for a real problem

Consider a simple student-service application. It needs to record several different kinds of information:

| Problem | Suitable structure | Why it fits |
| :---- | :---- | :---- |
| Undo the latest editing action | Stack | Most recent action comes out first |
| Process help requests by arrival | Queue | Earliest request comes out first |
| Retrieve a score by student ID | Dictionary | The ID serves as a key |
| Keep each registered ID only once | Set | Duplicate values are removed |
| Keep scores in a visible sequence | List | Supports order, indexing, and iteration |

A real program may use **several structures together**. For example, the program can use a dictionary to find a student's score, a set to check whether an ID is registered, and a queue to manage help requests.

**Worked example — Adding task D:**

If tasks arrive in the order A, B, C, D:

- Stack removal order: `D → C → B → A`.  
- Queue removal order: `A → B → C → D`.

These are different because the rules for removing items are different, **not** because the letters changed.

**Reader action — Predict and modify:** Add task `D` to the stack and queue example. Predict the complete removal order before running it. Then change the registration list to `['S01', 'S02', 'S01', 'S03', 'S03']`: how many distinct IDs remain?

**Answer / hint:** The stack gives D–C–B–A, the queue gives A–B–C–D, and the set has three distinct IDs (`S01`, `S02`, `S03`).

**Chapter 5 takeaway:** Data structures encode different rules for storing and retrieving information; choose a structure to match the required operation.

---

# Chapter 6 — Trees, Heaps, and Graph Representations

**Starting problem:** *How do we represent folders, urgent tasks, and connected campus locations?*

Some kinds of information are better understood by describing **relationships** rather than only writing a list. A folder has subfolders, tasks have priorities, and buildings connect by paths. We will briefly recognize trees and heaps, then focus on a graph that we will use again in Chapter 8\.

**Learning objective:** Recognize common relationship structures and construct a five-location, undirected graph in Python.

## 6.1 Recognize a tree as a hierarchy and a heap as a priority structure

A **tree** is a structure that organizes elements hierarchically. A tree has a top-level **root** and elements connected by **parent–child** relationships. A simple example is a folder system:

Course Materials (root)

├── Lectures

│   ├── Week 1

│   └── Week 2

└── Assignments

    ├── Task A

    └── Task B

Here, `Lectures` and `Assignments` are children of `Course Materials`. `Week 1` is a child of `Lectures`. This diagram shows how a tree helps explain containment and hierarchy.

A **heap** is a particular tree-based structure organized around a priority rule. For example, in a **max-heap**, a parent has a value at least as large as its children. This helps make a highest-priority item readily available.

Example max-heap (illustrative priorities)

          9

         / \\

        7   8

       / \\

      2   4

The number at the top is the greatest priority in this example. A heap is **not** the same as an entirely sorted list: it guarantees a parent–child ordering property, not that every value is globally in sorted sequence.

**Scope note:** We use these structures only as visual introductions. We will not write tree insertion code or implement a heap in this guide.

## 6.2 Represent graphs using vertices, edges, and an adjacency list

A **graph** represents entities and the connections among them:

- A **vertex (node)** represents a place or object.  
- An **edge** represents a connection between two vertices.  
- An **adjacency list** records which other vertices connect directly to each vertex.

For a campus map, vertices can represent `Dorm`, `Library`, `Canteen`, `Lab`, and `Gate`. An edge can represent a walkable connection between two locations.

Our example graph is **undirected**: if a path connects Dorm and Library, the same connection works from Library to Dorm. The edges are **unweighted**: we are not storing distances or travel times.

**Five-location campus graph (schematic, not to geographical scale):**

Dorm ───── Library ───── Lab

  │                         │

  │                         │

Canteen ───── Gate ─────────┘

This is a schematic of the five intended edges:

1. Dorm — Library  
2. Dorm — Canteen  
3. Library — Lab  
4. Canteen — Gate  
5. Gate — Lab

An adjacency list for those five edges is:

| Vertex | Direct neighbors |
| :---- | :---- |
| Dorm | Library, Canteen |
| Library | Dorm, Lab |
| Canteen | Dorm, Gate |
| Lab | Library, Gate |
| Gate | Canteen, Lab |

**Python representation:**

campus \= {

    "Dorm": \["Library", "Canteen"\],

    "Library": \["Dorm", "Lab"\],

    "Canteen": \["Dorm", "Gate"\],

    "Lab": \["Library", "Gate"\],

    "Gate": \["Canteen", "Lab"\],

}

for location, neighbors in campus.items():

    print(location, "connects to", neighbors)

This representation is easy to read and modify. Because the graph is undirected, each connection appears in **both directions** in the dictionary.

## 6.3 Build the campus map and add one new connection

Suppose the campus adds a direct walkway from the **Dorm** to the **Gate**. We must update both neighbor lists because the connection is undirected.

campus \= {

    "Dorm": \["Library", "Canteen"\],

    "Library": \["Dorm", "Lab"\],

    "Canteen": \["Dorm", "Gate"\],

    "Lab": \["Library", "Gate"\],

    "Gate": \["Canteen", "Lab"\],

}

\# Add a two-way walkway without duplicating an existing edge.

if "Gate" not in campus\["Dorm"\]:

    campus\["Dorm"\].append("Gate")

if "Dorm" not in campus\["Gate"\]:

    campus\["Gate"\].append("Dorm")

print("Dorm neighbors:", campus\["Dorm"\])

print("Gate neighbors:", campus\["Gate"\])

**Expected output:**

Dorm neighbors: \['Library', 'Canteen', 'Gate'\]

Gate neighbors: \['Canteen', 'Lab', 'Dorm'\]

Now a traveler can go directly from Dorm to Gate in a single connection rather than using Dorm → Canteen → Gate. The actual time saved cannot be determined from this graph alone; edge lengths are not represented.

**Reader action — Predict and modify:** Before executing the code, draw a new edge between Dorm and Gate on paper. List the neighbors of both locations after the change. What would go wrong if we added `Gate` to `Dorm` but forgot to add `Dorm` to `Gate`?

**Answer / hint:** The two affected lists are displayed above. Updating only one direction would make the adjacency list **inconsistent with the intended undirected map**, incorrectly suggesting the connection works in only one direction.

**Chapter 6 takeaway:** Trees show hierarchies, heaps support priority selection, and graphs represent relationships; an adjacency list describes a graph in a form programs can use.

---

# Chapter 7 — Searching and Elementary Sorting

**Starting problem:** *How can we find a student record and put scores in order?*

Searching is the act of locating an item. Sorting arranges items according to a rule. A student-record program might need to find a particular score or display scores from lowest to highest. Two search methods can produce the same answer but perform different numbers of checks.

**Learning objective:** Trace linear search, binary search, and a basic insertion-sort example; recognize the assumptions and growth patterns involved.

## 7.1 Trace linear search and binary search

**Linear search** checks the list from the beginning, one item at a time, until it finds the target or reaches the end. It also works when the input is not sorted.

Consider the sorted score list:

`[68, 72, 85, 91, 96]`

We want to find `85`.

| Linear-search step | Index inspected | Value | Found? |
| :---- | ----: | ----: | :---- |
| 1 | 0 | 68 | No |
| 2 | 1 | 72 | No |
| 3 | 2 | 85 | Yes |

Linear search needs **3 checks** here.

**Binary search** repeatedly examines the middle element of a **sorted list** and discards the half that cannot contain the target.

In our five-item list, the middle index is `2`, whose value is `85`. Therefore, binary search finds the target in **1 check** in this particular example.

Sorted list:

Index:      0    1    2    3    4

Value:     68   72   85   91   96

                     ↑

                  Middle \= 85

                  Target found

If the target were `91`, the first middle value would be `85`; the search would discard the left half and continue in the right half. **Binary search assumes the list is already sorted according to the same comparison rule.** Applying it to arbitrary unsorted values can give an incorrect result.

**Runnable search demonstration:**

def linear\_search(values, target):

    for index, value in enumerate(values):

        if value \== target:

            return index

    return \-1

def binary\_search(sorted\_values, target):

    left \= 0

    right \= len(sorted\_values) \- 1

    while left \<= right:

        middle \= (left \+ right) // 2

        value \= sorted\_values\[middle\]

        if value \== target:

            return middle

        if value \< target:

            left \= middle \+ 1

        else:

            right \= middle \- 1

    return \-1

scores \= \[68, 72, 85, 91, 96\]

print("Linear index:", linear\_search(scores, 85))

print("Binary index:", binary\_search(scores, 85))

print("Missing item:", binary\_search(scores, 99))

**Expected output:**

Linear index: 2

Binary index: 2

Missing item: \-1

Returning `-1` is a simple convention indicating that the value was not found; it is **not** a valid index returned by these two functions for a successful match.

## 7.2 Trace insertion sort and use Python's built-in sorting

**Insertion sort** works much like sorting playing cards in your hand. It treats the left portion of a list as sorted and inserts the next value into its correct position there.

Start with `[85, 68, 91, 72]`.

| Pass | Value to insert | Explanation | List after pass |
| :---- | ----: | :---- | :---- |
| Start | — | First item is treated as sorted | `[85, 68, 91, 72]` |
| 1 | 68 | Move 85 right; insert 68 before it | `[68, 85, 91, 72]` |
| 2 | 91 | Already larger than 85; leave in place | `[68, 85, 91, 72]` |
| 3 | 72 | Shift 91 and 85; insert 72 | `[68, 72, 85, 91]` |

**Sorted result:** `[68, 72, 85, 91]`.

This hand trace is the main learning activity. In ordinary Python applications, a built-in sorting operation is often simpler and more appropriate than writing your own sort:

scores \= \[85, 68, 91, 72\]

ordered\_scores \= sorted(scores)

print("Original:", scores)

print("Sorted:", ordered\_scores)

**Expected output:**

Original: \[85, 68, 91, 72\]

Sorted: \[68, 72, 85, 91\]

`sorted(scores)` produces a **new** list, leaving `scores` unchanged. In contrast, `scores.sort()` sorts that existing list in place.

**Scope note:** We will trace insertion sort to understand its principle, but we do not need to implement several competing sorting algorithms for this project.

## 7.3 Compare search checks and connect repeated halving to O(log n)

The number of checks depends on both the input size and the search method.

- **Linear search:** In the worst case, it may inspect all `n` values, giving **O(n)** time.  
- **Binary search:** For a sorted sequence with efficient indexed access, the remaining search region is approximately halved after each unsuccessful comparison, giving **O(log n)** time.  
- **Insertion sort:** In the worst case, inserting many values requires repeatedly shifting earlier elements, giving **O(n²)** time. This complexity is a useful connection to Unit I, but our focus remains the worked trace.

**Illustration of repeated halving:**

About 32 candidate values

          ↓

About 16 remain

          ↓

About 8 remain

          ↓

About 4 remain

          ↓

About 2 remain

          ↓

About 1 remains

Binary search can be substantially more efficient for repeated lookups **when the input is already sorted**. However, if we must sort an unsorted list first, that preparation also costs work. The appropriate choice depends on the actual task, not only on the Big O label of a single search.

**Reader action — Predict and modify:** Using `[68, 72, 85, 91, 96]`, search for `91`. Trace the middle indexes visited by binary search, then trace how many values linear search inspects. Next, arrange `[85, 68, 91, 72]` using insertion-sort passes without running any code.

**Answer / hint:** Binary search checks index `2` (`85`), then index `3` (`91`): **2 checks**. Linear search checks `68`, `72`, `85`, `91`: **4 checks**. The insertion-sort result is `[68, 72, 85, 91]`.

**Chapter 7 takeaway:** Searching and sorting are basic tools for finding information; binary search gains its speed by exploiting sorted order, while insertion sort demonstrates how ordering can be built one item at a time.

---

# Chapter 8 — Graph Traversal and Shortest Paths

**Starting problem:** *Which route crosses the fewest connections on our campus map?*

A graph tells us which locations are connected, but it does not automatically answer a route question. We need an **algorithm** to explore possible connections. For this introductory project, we use **breadth-first search (BFS)** to find a route with the fewest edges in an unweighted graph.

**Learning objective:** Follow BFS using a queue and visited locations, reconstruct a shortest route, and test a map where a destination cannot be reached.

## 8.1 Explore a graph with breadth-first search, a queue, and visited locations

**Breadth-first search** explores nearby vertices before moving farther away. Starting at a vertex, it visits vertices one edge away, then those two edges away, and so on.

Three useful pieces of information are:

1. A **queue** of vertices to examine next (first in, first out).  
2. A **visited set** to avoid processing the same vertex repeatedly.  
3. A **parent record** to remember how each discovered vertex was reached.

We reuse the original Chapter 6 graph, **without** the optional Dorm–Gate walkway:

Dorm ───── Library ───── Lab

  │                         │

  │                         │

Canteen ───── Gate ─────────┘

The question is: **How do we travel from Dorm to Lab using the fewest graph connections?**

Compare two possible routes:

- Dorm → Library → Lab: **2 edges**.  
- Dorm → Canteen → Gate → Lab: **3 edges**.

The first route uses fewer edges. BFS discovers vertices by increasing edge distance from the start, so it can find such a route in an **unweighted** graph.

## 8.2 Trace a supplied BFS example and reconstruct the route

To make the trace predictable, we examine neighbors in the exact order shown in the adjacency list: Dorm's neighbors are Library first, then Canteen.

**Trace of the exploration:**

| Step | Vertex removed from queue | Newly discovered vertices | Queue after step |
| :---- | :---- | :---- | :---- |
| Start | — | Dorm (starting point) | `[Dorm]` |
| 1 | Dorm | Library, Canteen | `[Library, Canteen]` |
| 2 | Library | Lab | `[Canteen, Lab]` |
| 3 | Canteen | Gate | `[Lab, Gate]` |
| 4 | Lab | Target reached | Stop |

When Library discovers Lab, we store `parent["Lab"] = "Library"`. Earlier, Dorm discovered Library, so `parent["Library"] = "Dorm"`. Following these parent links backward reconstructs:

Lab ← Library ← Dorm

Reverse the sequence:

Dorm → Library → Lab

**Runnable BFS demonstration:**

from collections import deque

campus \= {

    "Dorm": \["Library", "Canteen"\],

    "Library": \["Dorm", "Lab"\],

    "Canteen": \["Dorm", "Gate"\],

    "Lab": \["Library", "Gate"\],

    "Gate": \["Canteen", "Lab"\],

}

def shortest\_path(graph, start, goal):

    """Return a fewest-edge path, or None if no path exists."""

    if start not in graph or goal not in graph:

        return None

    queue \= deque(\[start\])

    visited \= {start}

    parent \= {start: None}

    while queue:

        current \= queue.popleft()

        if current \== goal:

            path \= \[\]

            while current is not None:

                path.append(current)

                current \= parent\[current\]

            return list(reversed(path))

        for neighbor in graph\[current\]:

            if neighbor not in visited:

                visited.add(neighbor)

                parent\[neighbor\] \= current

                queue.append(neighbor)

    return None

route \= shortest\_path(campus, "Dorm", "Lab")

print("Route:", " \-\> ".join(route) if route else "Unreachable")

print("Number of edges:", len(route) \- 1 if route else "N/A")

**Expected output:**

Route: Dorm \-\> Library \-\> Lab

Number of edges: 2

**Why is a visited set necessary?** Our undirected map contains connections in both directions. Without tracking discovered locations, a program could repeatedly add Dorm after visiting Library, then add Library again after visiting Dorm. Recording a vertex as visited when it enters the queue prevents this unnecessary repetition.

## 8.3 Change a connection, test an unreachable destination, and interpret the result

A route depends on which edges actually exist. Suppose both connections to Lab are closed:

- Library — Lab is removed.  
- Gate — Lab is removed.

Now Lab has no remaining links, so there is **no route from Dorm to Lab** in our graph.

**Runnable continuation:** Run the Chapter 8 BFS code above first, then run this cell.

\# Make a separate graph so the original campus map remains unchanged.

blocked\_campus \= {

    location: neighbors.copy()

    for location, neighbors in campus.items()

}

\# Remove both undirected connections to the Lab.

for neighbor in \["Library", "Gate"\]:

    blocked\_campus\[neighbor\].remove("Lab")

    blocked\_campus\["Lab"\].remove(neighbor)

blocked\_route \= shortest\_path(blocked\_campus, "Dorm", "Lab")

print("Route after closures:", blocked\_route)

print("Lab neighbors:", blocked\_campus\["Lab"\])

**Expected output:**

Route after closures: None

Lab neighbors: \[\]

This result is **not an error**: it correctly reports that the destination is unreachable through the available connections.

**An important limitation:** An unweighted BFS route minimizes the **number of edges**, not necessarily the walking distance or travel time. A direct connection could be physically longer than a two-edge route. To minimize measured distances, a model would need edge weights and an appropriate method; those are outside the implementation scope of this guide.

**Small connection to other algorithm ideas:** Some algorithms solve a large problem by breaking it into smaller ones (divide and conquer), and some choose locally promising options (greedy strategies). Those are useful wider concepts, but for this project we do not add separate recursion, greedy, DFS, or Dijkstra implementation lessons.

**Reader action — Predict and modify:**

1. Before running the code, predict the Dorm-to-Lab route and the number of edges.  
2. Remove both links to Lab. What should BFS return?  
3. Restore the original map, then add the optional Dorm–Gate connection from Chapter 6\. Does it make Dorm → Lab shorter in **edge count**?

**Answer / hint:** The original route has 2 edges: Dorm → Library → Lab. After both Lab links are removed, the destination is unreachable, so the function returns `None`. Adding Dorm–Gate creates the route Dorm → Gate → Lab, also **2 edges**; it does not improve the minimum edge count. Depending on neighbor order, BFS may return either of the two-edge routes.

**Chapter 8 takeaway:** BFS uses a queue and a visited set to explore an unweighted graph in increasing edge distance; parent links reconstruct a fewest-edge route, and `None` can represent an unreachable destination.

---

# Unit II — Consolidated Learning Review

## How the five chapters connect

| Chapter | Core idea | Reused example | Skill gained |
| :---- | :---- | :---- | :---- |
| 4 | Indexed lists and record updates | Student scores | Add, correct, and remove data |
| 5 | Structures for different retrieval rules | Help-desk tasks and student IDs | Choose stack, queue, dictionary, or set |
| 6 | Relationships between objects | Five-location campus | Draw and encode a graph |
| 7 | Finding and ordering information | Student scores | Trace searches and insertion sort |
| 8 | Exploring connections | Campus graph | Find a fewest-edge route with BFS |

The lessons form one connected sequence. We first represent values with lists, then choose specialized structures for different problems. Next, we model connections with graphs. Finally, we use algorithms to find records and routes.

## Quick self-check questions

**Q1 — Lists:** Starting with `[10, 20, 30]`, what is the result after `append(40)` and then `pop(1)`?

**Q2 — Structures:** Which structure would you use for each task: (a) undo the latest change, (b) serve requests in arrival order, (c) look up a score by unique student ID, (d) keep IDs without duplicates?

**Q3 — Graphs:** In an undirected graph, if the adjacency list for Dorm contains Library, what must the adjacency list for Library contain?

**Q4 — Search:** Which method requires sorted input: linear search or binary search? Why?

**Q5 — Sorting:** Trace insertion sort on `[9, 4, 7]`. What does the list look like after each pass?

**Q6 — BFS:** In an unweighted campus graph, what does BFS minimize: number of edges, physical distance, or travel time? What does `None` mean in the supplied route-finding function?

### Answers and brief explanations

1. `[10, 30, 40]`: `append()` adds `40`, then `pop(1)` removes `20`.  
2. (a) Stack; (b) Queue; (c) Dictionary; (d) Set.  
3. `Dorm`, because an undirected connection works in both directions.  
4. Binary search. Its logic discards half the candidates based on comparisons with ordered values; an unsorted list does not justify that choice.  
5. Start `[9, 4, 7]`; after inserting `4`: `[4, 9, 7]`; after inserting `7`: `[4, 7, 9]`.  
6. BFS minimizes **edge count** in an unweighted graph. In our function, `None` means the goal is missing from the graph or no path can reach it.

## Optional collaborative demonstration

One teammate can operate a student-score list while another explains each change. A third can hold task cards A, B, and C and demonstrate stack versus queue removal. Finally, the team can draw the five-location campus map and use the BFS trace table to act out discovering vertices and reconstructing a route.

This is a **suggested teaching activity**, not an additional compulsory chapter or project.

## Bridge to Unit III — Connectionist AI: Data, Neurons, and Networks

Algorithms and data structures will continue to matter when we study machine learning. A future classifier needs information organized as usable samples and features; we also need algorithms that process those values and track results. In Unit III, the guide shifts from writing fixed rules for data processing to exploring how connected artificial neurons combine numerical inputs and produce predictions.

**Next chapters:** 9–12 — AI, Machine Learning, and Connectionism; Learning from Data; Artificial Neurons; and Neural Network Layers and Forward Propagation.

---

# Instructor / Team Production Notes

- **Source alignment:** This draft expands the provided PentaByte focused outline's Chapters 4–8 while preserving the specified three numbered subtopics, student-record example, five-location campus graph, and worked activities.  
- **Scope:** Linked lists, trees, and heaps are recognized conceptually only. No linked-list implementation, hash-collision handling, heap implementation, DFS or Dijkstra implementation, or extra sorting-algorithm survey has been added.  
- **Illustrations:** All text diagrams are original teaching schematics rather than externally sourced images. The campus map is fictional and not geographically scaled.  
- **Code:** Python examples use the standard library only and are designed for Python 3\. The Chapter 8 closure example must be run after the BFS definition in Chapter 8.2.  
- **Video/PPT reuse:** Chapter 4 can supply a short list-update demo; Chapters 5–6 supply visual comparisons; Chapters 7–8 supply algorithm traces. The team's video plan may select representative concepts rather than narrating all five chapters.  
- **Further references:** For production, consider linking to the official *Python Tutorial* (data structures) and the Python `collections` documentation. Add any required credits and AI-use disclosure to the team repository before submission.

**End of Unit II — Core Data Structures and Problem-Solving Algorithms**