# Chapter 2

## Essential Python for the Guide

In Chapter 1, you designed a method before choosing a language. Now you will turn those ideas into Python. Our running task is a small student-score report: calculate the average, find the highest score, and count how many scores reach an agreed pass mark.

<img width="512" height="184" alt="image" src="https://github.com/user-attachments/assets/bdfeacd8-6858-41c8-acab-46042cf20e44" />


Every topic adds a tool you will use in the final program. You will also learn to check what the program actually does, rather than trusting a result just because it looks plausible.

#### What you will learn

Run scripts and notebooks, and work with values, expressions, and input.

Control execution with conditions, loops, and reusable functions.

Use strings, lists, imports, and simple debugging checks.

Translate pseudocode into a tested score-processing program.

Build the foundations

Organize the work

Finish the program

### 2.1 Running Python

### 2.2 Variables And Types

### 2.3 Operators

### 2.4 Input And Output

### 2.5 Conditions

### 2.6 Loops

### 2.7 Functions And Scope

### 2.8 Strings And Lists

### 2.9 Imports

### 2.10 Debugging

### 2.11 Translation

### 2.12 Student Scores

How to study Predict each short example’s result, run it, then change one value. Python code uses straight quotation marks and consistent indentation. Code blocks are Python unless labeled Terminal, Pseudocode, or Output.

### 2.1 Running Python Scripts And Notebooks

Choose where your code runs

A Python interpreter executes Python instructions. Use a supported Python 3 installation or your course environment. In a terminal, python --version checks the interpreter selected by the python command. Some systems use python3; on Windows, py may also be available. Use the command that selects your intended Python 3 installation. [1]

#### Your first script

Save the following in a plain-text file named hello.py. Open a terminal in that file’s folder and run python hello.py, replacing python with your working interpreter command if necessary.

```python
name = "Su Ming"
print(f"Hello, {name}!")
```

**Output**

Hello, Su Ming!

A script runs from top to bottom when started. Saving an edit does not rerun it: run the file again. Terminal commands belong in the terminal, not inside the .py file. If you are at a >>> prompt, you are already in the interactive Python interpreter.

#### Working in a notebook

A notebook (.ipynb) mixes code cells with explanatory Markdown cells. Its kernel is the running process that remembers variables between executions. Run a cell with Shift+Enter. A later cell can use variables created by an earlier executed cell. [2]

# Cell 1

```python
scores = [72, 85, 59]

```

# Cell 2

```python
print(sum(scores))  # 216
```

Cell position is not execution order. If you edit Cell 1 without running it, Cell 2 still sees the old values. Before sharing a notebook, restart its kernel and run all cells from top to bottom. This checks for hidden dependencies on previous work.

If you need a local notebook installation, the optional terminal commands below install and launch it in your selected Python environment. The chapter’s .py program does not need Jupyter. [2]

**Terminal**

python -m pip install notebook

python -m notebook

### 2.2 Variables Assignment And Basic Data Types

#### Give meaningful names to values

A variable name refers to a value. Assignment evaluates the right-hand expression and binds the name on the left to its result. It does not declare an equation that must remain true forever.

```python
score = 72
score = score + 5
print(score)  # 77

```

<img width="512" height="209" alt="image" src="https://github.com/user-attachments/assets/138716b8-c69d-4039-b721-c367babe1c46" />


**Type**

Example

Typical role

int

Whole-number count or score

float

72.5

Measurement or average

str

"Su Ming"

Text

bool

True or False

A condition’s result

list

[72, 85, 59]

An ordered, changeable collection

NoneType

None

No result available

The value 72 and the text "72" have different types. type(72) reports int; type("72") reports str. Python tracks types at runtime, so the same name can later refer to another type. Clear programs avoid unnecessary type changes because they make reasoning harder.

#### Choose names that explain their role

Use score, total, and pass_count rather than unexplained single letters. Names are case-sensitive: score and Score are different. A name cannot begin with a digit or use a keyword such as for. Use underscores for multiple words, and avoid hiding built-in names such as list or sum.

> **Predict After a = 10; b = a; a = 20, b is still 10. Assigning the number to b does not create a permanent connection between the two names. Shared mutable lists behave differently; Section 2.8 shows why.**

### 2.3 Operators Expressions And Type Conversion

#### Calculate with the right kinds of values

An expression combines values and operations to produce a result. For our report, total / count computes an average. Choose operators deliberately: ordinary division and floor division answer different questions.

