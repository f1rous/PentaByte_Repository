# PentaByte — Detailed Learning Content (Version 3.0)

## Algorithms, Data Structures, and Connectionist AI

### A Beginner's Guide to Learning Through Problems

**Unit I:** Computational Thinking and Python Foundations  
**Chapters:** 1–3  
**Team:** PentaByte  
**Based on:** Focused Project Content Outline, 25 October 2026  
**Audience:** Beginning university students with little or no programming experience  
**Example language:** Python 3

---

# Unit I — Computational Thinking and Python Foundations

## Unit Introduction

Computers can process large amounts of information, but they need clearly stated instructions. Before studying complex data structures or artificial intelligence, learners should understand three connected ideas: how to define a problem, how to express its solution in Python, and how to judge the resources a solution needs.

This unit uses **one recurring classroom problem**: a teacher wants to understand students' test scores. Using the same list of scores throughout makes it easier to see how an idea becomes an algorithm, how an algorithm becomes code, and how code can be evaluated.

**Learning pathway:**

`Problem → Algorithm → Python program → Efficiency analysis`

By the end of Unit I, readers should be able to:

1. Identify the inputs, outputs, and steps of a small computational problem.  
2. Write and manually trace simple pseudocode.  
3. Read and modify a Python program using variables, lists, conditions, loops, and functions.  
4. Recognize basic time-complexity patterns and distinguish runtime growth from memory use.  
5. Explain why checking empty input and other unusual cases matters.

---

# Chapter 1 — From Problems to Algorithms

**Starting problem:** *How can we find the highest score in a class?*

Imagine a teacher has recorded five scores: `[72, 85, 68, 91, 85]`. Finding the highest score by looking at this short list is easy. But what if the teacher has 3,000 scores? We want a method that is precise enough for a computer to follow and reliable enough to work with different lists.

**Learning objective:** Convert a real-life question into a clear sequence of logical steps and verify the result by tracing examples.

## 1.1 Identify the inputs, expected output, and smaller steps

An **algorithm** is a finite, well-defined sequence of steps for accomplishing a task. An algorithm does not have to be written in a programming language; it can first be expressed as plain instructions or pseudocode.

For our problem:

| Element | Description | Example |
| :---- | :---- | :---- |
| Input | A collection of student scores | `[72, 85, 68, 91, 85]` |
| Output | The highest score, or a message if none exists | `91` |
| Process | Inspect each score and remember the largest seen | Compare 72, 85, 68, 91, 85 |
| Special case | The list is empty | `[]` → `No scores available` |

We can **decompose** the task into smaller actions: check whether any score exists; choose the first score as the current highest; inspect each remaining score; replace the current highest when a larger score appears; report the result.

The empty-list check is essential. If no score exists, there is no first value to use as an initial maximum. A robust solution needs an explicitly defined response instead of failing unexpectedly.

We also distinguish the **problem** from the **method**: the problem asks for the highest score, while the algorithm explains how to obtain it. Different methods may solve the same problem but require different time or memory.

## 1.2 Express the solution in pseudocode, then trace decisions

**Pseudocode** is a language-independent description of a program. It shows the intended logic without requiring exact Python syntax.

ALGORITHM FindHighestScore(scores)

    IF scores is empty THEN

        RETURN "No scores available"

    END IF

    highest ← first element of scores

    FOR each remaining score in scores DO

        IF score \> highest THEN

            highest ← score

        END IF

    END FOR

    RETURN highest

END ALGORITHM

The arrow `←` means “assign a value.” The condition `score > highest` asks whether the newly examined score is larger than the best result so far.

**Visual decision path:**

Start

  \|

Is the list empty? \-- Yes \--\> Report: No scores available

  \|

  No

  \|

Set highest to first score

  \|

Examine each remaining score

  \|

Is score \> highest? \-- Yes \--\> Update highest

  \|                             \|

  No \--------------------------+

  \|

Continue until all scores are checked

  \|

Report highest

A **trace** means following these instructions manually and recording the changing values. Tracing helps us discover mistakes before or after writing code.

## 1.3 Work through the highest-score example and test unusual cases

**Worked example:** `[72, 85, 68, 91, 85]`

Initialize `highest = 72`, then trace the remaining values:

| Step | Score inspected | Previous highest | Action | New highest |
| :---- | ----: | ----: | :---- | ----: |
| Initialize | 72 | — | Use first score | 72 |
| 1 | 85 | 72 | 85 is larger; update | 85 |
| 2 | 68 | 85 | Keep existing value | 85 |
| 3 | 91 | 85 | 91 is larger; update | 91 |
| 4 | 85 | 91 | Keep existing value | 91 |

**Final output: `91`.**

We should test more than one ordinary example:

