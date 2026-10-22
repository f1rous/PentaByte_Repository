# Chapter 1: From Problems to Algorithms

*An illustrated introduction to computational thinking*

This chapter introduces computational thinking through a battery-charge example. It moves from defining a problem to modeling it, writing an algorithm, tracing its execution, and testing a Python implementation.

Your student robotics team has five batteries. Before a demonstration, you need the one with the highest charge. Looking at five readings is easy. But what if there are five thousand, the values arrive in a different order, or the list is empty?

![Figure 1.1: Five fictional battery charge readings](assets/images/figure-1.png)

**Figure 1.1  Our running example uses five fictional battery readings.**

This chapter shows how to turn that everyday decision into a precise, testable solution. You will move from a problem statement to a model, then to pseudocode, a trace, and a small Python program. The same approach will support the algorithms and AI systems you study later.

## Learning Objectives

* Define what a solution receives, what it must produce, and which rules it must follow.
* Use sequence, selection, and repetition to express a method clearly.
* Read a flowchart and trace how variables change.
* Explain why a maximum-finding algorithm works and when it stops.

## Chapter Roadmap

| Understand the task | Express the method | Check the result |
| --- | --- | --- |
| 1.1 Computational thinking<br>1.2 Problem definition<br>1.3 Modeling | 1.4 Algorithms and programs<br>1.5 Control structures<br>1.6 Pseudocode<br>1.7 Flowcharts | 1.8 Tracing<br>1.9 Correctness and edge cases<br>1.10 Finding the largest value |

**Before you begin** No prior Python knowledge is required. Read the plain-language reasoning first; the Python example near the end is a preview, with its syntax explained.

## 1.1 Computational Thinking

### Break the problem into useful pieces

Computational thinking means formulating a problem so that a clear process can solve it. It begins before you write code. Three useful habits are decomposition, pattern recognition, and abstraction. They work together, and you may return to them as your understanding improves. [1]

#### Decomposition

Break a task into smaller tasks with clear responsibilities. For the battery problem, separate reading the data, comparing the values, and reporting the result. If a reading is missing, you can investigate the input stage without rewriting the comparison method.

![Figure 1.2: Decomposition of a problem into smaller responsibilities](assets/images/figure-2.png)

**Figure 1.2  Decomposition separates the responsibilities of a solution.**

#### Pattern recognition

Look for a repeated structure. After choosing a temporary best value, every new battery asks the same question: is its charge higher than the best seen so far? That repeated comparison suggests a loop. The same pattern also appears when finding the highest score or the longest measured part.

#### Abstraction

Keep the information needed for the question and leave other details out of the model. To find only the highest charge, battery color and purchase date do not matter. If the task asks which battery to collect, however, its ID matters too. A detail is relevant because of the required output, not because it is interesting.

These are thinking tools, not a rigid three-step recipe. A useful abstraction may reveal a repeated pattern; testing may show that a task needs to be split differently.

**Pause and think** You are choosing the shortest queue at a canteen. What would you measure, and which details could you ignore? Think about whether “fewest people” always means “shortest waiting time.”

## 1.2 Defining a Problem

### Say exactly what success means

“Choose the best battery” sounds clear until two people interpret “best” differently. One might choose the highest charge; another might prefer the newest battery. A problem specification removes this uncertainty before the algorithm is designed.

| Part of the specification | Battery example |
| :---- | :---- |
| Input | A finite list of numeric charge readings, each from 0 to 100 percent. |
| Output | The highest charge value; if the list is empty, report that no readings are available. |
| Assumptions | Readings use the same scale, are valid, and do not change during this calculation. |
| Constraints | Do not modify the input list. Examine readings in their given order. Return one maximum value, even if it occurs more than once. |

#### Assumptions and constraints do different jobs

An assumption is something the solution relies on. A constraint is a requirement that restricts acceptable solutions. If a real sensor may send text or a missing value, the valid-number assumption is unsafe unless an earlier stage validates the data. Validation can be added, but it should be stated as part of the design.