**Operator**

Example

Result or meaning

+  -  *

8 + 3; 8 - 3; 8 * 3

11; 5; 24

/

7 / 2

3.5

//

7 // 2

3, the floor of the quotient

%

7 % 2

1, the remainder

**

2 ** 3

8, exponentiation

==  !=

72 == 72; 72 != 72

True; False

<  <=  >  >=

score >= 60

Compare values

Multiplication and division bind more tightly than addition and subtraction. Parentheses make the intended grouping explicit: (72 + 85 + 59) / 3 is 72.0, while 72 + 85 + 59 / 3 is a different calculation. Floor division rounds downward: -7 // 2 is -4, not -3.

#### Convert when the meaning requires it

```python
text = "85"
score = int(text)
average = float("75.5")
label = str(score)
print(score + 5)     # 90
print(label + "5")  # 855
```

int("85") creates an integer. int("85.5") raises ValueError because the string is not an integer literal. int(85.9) gives 85 by truncating toward zero; it does not round to the nearest integer. Converting text and validating its allowed range are separate tasks.

Floating-point values approximate many decimal fractions. For example, 0.1 + 0.2 may display as 0.30000000000000004. Format output for readers and use an appropriate tolerance for numerical checks. Do not assume every decimal calculation is exact.

> **Remember An assignment uses =. A comparison uses ==. Confusing the two is a common source of errors.**

### 2.4 Input Output And Formatted Results

#### Turn user text into a readable result

input displays a prompt and returns text. Even when a person types digits, conversion is needed before arithmetic. print displays values; an f-string inserts expression results into a text template. [3]

```python
name = input("Student name: ").strip()
score = float(input("Score: "))
print(f"{name}: {score:.1f}/100")
```

If the user enters Su Ming and then 85, the displayed result is Su Ming: 85.0/100. strip removes surrounding whitespace from the name. The .1f format displays one digit after the decimal point; it changes the display, not the stored value.

#### Separate conversion from validation

```python
try:
    score = float(input("Score from 0 to 100: "))
    if 0 <= score <= 100:
        print(f"Accepted: {score:.1f}")
    else:
        print("Score must be from 0 to 100.")
except ValueError:
    print("Please enter a number, such as 85.")
```

try marks an operation that may fail. If conversion raises ValueError, the except block gives a useful message. Entering 120 converts successfully but fails the range check. This version asks once; a retry loop could be added later. Exception handling is explored in Section 2.10.

#### Format the report consistently

```python
average = 75.0
passed = 4
count = 5
print(f"Average: {average:.2f}")
print(f"Passed: {passed}/{count}")
print(f"Pass rate: {passed / count:.1%}")
```

**Output**

Average: 75.00

Passed: 4/5

Pass rate: 80.0%

The percentage format multiplies a fraction by 100 for display. Pass 4 / 5 to .1%, not 80; otherwise the displayed percentage would be 8000.0%. Always make sure count is nonzero before dividing.

### 2.5 Conditional Statements And Boolean Logic

#### Choose a path from a condition

An if statement runs a block only when its condition is true. elif adds another condition and else handles the remaining case. In one if/elif/else chain, Python executes the first matching branch, so order matters. [4]

```python
score = 85
if score >= 90:
    result = "Excellent"
elif score >= 60:
    result = "Pass"
else:
    result = "Below pass mark"
print(result)  # Pass
```

These labels are illustrative. If the >= 60 branch came first, a score of 95 would match it before reaching the excellence check. Independent if statements are different: more than one can run.

#### Combine conditions

**Expression**

When it is true

Example

A and B

Both conditions are true.

score >= 60 and submitted

A or B

At least one condition is true.

late or missing

not A

A is false.

not submitted

```python
score = 85
submitted = True
passed = score >= 60 and submitted
valid = 0 <= score <= 100
print(passed, valid)  # True True
```

and and or short-circuit: the second expression is evaluated only when needed. For example, count > 0 and total / count >= 60 avoids division when count is zero. With Boolean operands their results are Boolean; more generally, Python’s and and or return one of their operands.

#### Indentation is part of the meaning

Put a colon after a condition and indent its block consistently, conventionally with four spaces. Lines at the same indentation belong to the same block. Do not mix tabs and spaces. A line moved outside the block may run even when the condition is false.

> **Quick check Which branch handles exactly 60? Which handles exactly 90? Test the boundaries before trying many random values.**