| Test | Input | Expected result | Reason |
| :---- | :---- | :---- | :---- |
| Typical | `[72, 85, 68, 91, 85]` | `91` | One clear maximum |
| Repeated maximum | `[91, 85, 91]` | `91` | Equal largest values are valid |
| One value | `[74]` | `74` | No remaining comparison is needed |
| Empty list | `[]` | `No scores available` | No maximum exists |

Repeated scores cause no problem: because the condition is `>`, an equal score does not replace the current maximum. The output remains correct.

**Reader action — Predict before tracing:** Change the last score to `95`, making the list `[72, 85, 68, 91, 95]`. What should the algorithm return? Trace the steps yourself before checking the answer.

**Answer / hint:** The current maximum becomes `95` at the final comparison, so the result is **95**. For an empty list, report that no scores are available rather than inventing a maximum.

**Chapter 1 takeaway:** An algorithm converts a clearly stated problem into a sequence of steps with defined input, output, decisions, and behavior for special cases.

---

# Chapter 2 — Essential Python for the Guide

**Starting problem:** *How can we turn our score-processing steps into a working program?*

Pseudocode expresses the logic, but a computer needs instructions written in a programming language. **Python** is suitable for these introductory examples because its readable syntax allows learners to focus on how a solution works. You do not need advanced Python knowledge for this guide.

**Learning objective:** Run, understand, and safely modify a small program that processes student scores.

## 2.1 Run a prepared notebook; read variables, numbers, lists, and output

A **Jupyter notebook** runs Python code in separate cells and displays results below them. If you have a prepared notebook, open it in a Python-capable notebook environment and run its cells from top to bottom. For this lesson, the following code can also be run in a regular Python 3 editor.

scores \= \[72, 85, 68, 91, 85\]

pass\_mark \= 60

print(scores)

print("Number of students:", len(scores))

print("Required pass mark:", pass\_mark)

**Expected output:**

\[72, 85, 68, 91, 85\]

Number of students: 5

Required pass mark: 60

Key elements of this example:

| Python element | Meaning | In this example |
| :---- | :---- | :---- |
| Variable | A name referring to a value | `pass_mark` |
| Integer | A whole number | `60` |
| List | An ordered, changeable collection | `scores` |
| Assignment (`=`) | Store or bind a value to a name | `pass_mark = 60` |
| `len()` | Return the number of list items | `len(scores)` gives `5` |
| `print()` | Display information | `print(scores)` |

A list uses square brackets. Its items are ordered, and later chapters will explain how to access or update them efficiently. Here, we only need to read the list and examine its items.

## 2.2 Modify a condition, a loop, and a short function

A **condition** allows a program to make a decision. A **loop** repeats a task. A **function** packages instructions so we can reuse them.

Here is the basic building block:

scores \= \[72, 85, 68, 91, 85\]

pass\_mark \= 60

count \= 0

for score in scores:

    if score \>= pass\_mark:

        count \= count \+ 1

print("Students meeting the pass mark:", count)

**Expected output:** `Students meeting the pass mark: 5`

How it works:

1. `count = 0` starts the total at zero.  
2. `for score in scores` reads each score in the list, one after another.  
3. `if score >= pass_mark` checks whether the student meets or exceeds the passing requirement.  
4. When the condition is true, `count = count + 1` adds one.  
5. After the loop ends, `print()` displays the count.

Python uses **indentation** (consistent spaces at the start of a line) to indicate which instructions belong inside the loop and condition. If the indentation is wrong, the program may fail or behave incorrectly.

Now put the same logic in a reusable function:

def count\_passing(scores, pass\_mark):

    count \= 0

    for score in scores:

        if score \>= pass\_mark:

            count \+= 1

    return count

print(count\_passing(\[72, 85, 68, 91, 85\], 60))  \# 5

print(count\_passing(\[72, 85, 68, 91, 85\], 80))  \# 3

`def` introduces a function, parameters such as `scores` and `pass_mark` receive input values, and `return` gives the result back to the caller. `count += 1` is a shorter way of writing `count = count + 1`.

We can also implement Chapter 1's maximum algorithm, including the empty-list check:

def find\_highest\_score(scores):

    if not scores:

        return None

    highest \= scores\[0\]

    for index in range(1, len(scores)):

        if scores\[index\] \> highest:

            highest \= scores\[index\]

    return highest

result \= find\_highest\_score(\[72, 85, 68, 91, 85\])

if result is None:

    print("No scores available")

else:

    print("Highest score:", result)

**Expected output:** `Highest score: 91`

Here, `None` means that no maximum was found. We avoid returning `0` for an empty list because `0` could itself be a genuine score. `scores[0]` gets the first item; `range(1, len(scores))` lets the loop visit every later position. List indexing will be explored further in Unit II.