#### Make the output precise

For [42, 76, 58, 91, 67], the required output is 91. It is not the fourth position, the ID “D,” or a sorted list. Those are different outputs and would require a different specification. In Python, the fourth element has index 3 because indexing starts at zero.

For [91, 91, 67], the maximum value is still 91. No tie-breaking rule is needed unless the output must identify a particular battery.

#### Write one sentence you can test

Given a finite list of valid charge readings, return a value that occurs in the list and is at least as large as every reading; for an empty list, report that no maximum is available.

**Design habit** A requirement such as “the program should be fast” is too vague to test. A useful requirement would specify the input size and an allowed response time, or require a single pass through the data.

## 1.3 Modeling a Real-World Problem

### Represent only what the task needs

A model is a simplified representation of a situation. Computers cannot directly reason about a battery on a table; they operate on a representation, such as a number and an identifier. A useful model preserves the information needed to answer the question.

![Figure 1.3: Representing a real-world collection as data](assets/images/figure-3.png)

**Figure 1.3  A physical collection becomes data that a method can process.**

| Question | Suitable representation | Possible output |
| :---- | :---- | :---- |
| What is the highest charge? | [42, 76, 58, 91, 67] | 91 |
| Which battery has it? | [("A", 42), ("B", 76), ("C", 58), ("D", 91), ("E", 67)] | ("D", 91) |

#### Check the model against reality

Charge percentage is enough for our defined task. It is not enough to decide which battery will run a robot longest. Capacity, battery condition, and the robot’s power demand can change that answer. An algorithm can be correct for a model while the model is unsuitable for the real decision.

For this chapter, we deliberately solve the narrower problem: find the highest reported charge. We assume all readings are valid and comparable. This keeps the focus on the method rather than battery engineering.

#### Choose a representation you can work with

A list is an ordered collection. Its order tells us which value to inspect first, second, and so on; it does not mean the values are sorted. We can scan the list without rearranging it. Later chapters will compare other ways of organizing data.

**Try it** If the output changes from “highest charge” to “all batteries below 20 percent,” what information must remain in the model so a team member can locate those batteries?

## 1.4 Algorithms and Programs

### Separate the method from its implementation

An algorithm is a precise method for solving a defined problem. In this chapter, our algorithms describe steps that finish after a finite amount of work for each valid input. A program expresses such a method in a programming language so that a computer can execute it.

#### One method in two forms

| Algorithm in ordinary language | Python implementation |
| :---- | :---- |
| Start with the first reading as the best value. | best = values[0] |
| Visit each later reading in order. | for i in range(1, len(values)): |
| If it is higher than the best, replace the best. | `if values[i] > best:`<br>`best = values[i]` |
| Give back the best value. | return best |

This comparison assumes a non-empty list. The complete version in Section 1.10 checks the empty case before reading the first element. You do not need to memorize the Python syntax yet; notice that both columns describe the same decisions.

#### Why the distinction matters

The method could be implemented in Python, C, or another language. The punctuation and syntax would change, but the idea of keeping the largest value seen so far would remain. A single program may also contain many algorithms, alongside user-interface code and file handling.

A syntax error breaks the rules of the language, such as a missing colon in Python. A logic error can occur in code that runs: using “less than” instead of “greater than” would keep the smallest value. Clear reasoning is still necessary after the program becomes executable.

#### Design before debugging

First explain the method on paper. Then check a small example. Only after the steps make sense should you translate them into code. If the result is wrong, ask whether the specification, the method, or the implementation caused the problem.

**Remember** A computer carries out the instructions you give it. It does not infer an unstated intention such as “ignore invalid readings” or “choose the safest battery.”

## 1.5 Sequence, Selection, and Repetition

### Control the order of the work

Many introductory algorithms can be built from three control structures. Sequence determines what happens next, selection chooses between actions, and repetition performs a group of actions more than once.

![Figure 1.4: Sequence, selection, and repetition control structures](assets/images/figure-4.png)

**Figure 1.4  The arrows show order, branching, and a return to a loop condition.**