### 2.6 Loops With For While And Range

#### Repeat without copying instructions

Use a for loop to visit items in a collection. The loop variable takes one item at a time. An accumulator, such as total, stores a result that grows as the loop runs.

```python
scores = [72, 85, 59]
total = 0
for score in scores:
```

total += score

```python
print(total)  # 216
```

total += score means total = total + score here. Initialize total before the loop. Resetting it to zero inside the loop would discard earlier work.

**Iteration**

Current score

Total before

Total after

#### Use range for a sequence of integers

```python
print(list(range(4)))        # [0, 1, 2, 3]
print(list(range(1, 5)))     # [1, 2, 3, 4]
print(list(range(0, 6, 2)))  # [0, 2, 4]
```

range(start, stop, step) excludes stop. Its defaults are start = 0 and step = 1; step cannot be zero. range does not build a full list of integers. Here list(...) is used only to display the values together.

#### Use while when repetition depends on a condition

```python
attempts = 0
while attempts < 3:
```

attempts += 1

```python
    print(f"Attempt {attempts}")
```

This prints attempts 1, 2, and 3, then stops. A while condition is tested before each iteration; it may be false immediately. A missing update can create an infinite loop. break exits the nearest loop early, while continue skips to its next iteration.

> **Boundary case A for loop over [] runs zero times. That behavior is useful, but it does not automatically make later operations such as division by len(scores) safe.**

### 2.7 Functions Parameters And Return Values

#### Give one task a reusable name

A function groups a task behind a name. Parameters are the names listed in its definition. Arguments are the actual values supplied in a call. Defining a function does not run its body; calling it does.

```python
def is_pass(score, pass_mark=60):
    return score >= pass_mark

print(is_pass(59))      # False
print(is_pass(60))      # True
print(is_pass(65, 70))  # False
```

score and pass_mark are parameters. In is_pass(65, 70), the arguments are 65 and 70. The default pass_mark of 60 is used only when the caller omits that argument. Naming the parameter in a call, is_pass(65, pass_mark=70), can make its purpose clearer.

#### Return a result that another step can use

```python
def mean_score(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

result = mean_score([72, 85, 59])
print(result)  # 72.0
```

sum adds the items, and len counts them. return immediately leaves the function. Returning None for empty input is a design choice: the caller must handle “no average” before formatting it as a number.

print displays a value but does not return that value to the caller. A function that reaches its end without a return statement returns None. Keep calculations separate from presentation so the same result can be printed, tested, or used in another calculation.

#### Returning several related results

```python
def endpoints(values):
    return values[0], values[-1]

first, last = endpoints([72, 85, 59])
print(first, last)  # 72 59
```

The comma-separated values form a tuple, an ordered collection whose elements cannot be replaced in place. The assignment unpacks two results into two names. endpoints assumes a non-empty collection; its contract is different from mean_score.

### 2.7 Scope And Function Design

#### Know which names a function owns

Scope determines where a name can be used. Parameters and names assigned inside a function are normally local to that function call. A local score can have the same spelling as a caller’s score without being the same variable binding.

```python
def add_bonus(score, bonus):
    score = score + bonus
    return score

score = 72
adjusted = add_bonus(score, 5)
print(score, adjusted)  # 72 77

```

<img width="512" height="209" alt="image" src="https://github.com/user-attachments/assets/94e162af-d156-44d0-92d6-e9b1ae8a15d6" />


The local assignment does not reassign the caller’s score. The caller receives 77 and binds adjusted to it. To replace the caller’s score, write score = add_bonus(score, 5).

#### Use explicit inputs instead of hidden dependencies

A function can read a module-level name if no local name hides it, but that can make its behavior depend on unseen state. Prefer passing a threshold as a parameter and returning a result. Avoid global updates while learning; they make tracing several function calls harder.

#### A local name does not make every object private

A parameter may refer to a mutable object supplied by the caller. If a function performs values.append(100), it changes that shared list. Rebinding the parameter, as in values = [], is different: it changes the local name. Section 2.8 illustrates sharing and copying.

> **Design habit Design a function around a clear task and state its assumptions. A helpful comment explains a decision, such as why empty input returns None, rather than repeating every visible line.**

### 2.8 Strings Indexing And Slicing

#### Select the characters you need

A string is an ordered sequence of text characters. Indexing selects one position. Python starts at zero; negative indices count from the end. The same basic indexing notation also works with lists.