## 2.3 Complete the score-summary program and test other pass marks

**Worked example:** Use the list `[72, 85, 68, 91, 85]` and find the number of scores meeting two thresholds.

def count\_passing(scores, pass\_mark):

    total \= 0

    for score in scores:

        if score \>= pass\_mark:

            total \+= 1

    return total

scores \= \[72, 85, 68, 91, 85\]

for mark in \[60, 80\]:

    print("Pass mark:", mark,

          "\| Students meeting it:", count\_passing(scores, mark))

**Expected output:**

Pass mark: 60 \| Students meeting it: 5

Pass mark: 80 \| Students meeting it: 3

For a threshold of 60, all five scores qualify. For a threshold of 80, the qualifying scores are **85, 91, and 85**. The repeated 85 represents two students and must be counted twice.

**Reader action — Change one value:** Predict the count for a pass mark of `90`, then change the code and run it. Next, try an empty list (`scores = []`).

**Answer / hint:** At `90`, only `91` qualifies, so the count is **1**. For an empty list, the counting function returns **0**, because no scores meet the threshold. The highest-score function instead returns `None`, because an empty list has no maximum.

**Chapter 2 takeaway:** Variables store data, conditions make decisions, loops process collections, and functions turn clear algorithms into reusable Python programs.

---

# Chapter 3 — Measuring Algorithm Efficiency

**Starting problem:** *What changes when a class has 30 students instead of 3,000?*

A program can be correct but become inconveniently slow or memory-hungry as its input grows. **Algorithm efficiency** describes how much work and storage a method needs. In this chapter we focus on simple growth patterns rather than advanced mathematical proofs.

**Learning objective:** Estimate how processing time and extra memory change when the number of scores increases.

## 3.1 Count representative operations and distinguish runtime from growth

Let **n** mean the number of scores. In the Chapter 1 algorithm, the program starts with the first score and then compares each of the remaining scores to the current highest.

For a nonempty list, the number of `score > highest` comparisons is **n − 1**. The algorithm still visits all scores, so its total work grows approximately in proportion to **n**.

| Number of scores (`n`) | Comparisons after initialization (`n − 1`) |
| ----: | ----: |
| 5 | 4 |
| 30 | 29 |
| 50 | 49 |
| 3,000 | 2,999 |

Doubling the input from 5 to 10 does not require searching through every possible pair. It simply adds more scores to a single scan.

**Measured runtime** is the actual time a program takes on a particular computer, possibly expressed in milliseconds. It depends on hardware, Python's implementation, other running software, and input details. **Growth pattern**, by contrast, describes how the work scales as `n` increases. A single tiny timing measurement is not enough to establish a general growth rule.

When studying algorithms, it is useful to estimate the number of relevant steps before worrying about exact wall-clock time.

## 3.2 Recognize O(1), O(n), and O(n²) visually

**Big O notation** is a way to describe an upper bound on how resource requirements grow with input size. In beginner comparisons, it is commonly used to express the dominant growth pattern of an algorithm, usually for sufficiently large inputs.

| Notation | Simple meaning | Example |
| :---- | :---- | :---- |
| **O(1)** | Work does not increase with list length | Reading one known index, such as `scores[0]` |
| **O(n)** | Work grows approximately with the number of items | Finding the maximum by scanning all scores |
| **O(n²)** | Work may grow roughly with the square of the number of items | Comparing each score against every score in nested loops |

Illustrative examples (not benchmark measurements):

\# O(1) work: one indexed access, assuming scores is nonempty

first\_score \= scores\[0\]

\# O(n) work: one pass through all scores

for score in scores:

    print(score)

\# O(n^2) work: every score is paired with every score

for first in scores:

    for second in scores:

        print(first, second)

The nested-loop example prints `n × n` pairs; it is intended only to demonstrate a growth pattern, not to suggest a good score-processing solution. For five scores, it prints 25 pairs. For 50 scores, it prints 2,500 pairs.

**Conceptual growth comparison:**

| Input size `n` | Constant model | Linear model (`n`) | Quadratic model (`n²`) |
| ----: | ----: | ----: | ----: |
| 5 | 1 | 5 | 25 |
| 10 | 1 | 10 | 100 |
| 50 | 1 | 50 | 2,500 |
| 100 | 1 | 100 | 10,000 |

These are mathematical illustrations of growth, **not observed execution times**. An O(n²) routine may still be fast for a very small input, but its workload rises much faster as the input grows.

A fourth useful pattern is **O(log n)**, associated with repeatedly reducing the problem to a fraction of its current size. Binary search is a common example: for a sorted list, each comparison can eliminate roughly half the remaining search space. **We will trace binary search in Chapter 7**, rather than adding another algorithm here.