#### Sequence follows an order

Read a charge value, compare it with a threshold, then display a result. Order matters: a comparison cannot use a value that has not yet been read or assigned.

#### Selection makes a decision

A condition has a true or false result. If a battery has at least 80 percent charge, label it “ready”; otherwise label it “charge first.” Exactly 80 qualifies because “at least” includes the boundary.

```text
IF charge >= 80 THEN
    OUTPUT "Ready"
ELSE
    OUTPUT "Charge first"
END IF
```

#### Repetition handles a collection

To inspect five batteries, repeat the same action for each reading. A FOR EACH loop is convenient when working through a collection. A WHILE loop repeats while a condition remains true, so its body must make progress toward stopping when termination is required.

These structures can be nested. Finding the largest reading uses sequence to initialize the candidate, a loop to visit later readings, and a selection inside the loop to decide whether the candidate should change.

## 1.6 Writing Clear Pseudocode

### Make the logic readable before coding

Pseudocode describes an algorithm using structured, language-independent instructions. It is written for people, so there is no single universal syntax. Its value comes from consistent notation and enough precision that another reader can implement the same method.

#### Conventions used in this chapter

| Notation | Meaning | Example |
| :---- | :---- | :---- |
| ← | Assign a new value to a variable. | count ← 0 |
| = | Compare values for equality in pseudocode. | count = 0 |
| INPUT / OUTPUT | Receive information / display it. | OUTPUT count |
| RETURN | Give a result back and leave the procedure. | RETURN best |
| IF / ELSE / END IF | Choose a branch from a condition. | IF charge >= 80 THEN |
| FOR EACH / END FOR | Repeat for the items in a collection. | FOR EACH charge IN readings |

#### Example that counts ready batteries

```text
ALGORITHM CountReady(readings)
    count ← 0
    FOR EACH charge IN readings DO
        IF charge >= 80 THEN
            count ← count + 1
        END IF
    END FOR
    RETURN count
```

The statement count ← count + 1 means “read the old count, add one, and store the result.” It is an update, not an algebraic equation. With no readings, the loop runs zero times and the initialized count of 0 is returned.

#### Replace vague instructions with visible decisions

“Check the batteries” does not say what to compare or what to do next. “If charge >= 80, increase count by one” does. Use meaningful names, indent nested instructions, initialize variables before use, and show where the result leaves the algorithm.

**Watch the notation** Python uses = for assignment and == for equality comparison. The arrow convention belongs to our pseudocode, not to Python syntax.

## 1.7 Flowcharts and Standard Symbols

### Show the path through an algorithm

A flowchart represents steps and decisions with shapes connected by arrows. It is especially useful when a reader needs to see branching or a repeated path. The following are common introductory conventions; the label inside each symbol should state its exact purpose.

![Figure 1.5: Common flowchart symbols](assets/images/figure-5.png)

**Figure 1.5  Four common symbols used in this chapter’s flowcharts.**

#### Arrows and connectors

An arrow shows the direction of control. Read from Start and follow one arrow at a time. A decision diamond usually has two exits labeled Yes and No, or True and False. A small labeled circle can connect distant parts of a larger diagram, but short diagrams rarely need one.

#### Keep the picture faithful to the method

* Write actions in process boxes and questions in decision diamonds.
* Show both outcomes of a decision, including the case where no action is needed.
* Draw a loop’s return arrow back to the condition or the appropriate next step.
* Give every terminating route a clear way to reach End.

A neat diagram can still describe incorrect logic. Trace it with a real input and check its decisions, just as you would check pseudocode. If the chart grows too crowded, divide the task into named procedures and chart each one separately.

**Common mistake** A diamond labeled “Update count” is misleading: that is an action. A diamond labeled “Charge >= 80?” represents a decision.

### 1.7 Flowcharts in Practice

### Follow both branches

Consider a simplified campus gate. Its input is whether a card is valid. A valid card unlocks the gate; an invalid card produces a denial message. This teaching model leaves out real access-control details such as time restrictions and hardware faults.