```python
text = "PYTHON"
print(text[0])    # P
print(text[-1])   # N
print(text[1:4])  # YTH

```

<img width="512" height="181" alt="image" src="https://github.com/user-attachments/assets/2bcd8665-0265-4ee3-a95d-76ca95f52fc2" />


#### Read a slice as a range of positions

**Expression**

Result

Interpretation

text[:3]

"PYT"

From the beginning, before index 3

text[3:]

"HON"

From index 3 to the end

text[::2]

"PTO"

Every second character

text[::-1]

"NOHTYP"

Reverse order

text[2:2]

""

An empty slice

Indexing outside the valid positions raises IndexError: text[6] is invalid here. A slice with a large stop, such as text[:99], is clipped to the available length. This difference is useful when selecting a prefix of text.

#### Strings cannot be edited in place

```python
name = "  Su Ming  "
clean_name = name.strip()
print(clean_name.upper())  # SU MING
print("Ming" in clean_name)  # True
```

Methods such as strip and upper return strings; they do not modify the original string. text[0] = "J" is invalid because strings are immutable. Use a new expression, such as "J" + text[1:], to create a changed value.

### 2.8 Basic List Operations

#### Change a collection deliberately

A list is ordered and mutable: you can replace, add, or remove elements. We will use numeric lists for scores so that each item has the same role. [5]

```python
scores = [72, 85, 59]
```

scores[0] = 75

scores.append(91)

```python
removed = scores.pop()
print(scores, removed)  # [75, 85, 59] 91
```

Operation

Purpose

Important detail

len(scores)

Count the elements.

Empty lists have length 0.

scores.append(91)

Add one value at the end.

Changes the list; returns None.

scores.extend([68, 80])

Add several values.

Adds each item separately.

scores.remove(59)

Remove the first matching value.

Raises ValueError if absent.

scores[1:3]

Select a slice.

Creates a new list.

59 in scores

Check membership.

Returns True or False.

#### Assignment does not copy a list

```python
scores = [72, 85, 59]
alias = scores
copy_scores = scores.copy()
```

alias[0] = 90

```python
print(scores)       # [90, 85, 59]
print(copy_scores)  # [72, 85, 59]

```

<img width="512" height="181" alt="image" src="https://github.com/user-attachments/assets/e4157f6e-cd39-4f0d-b779-b823d48e2972" />


copy is shallow: nested mutable items would still be shared. For our flat list of numbers, it is enough to separate element replacements. Avoid adding or removing items from a list while looping over that same list; build a new list instead.

### 2.9 Imports And Standard Library Modules

#### Use tools that Python already provides

A module organizes reusable definitions. import makes a module available by name. Python’s standard library ships with Python; external packages are installed separately. Our final score program uses only the standard library. [6]

```python
import math
import statistics

print(math.sqrt(81))  # 9.0
print(statistics.mean([72, 85, 59]))  # 72
```

The dot connects a module name to a function inside it. You can also write from math import sqrt and call sqrt(81), but retaining math.sqrt makes the source visible. Avoid import * in beginner projects because it hides where names come from.

**Module**

Useful tool

Example use

math

sqrt, isclose, isfinite

Numeric calculations and checks

statistics

mean, median

Small data summaries

random

Random, randint

Generating practice data

pathlib

Path

Working with file paths

```python
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
print(math.isfinite(75.0))           # True
print(math.isfinite(float("nan")))  # False
```

isclose compares with a tolerance. isfinite rejects infinity and NaN, a special “not a number” value. These checks serve different purposes: a number can be finite yet outside the allowed score range of 0 to 100.

#### Make files safe to import

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Su Ming"))
```

The guarded block runs when the file is executed directly. It is skipped when another file imports it, so examples do not run unexpectedly during reuse. Avoid naming your own file math.py or statistics.py: it can hide the module you meant to import.

### 2.10 Errors And Debugging

#### Use an error as evidence

Debugging means finding the cause of unexpected behavior. A syntax error prevents Python from parsing the code. An exception occurs during execution. A logic error can produce the wrong result without raising an exception. [7]

**Problem**

Small example

First thing to check

SyntaxError

```python
if score >= 60
```

Missing colon or unmatched punctuation

NameError

```python
print(scroe)
```

Spelling and whether a name was assigned

TypeError

"85" + 5

Text used where a number was intended

ValueError

int("eighty")

Input cannot be converted as requested

IndexError

[][0]

Empty collection or invalid position

ZeroDivisionError

total / 0

Empty input or a bad denominator

#### Read the last line then locate the cause

A traceback usually ends with an exception type and a message. Find the referenced line in your code and inspect the values involved. The indicated location is where the problem became visible; the cause may be an earlier assignment.

```python
scores = [72, 85, 59]
total = 0
for score in scores:
    total = score  # Logic bug: earlier values are lost.