## 3.3 Compare keeping one maximum with copying a list: space complexity

**Space complexity** concerns memory use as an input grows. For clarity, we distinguish the space already occupied by the input from **additional (auxiliary) space** created by the algorithm.

Our maximum-scanning method maintains only a few variables, including `highest` and the current position. It does not need to create another list of all the scores. Its auxiliary storage is therefore **O(1)**: a fixed amount of additional space independent of `n`.

def highest\_without\_copy(scores):

    if not scores:

        return None

    highest \= scores\[0\]

    for index in range(1, len(scores)):

        if scores\[index\] \> highest:

            highest \= scores\[index\]

    return highest

This function uses **O(1) auxiliary space** and **O(n) time complexity**. Avoid using a list slice such as `scores[1:]` here if you want to preserve the O(1) auxiliary-space claim: in Python, slicing creates a separate list of the remaining elements.

Contrast that with deliberately copying every score:

def highest\_with\_copy(scores):

    if not scores:

        return None

    copied\_scores \= scores.copy()

    highest \= copied\_scores\[0\]

    for index in range(1, len(copied\_scores)):

        if copied\_scores\[index\] \> highest:

            highest \= copied\_scores\[index\]

    return highest

`copied_scores = scores.copy()` creates a new list containing all `n` references. The list copy uses **O(n) additional space**, even though it is not necessary to find the maximum.

| Method | Time complexity | Auxiliary space | Why |
| :---- | :---- | :---- | :---- |
| Scan by index, keep current maximum | O(n) | O(1) | One pass; only a few variables |
| Copy list, then scan | O(n) | O(n) | Extra list grows with input |

**Worked example:** If the class has **5** scores, scanning requires **4** comparisons after initialization; with **50** scores, it requires **49**. The number of comparisons increases roughly tenfold when the list size increases tenfold. The no-copy method still needs only one current-maximum variable, whereas a separate full list copy grows from 5 to 50 elements.

**Reader action — Predict before checking:** A class grows from 30 to 3,000 students. Approximately how does the number of comparisons change? Does the no-copy maximum finder need 100 times as much *additional* memory?

**Answer / hint:** The comparisons rise from **29 to 2,999** (roughly 100 times as many for large lists), so the time remains **O(n)**. The correctly implemented no-copy method uses **O(1)** auxiliary space, so its extra storage does **not** scale by a factor of 100\. Its input list itself is larger, but that is distinct from auxiliary space.

**Chapter 3 takeaway:** Efficiency helps us choose algorithms that scale: a single scan takes linear time, and careful implementation can find the maximum using constant extra space.

---

# Unit I — Review and Knowledge Check

Before continuing, check that you can answer the following questions without running the program:

1. In the problem “find the highest score,” what are the input and output?  
2. Why must the algorithm handle an empty list explicitly?  
3. What changes in our maximum trace if the final score becomes `95`?  
4. What does `if score >= pass_mark` mean in Python?  
5. How many students meet a pass mark of `80` in `[72, 85, 68, 91, 85]`?  
6. What is the difference between measured runtime and the growth of an algorithm?  
7. Why is a single scan O(n) but two nested full scans O(n²)?  
8. What is the difference between a program's input memory and auxiliary memory?

**Brief answer key:**

1. Input: a list of scores; output: its maximum or a no-scores response.  
2. An empty list has no first element and no maximum.  
3. The result changes to 95\.  
4. The score is greater than or equal to the pass mark.  
5. Three students.  
6. Runtime is an observed duration; growth describes how the workload changes with input size.  
7. One visits n items; the other can examine n² ordered pairs.  
8. Input memory holds the given data; auxiliary memory is extra storage the algorithm uses.

## Unit I Summary

This unit followed one continuous learning journey. **Chapter 1** showed how to describe a task as an algorithm and test its decisions. **Chapter 2** translated similar logic into a short Python program using lists, loops, conditions, and functions. **Chapter 3** introduced the idea that a correct algorithm also needs sensible time and space use, particularly when the list grows.

**Bridge to Unit II:** We can now describe, run, and evaluate a basic score-processing algorithm. Next we will explore how choices such as lists, stacks, queues, dictionaries, sets, trees, and graphs affect the ways information can be stored, found, and used.

---

## Notes for PentaByte Editors

- This detailed teaching draft expands **only** Unit I, Chapters 1–3, of the team's supplied focused outline; it is not a new 18-chapter outline.  
- Keep the same student-score example, heading numbers, and expected outputs when adapting the material into the study guide, PPT, and video demonstrations.  
- The code and answers in this unit are instructional examples rather than measured experiment results.  
- If adapting diagrams, explanations, or code from external resources later, add the required credits and citations in the final guide. Python language documentation: [https\://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/) .