![Figure 1.6: A flowchart showing both gate-decision branches](assets/images/figure-6.png)

**Figure 1.6  Both branches complete the decision and then reach End.**

For a valid card, follow Start → Read card validity → Yes → Unlock gate → End. For an invalid card, follow the No branch to the denial message. Only one branch runs for a given decision.

**Your turn** Suppose access also requires the laboratory to be open. Add a second decision or change the condition to “card valid AND laboratory open.” Check all four combinations of the two inputs.

## 1.8 Tracing an Algorithm

### Make every state change visible

A trace is a manual execution of an algorithm on a particular input. Instead of guessing the output, record the values of important variables as each step runs. This makes an incorrect update or a skipped boundary much easier to see.

#### Trace the ready battery counter

Use the pseudocode from Section 1.6 with readings [42, 80, 58, 91]. The count starts at 0. Each reading is tested against the condition charge >= 80.

| Step | Reading | Condition | Count before | Count after |
| :---: | :---- | :---- | :---- | :---- |
| Initialize | - | - | - | 0 |
| 1 | 42 | 42 >= 80 is false | 0 | 0 |
| 2 | 80 | 80 >= 80 is true | 0 | 1 |
| 3 | 58 | 58 >= 80 is false | 1 | 1 |
| 4 | 91 | 91 >= 80 is true | 1 | 2 |
| Return | - | Loop finished | 2 | 2 |

The returned answer is 2. Notice the row for 80: it changes the count because equality is included. If the condition were charge > 80, the same input would produce 1. A single symbol can change the meaning of the specification.

#### How to build a useful trace table

1. Write the input and the starting values of the variables.
2. Choose one consistent moment to record each row, such as after an iteration.
3. Evaluate conditions using the current values, not the values you expect later.
4. Record the update, or explicitly show that the value stays unchanged.
5. Continue until the loop finishes or a RETURN is reached.

A trace demonstrates behavior for one input. It can reveal a bug, but a successful trace does not establish correctness for every valid input. Section 1.9 adds a general argument.

**Quick check** Repeat the trace for [80, 79, 80]. Before checking the answers, identify which two rows increase the count.

## 1.9 Correctness, Termination, and Edge Cases

### Check more than the ordinary example

A useful solution must produce the required result and finish when it is supposed to. Correctness is always judged against the specification. If empty input is allowed, the behavior on an empty list is part of correctness, not an optional extra.

#### Correctness needs a reason

For the counting algorithm, a useful invariant is: after each iteration, count equals the number of ready batteries among the readings already processed. An invariant is a statement that remains true at a chosen point throughout a loop.

It is true initially because no readings have been processed and count is 0. Each iteration adds one exactly when the next reading qualifies, so it remains true. When every reading has been processed, it describes the whole input and establishes the required result.

#### Termination needs progress

The FOR EACH loop visits a finite collection once, so the number of unread items decreases until none remain. In a WHILE loop, check the update explicitly: “WHILE i < n” with no change to i can repeat forever if the condition starts true.

#### Test the boundaries deliberately

| Test for CountReady | Expected result | What it checks |
| :---- | :---- | :---- |
| [] | 0 | No iterations |
| [80] | 1 | Exact threshold |
| [79] | 0 | Just below threshold |
| [80, 80] | 2 | Repeated qualifying values |
| [0, 100] | 1 | Valid range endpoints |

An edge case is an unusual but important situation, often near a boundary. Invalid input is different: ["unknown"] violates the numeric-input assumption. A production program should reject or handle it through a defined validation policy.

**Takeaway** Tests provide evidence for specific cases. A loop invariant explains why the method works across its valid input domain. Use both when the stakes or complexity justify them.

## 1.10 Finding the Largest Value

### Keep the best value seen so far

We can now solve the running problem from beginning to end. For this general algorithm, the input is a finite list of comparable finite numbers. Negative values are allowed; the battery example is simply one use of the method. The output is the largest value, or NONE if the list is empty.

#### The idea