print(total)       # 59, but the intended sum is 216.
```

Trace total: it becomes 72, then 85, then 59. The repair is total += score. A print placed inside the loop, such as print(score, total), would expose the replacement at each step.

#### A small debugging routine

Reproduce the problem with the smallest input that still fails.

Write the expected result before changing the code.

Inspect types and values at the point where behavior diverges.

Fix the cause, then rerun both the failing case and a normal case.

Avoid hiding the evidence Catch the exception you expect, such as ValueError from numeric conversion. A blanket except can hide unrelated programming mistakes and make the program appear to succeed.

### 2.10 Simple Assertions

#### Turn expectations into executable checks

An assertion states something that should be true at that point in the program. If the expression is false, Python raises AssertionError. Passing assertions normally print nothing. Use them for development checks and small examples.

```python
def is_pass(score, pass_mark=60):
    return score >= pass_mark

assert is_pass(60) is True
assert is_pass(59) is False
assert is_pass(70, pass_mark=70) is True
```

The is operator checks identity. is None is the standard way to check for the special None marker; use == for ordinary value comparisons such as scores == [72, 85]. Do not use is to compare numeric values.

#### Check boundaries and preserve precision

```python
import math

def mean_score(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

assert mean_score([]) is None
assert mean_score([80]) == 80
assert math.isclose(mean_score([72, 85, 59]), 72.0)
```

For floating-point results, choose a tolerance suited to the task. math.isclose has defaults, but comparisons near zero may need an explicit abs_tol. Formatting to two decimal places is a display choice, not a complete numerical testing strategy.

#### Validation must remain active

Assertions can be disabled when Python runs with optimization. Do not use assert as the only check on user input. An explicit condition followed by raise ValueError remains part of normal program behavior. [8]

```python
def validate_score(score):
    if not math.isfinite(score) or not 0 <= score <= 100:
```

raise ValueError("Score must be finite and 0 to 100.")

```python
    return score
```

This helper assumes a numeric argument. It rejects non-finite or out-of-range numbers. Converting user text is a separate step, as shown in Section 2.4. A message should tell the caller what rule was broken.

### 2.11 Translating Pseudocode

#### Preserve the decisions when syntax changes

Translation is easier when you map each pseudocode operation to its Python equivalent. Keep the input contract, starting values, loop boundary, and return behavior the same. Then test the Python version with an example you can trace by hand.

**Pseudocode**

ALGORITHM CountPasses(scores, pass_mark)

passed ← 0

FOR EACH score IN scores DO

IF score >= pass_mark THEN

passed ← passed + 1

END IF

END FOR

RETURN passed

**Python**

```python
def count_passes(scores, pass_mark=60):
    passed = 0
    for score in scores:
        if score >= pass_mark:
```

passed += 1

```python
    return passed

assert count_passes([72, 85, 59, 91, 68]) == 4
assert count_passes([]) == 0
```

**Pseudocode feature**

Python translation

Assignment arrow

Use =, or += for this numeric update.

THEN and DO

Use a colon after the condition or loop header.

END IF and END FOR

Indentation marks the block boundaries.

RETURN after the loop

Align return with the for statement, not its body.

Moving return inside the loop stops after the first score. Moving passed = 0 inside the loop erases earlier passes. Both mistakes can be syntactically valid, which is why a trace and boundary checks matter.

> **Contract The function assumes valid numeric scores and a valid numeric threshold. Its job is counting; the complete report will add range and finiteness validation.**

### 2.12 Processing Student Scores

#### Define the report before writing it

Your team has five fictional scores: [72, 85, 59, 91, 68]. The report should show the number of scores, average, highest score, pass count, and pass rate. This is an equal-weight summary, not a GPA or credit-weighted calculation.

**Decision**

Our chosen behavior

Input

A finite Python list of int or float scores; no text, Boolean values, or nested collections.

Valid score

A finite number from 0 to 100, inclusive.

Pass mark

A numeric, finite threshold from 0 to 100; default 60.

Empty list

Return None; display “No scores available.”

Invalid numeric value

Raise ValueError; do not silently drop it.

**Output**

Return average, highest score, and pass count as a tuple. The display code adds count and pass rate.

Input preservation

Read the list without changing its values or order.

<img width="512" height="237" alt="image" src="https://github.com/user-attachments/assets/69c830ea-23fe-4326-9edb-5e83db6d2ab1" />


#### Plan the variables

total accumulates scores. highest keeps the largest value seen so far. passed counts values at or above the threshold. The list length provides count. At the end, average is total / count, and pass rate is passed / count.

> **Scope of validation The input contract requires numeric types; this beginner function does not implement a complete type-validation layer. It does check finiteness and range. An input interface should convert text and reject unsupported types before calling it.**

### 2.12 The Calculation Function

#### Build the summary one score at a time

```python
import math

def summarize_scores(scores, pass_mark=60):
    if not math.isfinite(pass_mark) or not 0 <= pass_mark <= 100:
```

raise ValueError("Pass mark must be finite and 0 to 100.")

```python
    if len(scores) == 0:
        return None

    total = 0.0
    highest = scores[0]
    passed = 0
    for score in scores:
        if not math.isfinite(score) or not 0 <= score <= 100:
```

raise ValueError("Score must be finite and 0 to 100.")

total += score

```python
        if score > highest:
            highest = score
        if score >= pass_mark:
```

passed += 1

```python
    average = total / len(scores)
    return average, highest, passed
```

#### Read the decisions in order

First validate the threshold, even if the list is empty. Then handle the empty case before reading scores[0]. Initializing highest from a real input value follows the maximum-finding method in Chapter 1.

Each iteration checks a score before adding it to total or counting it as a pass. The two if statements are independent: a score can be both a new maximum and a pass. An elif would incorrectly make those actions mutually exclusive.

The loop visits all scores once. The first score is included in total and passed, even though it already initialized highest. Its comparison with itself is harmless. The function returns data and leaves the presentation to its caller.

> **Cost preview The function uses O(n) time and O(1) auxiliary space under the usual fixed-cost numeric-operation model. It does not sort, copy, or mutate the input list. Complexity will receive a fuller treatment in Chapter 3.**

### 2.12 Reporting And Checking The Result

#### Make the output useful to a reader

```python
scores = [72, 85, 59, 91, 68]
```

summary = summarize_scores(scores)

```python
if summary is None:
    print("No scores available.")
else:
```

average, highest, passed = summary

```python
    count = len(scores)
    print(f"Students: {count}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest:g}")
    print(f"Passed: {passed}/{count}")
    print(f"Pass rate: {passed / count:.1%}")
```

**Output**

Students: 5

Average: 75.00

Highest: 91

Passed: 4/5

Pass rate: 80.0%

The tuple is unpacked only when summary is not None. The :g format gives a compact numeric display for the highest score. The percentage format uses the fraction passed / count.

**Score processed**

Total

Highest

Passed

Check the arithmetic: 375 / 5 gives 75, and 4 / 5 gives 0.8. The score 59 contributes to the average even though it does not pass. Filtering it out would answer a different question.

Runnable companion The companion chapter_2_student_scores.py combines the calculation and report, with a small demonstration inside a main guard. Run it as a script, or import summarize_scores into another exercise.

## Practice

#### Use the concepts without copying the answer

Try the prediction questions before running Python. For design questions, state the behavior on an empty input. Answer guidance follows on the next page.

#### Predict

1. What are the values and types of a, b, and c after a = "8"; b = int(a) + 2; c = b / 4?

2. What do 9 // 2, 9 % 2, and 2 ** 4 produce? What changes if you use 9 / 2?

3. For text = "PYTHON", predict text[-2], text[:2], and text[2:5].

4. What values does range(2, 8, 2) visit? How many iterations occur?

#### Trace and repair

5. Trace a pass counter for [60, 59, 100] using a pass mark of 60. Write the count after each iteration.

6. A function contains print(total / count) but no return statement. Why does answer = that_function(...) assign None? How would you change its design?

7. Given a = [10, 20]; b = a; b.append(30), what is a? Change the assignment so appending to b does not change this flat list a.

8. A notebook works only after you execute its third cell before its first cell. What should you fix before sharing it?

#### Write and test

9. Write a function count_below(scores, limit=60) that returns the number of values strictly below limit. Test [60, 59, 100], [], and [0].

10. Modify the report to include the lowest score. Keep input unchanged and preserve the current empty-input behavior. Explain where the new variable is initialized and updated.

11. Predict the full report for [60, 60, 100] with pass_mark=60. Then predict the pass count with pass_mark=70.

12. Name the expected behavior for each: [], [0, 100], [101], [float("nan")], and a pass mark of -1. Which cases should return None, return a summary, or raise ValueError?

#### Optional challenge

Add a text-input interface that asks for one score at a time and stops when the user types done. Convert and validate each score before appending it. Keep input collection separate from summarize_scores, so the calculation can still be tested without typing.

## Answer Guidance

#### Check both results and reasons

1. a is "8", a str; b is 10, an int; c is 2.5, a float. Converting a does not change a itself.

2. The results are 4, 1, and 16. Ordinary division gives 4.5.

3. The results are "O", "PY", and "THO". The stop index is excluded in each slice.

4. The values are 2, 4, and 6, giving three iterations. The stop value 8 is excluded.

5. The count starts at 0, then becomes 1, 1, and 2. A score of exactly 60 passes.

6. print displays the average; the function then returns None implicitly. Return the average from the function and let the caller print it. Also handle count = 0.

7. a becomes [10, 20, 30] because b refers to the same list. Use b = a.copy() before appending. A shallow copy is sufficient for this flat numeric list.

8. Move setup and definitions before the cells that use them. Restart the kernel and run all cells from top to bottom to verify reproducible execution.

```python
def count_below(scores, limit=60):
    count = 0
    for score in scores:
        if score < limit:
```

count += 1

```python
    return count

assert count_below([60, 59, 100]) == 1
assert count_below([]) == 0
assert count_below([0]) == 1
```

9. The code above counts only values strictly below the limit. It assumes valid numeric inputs, as specified in the exercise.

10. After the empty check, initialize lowest = scores[0]. Inside the loop, update it when score < lowest. Add it to the returned tuple and update the caller’s unpacking and display together.

11. Students: 3; Average: 73.33; Highest: 100; Passed: 3/3; Pass rate: 100.0%. With a threshold of 70, only one score passes. Use the unrounded average in later calculations.

12. With a valid default threshold: [] returns None; [0, 100] gives average 50.0, highest 100, and one pass. [101] and [float("nan")] raise ValueError. A threshold of -1 also raises ValueError, even for an empty list, because threshold validation happens first.

## Review And Further Reading

#### Keep these habits as programs grow

#### A compact Python reminder

**Need**

Pattern

Watch for

Assign or compare

x = 3; x == 3

Assignment and comparison differ.

Format a number

f"{average:.2f}"

Formats display, not stored precision.

Visit all items

```python
for score in scores:
```

Indent the repeated work.

Return a result

```python
return average
```

print is for display.

Select a slice

values[start:stop]

The stop position is excluded.

Copy a flat list

copy_values = values.copy()

Assignment alone shares the list.

Check no result

result is None

Do not format None as a number.

Validate input

```python
if invalid: raise ValueError(...)
```

Do not rely only on assert.

You are ready for the next chapter when you can run a clean script, explain how its variables change, and test its boundary cases. If a result surprises you, reduce the input and trace it. Small, reproducible examples are easier to reason about than a large program full of guesses.

## Official References

[1] Python Software Foundation. Using Python on Windows. https://docs.python.org/3/using/windows.html
[2] Project Jupyter. Notebook guide and installation. https://jupyter-notebook.readthedocs.io/en/stable/notebook.html ; https://jupyter.org/install
[3] Python Tutorial. Input and Output. https://docs.python.org/3/tutorial/inputoutput.html
[4] Python Tutorial. More Control Flow Tools. https://docs.python.org/3/tutorial/controlflow.html
[5] Python Tutorial. Data Structures. https://docs.python.org/3/tutorial/datastructures.html
[6] Python Tutorial. Modules. https://docs.python.org/3/tutorial/modules.html
[7] Python Tutorial. Errors and Exceptions. https://docs.python.org/3/tutorial/errors.html
[8] Python Language Reference. The assert statement. https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
Additional reference: Python Tutorial, An Informal Introduction to Python; math module reference. https://docs.python.org/3/tutorial/introduction.html ; https://docs.python.org/3/library/math.html

Scores and grading labels are fictional teaching examples. This chapter and its original diagrams were prepared with AI assistance. The examples use Python 3 and standard-library tools; references were checked in October 2026.