Choose the first value as a temporary best. Compare each later value with it. Replace the best only when the new value is larger. Once every value has been examined, return the candidate that remains.

![Figure 1.7: Tracking the largest value seen so far](assets/images/figure-7.png)

**Figure 1.7  The candidate changes at 76 and 91, and stays unchanged at 58 and 67.**

```text
ALGORITHM FindLargest(values)
    IF values is empty THEN
        RETURN NONE
    END IF

    best ← first value in values
    FOR EACH value AFTER the first IN values DO
        IF value > best THEN
            best ← value
        END IF
    END FOR
    RETURN best
```

NONE is a special marker meaning “no maximum is available,” not the number 0. A caller can turn that result into a message. The early return also prevents the algorithm from trying to read a first value that does not exist.

**Why initialization matters** Starting best at 0 would fail for [-8, -3, -12]: the algorithm would return 0 even though 0 is not in the list. Starting with the first actual value avoids this error.

### Worked Trace and Reasoning

### Explain why the answer is 91

The first value, 42, establishes the initial candidate. The loop begins with the second value, so five values require four comparisons.

| Stage | New value | Test | Best after |
| :---: | :---- | :---- | :---- |
| Initialize | 42 | First value becomes best | 42 |
| Compare 1 | 76 | 76 > 42 is true | 76 |
| Compare 2 | 58 | 58 > 76 is false | 76 |
| Compare 3 | 91 | 91 > 76 is true | 91 |
| Compare 4 | 67 | 67 > 91 is false | 91 |

#### A short correctness argument

After initialization and after each comparison, best is the largest value in the part of the list already examined. This is the loop invariant.

Initially, only the first value has been examined, so the claim is true. For the next value, there are two possibilities: it is larger and replaces best, or it is not larger and best remains correct. After the final comparison, the examined part is the entire list. Therefore best is the maximum.

#### Why the algorithm stops

Each iteration moves to the next unread value. The list is finite, so eventually no unread values remain. The empty case stops immediately with NONE; a one-value list skips all comparisons and returns that value.

#### How much work it does

For a non-empty list of n values, there are exactly n - 1 value comparisons. The work grows in proportion to n, so we call it linear time, written O(n). Only a fixed number of working variables is needed, giving O(1) auxiliary space. These costs exclude storage for the input itself.

**Notice** No sorting is needed. A full order contains more information than this task requires. If two values tie for the maximum, the output is still the same maximum value.

### Python Implementation

### Run the method and test its boundaries

```python
def find_largest(values):
    if len(values) == 0:
        return None

    best = values[0]
    for i in range(1, len(values)):
        if values[i] > best:
            best = values[i]
    return best

readings = [42, 76, 58, 91, 67]
print(find_largest(readings))  # 91
```

def introduces a function. values is the input parameter, and len(values) gives the number of elements. values[0] is the first element. range(1, len(values)) visits indices from 1 up to, but not including, the list length. Indentation shows which statements belong inside the loop or condition. [2]

return gives the result back to the caller; print displays it. None is Python’s marker for the empty case in our chosen contract. The function assumes a list of valid, comparable finite numbers; it does not validate mixed data types or special values such as NaN.

#### Expected behavior

| Input | Result | Reason |
| :---- | :---- | :---- |
| [42, 76, 58, 91, 67] | 91 | Ordinary unsorted input |
| [] | None | No maximum exists |
| [7] | 7 | One value needs no comparison |
| [-8, -3, -12] | -3 | All values are negative |
| [9, 9, 4] | 9 | A repeated maximum is allowed |
| [2, 5, 11] | 11 | The largest value is last |

Python already provides max. For a valid list, max(values, default=None) follows the same empty-input policy. Without default, max on an empty list raises ValueError. We wrote the method ourselves to understand its logic, not because Python lacks the operation. [3]

**Try a small modification** Change the comparison to find the smallest value. Then explain why the first-value initialization should remain.

### Practice

### Build and check your own solutions

Try these on paper before running code. Explain your decisions in complete sentences where requested. Short answer guidance appears on the next page.

#### Understand

1. A library app should find “the best available study room.” Write a clearer specification using room capacity and availability. State one assumption and one constraint.

2. A team wants the ID of the battery with the highest charge. Is a list containing only charge values enough? Explain what you would add and how you would handle a tie.

3. Identify the control structure: (a) display a result after computing it; (b) reject a reading if it is outside 0 to 100; (c) inspect every reading in a list.

#### Trace and Diagnose

4. Trace CountReady for [80, 79, 80]. Record the count after each iteration.

5. Trace FindLargest for [-4, -9, -2, -2]. Record the candidate after initialization and each comparison. How many comparisons occur?

6. A student initializes best to 0. Give an input that exposes the bug, state the incorrect output, and repair the initialization.

7. The loop below is meant to visit three positions. Explain why it fails to stop and write the missing update.

```text
i ← 0
WHILE i < 3 DO
    OUTPUT i
END WHILE
```

#### Design

8. Write pseudocode that counts values strictly below 20 in a list of valid charge readings. Include the empty case, and give three tests that cover a boundary.

9. Modify the maximum-finding method so that it returns the first index of the maximum. Use zero-based indexing. Define the empty-input result and show what happens for [5, 9, 9].

#### Optional Team Activity

Design a “battery readiness report” that returns the highest charge and the number of readings at least 80. Agree on the specification, draw its flowchart, and test it with [42, 80, 58, 91]. One person writes the method; another traces it without asking for explanations. Revise any ambiguous instruction.

### Answer Guidance and Review

### Check your reasoning

1. One possible specification: given room IDs, capacities, availability, and a group size, return any available room whose capacity is sufficient; report no match if none qualifies. Assume availability is current. Require that the selected room accommodate the whole group. Other clear specifications are possible.

2. Keep a battery ID paired with each charge. Define a tie rule, such as returning the first battery with the maximum charge. The rule must be explicit because several IDs may be valid.

3. (a) Sequence. (b) Selection. (c) Repetition. Real programs often combine them.

4. The count starts at 0, then becomes 1, 1, 2. The final result is 2.

5. The candidate values are -4, -4, -2, -2. There are three comparisons and the returned maximum is -2.

6. For [-8, -3, -12], initializing to 0 incorrectly returns 0. Check for empty input first, then initialize best from the first value.

7. i never changes, so i < 3 stays true. Add i ← i + 1 inside the loop, after OUTPUT i. It then displays 0, 1, 2 and stops.

8. Initialize count to 0; visit every charge; increment only when charge < 20; return count. Tests: [] gives 0, [19, 20, 21] gives 1, and [0, 0] gives 2. Exactly 20 does not qualify.

9. Return NONE if empty. Otherwise start best_index at 0, scan indices 1 through n - 1, and replace best_index only when values[i] > values[best_index]. Return best_index. For [5, 9, 9], return 1. Using a strict > preserves the first maximum.

Team activity: the highest charge is 91 and the count at or above 80 is 2. A single loop can update both results. For an empty list, a sensible agreed result is (NONE, 0).

#### Before Moving to Chapter 2

You should be able to describe an input and output contract, choose a useful model, express a method with control structures, trace it, and explain its behavior at the boundaries. If you can explain why the maximum algorithm starts with the first value, you understand one of the most important decisions in this chapter.

#### References and Further Reading

[1] Wing, J. M. (2006). Computational Thinking. Communications of the ACM, 49(3), 33–35. [https://www.cs.cmu.edu/~wing/publications/Wing06.pdf](https://www.cs.cmu.edu/~wing/publications/Wing06.pdf)

[2] Python Software Foundation. The Python Tutorial, More Control Flow Tools. [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)

[3] Python Software Foundation. Built-in Functions, max. [https://docs.python.org/3/library/functions.html#max](https://docs.python.org/3/library/functions.html#max)

> **Note:** All battery data are fictional teaching examples. Diagrams, exercises, and worked examples were created for this chapter. Prepared with AI assistance; verify against your course requirements before team submission.
