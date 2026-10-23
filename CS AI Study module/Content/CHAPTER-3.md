CHAPTER 03 • PYTHON ALGORITHMS

# Measuring Algorithm Efficiency

The central question How much work will your program do when the data grows?

A program that handles ten student scores can feel instant. Give it a million scores, and its design starts to matter. This chapter gives you a practical way to predict that change before you run the program.

https://github.com/f1rous/PentaByte_Repository/blob/main/CS%20AI%20Study%20module/Assets/Chapter%20Assets/Chapter_3/1.png

*Figure 3.1 • Comparing one scan with every unique pair. These are counts, not measured seconds.*

## From working code to scalable code

Chapter 1 explained how to design an algorithm. Chapter 2 translated those ideas into Python. Now we ask how the amount of work and memory changes as the input grows. Correctness still comes first: a fast program that returns the wrong answer is not a solution.

| You will learn to… | You will use… |
| --- | --- |
| Define what “size” means | Input measures and a basic cost model |
| Explain growth clearly | Cases, upper bounds, and common growth rates |
| Analyze real Python code | Loop counts, memory accounting, and experiments |
| Share reproducible work | A GitHub-friendly project layout and README |

Chapter convention: n is a nonnegative input size. Unless stated otherwise, examples use ordinary machine-sized values, and indexing, assignment, comparison, and arithmetic are treated as constant-time operations.

## 3.1 • FOUNDATIONS

## Input size and basic operations

Before asking whether an algorithm is efficient, decide what its input size measures. The same letter n can represent very different things in different problems.

| Problem | Useful size measure | Basic operation |
| --- | --- | --- |
| Find the highest score | n = number of scores | Compare a score with the current maximum |
| Search text | n = number of characters | Compare characters |
| Process a grid | r rows and c columns | Visit one cell |
| Multiply large integers | b = number of bits | An operation on a fixed-size part |

## Count a meaningful repeated action

def largest(values):    if not values:        raise ValueError("values must not be empty")    best = values[0]    for i in range(1, len(values)):        if values[i] > best:            best = values[i]    return best

For n ≥ 1, the comparison values[i] > best runs exactly n − 1 times. The number of assignments to best depends on the order of the values, but the comparison count does not. The overall running time grows linearly with n.

## A model is a deliberate simplification

Counting every processor instruction would hide the main idea. Instead, select an operation that reflects the repeated work, state what you count, and use that choice consistently. Counting comparisons in one algorithm and all instructions in another does not give a fair exact-count comparison.

Python integers can grow arbitrarily large. Arithmetic on a thousand-digit integer is not generally the same cost as arithmetic on a small integer. When integer size matters, include the number of bits or digits in your analysis.

## 3.2 • MEASUREMENT AND PREDICTION

## Seconds tell one story. Growth tells another.

Measured running time describes one implementation on one machine with one input. Growth-rate analysis describes how its work changes as the input gets larger. Both are useful, but they answer different questions.

| Measured running time | Growth-rate analysis |
| --- | --- |
| Affected by hardware, Python version, and system load | Based on a stated model of computation |
| Useful for comparing actual implementations | Useful for predicting scaling behavior |
| Usually reported in seconds | Usually reported as a function of input size |

https://github.com/f1rous/PentaByte_Repository/blob/main/CS%20AI%20Study%20module/Assets/Chapter%20Assets/Chapter_3/2.png

*Figure 3.2 • Hypothetical operation counts: 20n and n². The lower-growth method wins only after the crossover.*

At n = 10, algorithm A uses 200 model operations and B uses 100. At n = 100, A uses 2,000 and B uses 10,000. A linear growth rate does not guarantee a smaller count for every input size.

## Use the two approaches together

Start with analysis to identify how a design scales. Then measure realistic workloads to learn whether constants, implementation details, or input characteristics change the practical choice. Never label a chart of operation counts as a chart of execution time.

## 3.3 • CASES

## One algorithm, different inputs

Inputs of the same size can lead to different amounts of work. A linear search is a simple example: it stops when it finds the target, or when it runs out of items.

def linear_search(values, target):    for i, value in enumerate(values):        if value == target:            return i    return -1

| Case | Input situation, n ≥ 1 | Equality comparisons |
| --- | --- | --- |
| Best | The first item matches | 1 |
| Worst | Only the last item matches, or no item matches | n |
| Average, under a stated model | Exactly one match; each position equally likely | (n + 1) / 2 |

## Why the average needs an assumption

For a successful search with one equally likely match position, the possible counts are 1, 2, …, n. Their average is (1 + 2 + … + n) / n = (n + 1) / 2. If common targets appear near the beginning, the average can be lower.

If a search succeeds with probability p, successful positions are uniform, and an unsuccessful search checks all n items, the expected comparison count is p(n + 1)/2 + (1 − p)n. A different workload requires a different probability model.

## Do not mix up “case” and “bound”

Best, average, and worst describe which inputs you consider. Big-O describes an upper bound on a function. You can give a Big-O bound for the best-case function, the average-case function, or the worst-case function.

For this search, the best-case time is Θ(1), while the stated average-case and worst-case times are Θ(n). The symbol Θ means a tight asymptotic bound; Section 3.4 explains the distinction.

## 3.4 • MATHEMATICAL LANGUAGE

## Big-O: an eventual upper bound

We write T(n) = O(g(n)) when T(n) is at most a constant multiple of g(n) for every sufficiently large n. In plain language: beyond some threshold, g(n) can provide a ceiling after we scale it by a fixed constant.

## The definition, unpacked

There must be constants c > 0 and n₀ such that 0 ≤ T(n) ≤ c · g(n) for every n ≥ n₀.

| Symbol | Meaning |
| --- | --- |
| T(n) | The time or operation-count function being bounded |
| g(n) | A comparison growth function, such as n or n² |
| c | A fixed multiplier independent of n |
| n₀ | The input size after which the bound must hold |

## Worked bound: T(n) = 3n + 2

For every n ≥ 1, we have 3n + 2 ≤ 3n + 2n = 5n. Choose c = 5 and n₀ = 1. This proves T(n) = O(n). We do not need to claim that the algorithm performs exactly n operations.

## Upper bounds are not automatically tight

The same function is also O(n²), because n ≤ n² for n ≥ 1. That bound is valid but less informative. When we say an algorithm is “linear,” we usually intend a tight description of its growth.

| Notation | What it says |
| --- | --- |
| O(g(n)) | An asymptotic upper bound |
| Ω(g(n)) | An asymptotic lower bound |
| Θ(g(n)) | Both bounds hold: the growth rate is tight |

Simplification example: 4n² + 7n + 12 is Θ(n²). The quadratic term eventually dominates the lower-order terms. Constants and smaller terms still matter when estimating actual performance on small inputs.

Further reading: NIST, “big-O notation,” and Cornell CS 2112, “Asymptotic complexity” (references at the end).

## 3.5 • GROWTH-RATE LANDSCAPE

## Six growth rates worth recognizing

https://github.com/f1rous/PentaByte_Repository/blob/main/CS%20AI%20Study%20module/Assets/Chapter%20Assets/Chapter_3/3.png

*Figure 3.3 • Representative functions, not benchmark results. Each vertical step on the logarithmic axis represents a multiplication.*

| Growth | Typical pattern | If n doubles… |
| --- | --- | --- |
| O(1) | Index one list element | Work stays bounded |
| O(log n) | Repeatedly halve a search region | Only a fixed number of extra stages |
| O(n) | Scan every item once | About twice the work |
| O(n log n) | n work across about log n levels | A little more than twice |
| O(n²) | Compare every pair | About four times |
| O(2ⁿ) | Explore binary choices exhaustively | The model count is squared |

These are common patterns, not rules based on appearance. A loop can be constant, logarithmic, linear, or something else depending on how many times it runs and what each iteration does.

Logarithm bases differ by a constant factor, so O(log₂ n) and O(log₁₀ n) describe the same asymptotic class. We use base 2 when counting repeated halving.

## 3.5 • READING THE NUMBERS

## Why small differences become large

| n | 1 | log₂ n | n | n log₂ n | n² | 2ⁿ |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | 1 | 3 | 8 | 24 | 64 | 256 |
| 16 | 1 | 4 | 16 | 64 | 256 | 65,536 |
| 32 | 1 | 5 | 32 | 160 | 1,024 | 4,294,967,296 |

The entries are mathematical function values. They do not claim that every algorithm in a growth class performs those exact numbers of operations.

## Logarithmic: keep shrinking the problem

remaining = nsteps = 0while remaining > 1:    remaining //= 2    steps += 1

For n ≥ 1, this loop takes floor(log₂ n) steps. Starting at 32 gives 32 → 16 → 8 → 4 → 2 → 1: five iterations. Binary search uses a related idea, but it needs ordered data and efficient access to the middle element.

## Linearithmic: repeated levels of linear work

A common divide-and-conquer structure has about log₂ n levels and O(n) total work at each level. Multiplying the two gives O(n log n). Merge sort is a standard example; the work at a level is added across its subproblems.

## Exponential: each extra choice multiplies the possibilities

A set of n items has 2ⁿ subsets. Adding one item doubles the number of subsets; doubling n squares it. An algorithm that explicitly copies every subset can take Θ(n2ⁿ) time because writing the contents also costs work. Counting possibilities and producing all their contents are different tasks.

## 3.6 • LOOP ANALYSIS

## Add sequential work; inspect nested work

## Two scans do not make a quadratic algorithm

for value in values:        # n iterations    total += valuefor value in values:        # n more iterations    print(value)

Ignoring the variable cost of displaying long values, there are n + n = 2n body executions. Under a constant-cost body model, this is Θ(n). Sequential blocks add their costs; they do not multiply them.

## Independent nested loops multiply

for i in range(n):    for j in range(n):        count += 1

The inner body runs n times for each of n outer iterations: n × n = n². With a constant-cost body, the total time is Θ(n²).

## A fixed inner limit stays fixed

for i in range(n):    for j in range(5):        count += 1

This body runs 5n times, giving Θ(n), even though the loops are nested. Nesting alone does not determine the growth rate.

## Keep independent input sizes separate

If an outer loop visits n students and an inner loop visits m assignments, the work is Θ(nm). Do not replace this with Θ(n²) unless you know m grows proportionally to n. Two separate scans of those inputs would instead take Θ(n + m).

## 3.6 • DEPENDENT BOUNDS

## When the inner loop changes

for i in range(n):    for j in range(i + 1, n):        count += 1

https://github.com/f1rous/PentaByte_Repository/blob/main/CS%20AI%20Study%20module/Assets/Chapter%20Assets/Chapter_3/4.png

*Figure 3.4 • At n = 5, only cells with j > i are visited. Each unordered pair is counted once.*

The inner counts are n − 1, n − 2, …, 1, 0. Their sum is n(n − 1)/2. The leading term is n²/2, so the tight growth rate is Θ(n²). Avoiding repeated pairs roughly halves the leading count; it does not change the quadratic class.

## A logarithmic inner loop

for i in range(n):    remaining = n    while remaining > 1:        remaining //= 2        count += 1

Each outer iteration restarts remaining at n. For n ≥ 1, the body runs n · floor(log₂ n) times: Θ(n log n) as n grows. If remaining were initialized only once before the outer loop, the result would be different because later outer iterations would not repeat the halving work.

Analysis habit: identify the loop bounds, check where variables are reset, count the inner work for each outer iteration, and then sum. Include the cost of function calls inside the body.

## 3.7 • MEMORY

## Input storage and auxiliary space

Time is only one resource. Space complexity describes how memory use grows with input size. Always say what you include: input storage, extra working memory, and returned output can be counted separately.

https://github.com/f1rous/PentaByte_Repository/blob/main/CS%20AI%20Study%20module/Assets/Chapter%20Assets/Chapter_3/5.png

*Figure 3.5 • A running maximum adds constant working storage; a list copy adds storage proportional to the input.*

| Operation on n values | Auxiliary space | Why |
| --- | --- | --- |
| Find a maximum by scanning | O(1) | A fixed number of working variables |
| Make values[:] | O(n) | A new list stores n references |
| Build a set of distinct values | O(n) worst case | Up to n stored elements |
| Recursive calls to depth n | O(n) stack space | Suspended calls retain local state |

## A useful reporting convention

In this chapter, auxiliary space means additional working memory, excluding the supplied input and the returned output. We report output space separately when it grows. Some sources include output in auxiliary space, so check the convention before comparing claims.

For largest(values), the input list occupies O(n) storage and the auxiliary space is O(1). If total memory includes the input, the overall bound is O(n). A copied list has O(n) auxiliary space even though its elements may refer to the same underlying objects.

## Hidden allocation is still allocation

A slice creates a new list; a comprehension creates its output; a recursive call uses stack space. A range object does not store every integer in its range. Under the usual fixed-size integer model, it occupies O(1) space; list(range(n)) occupies O(n).

## 3.8 • DESIGN CHOICES

## Spend memory to avoid repeated work

Suppose a list contains student identification numbers and you need to detect a duplicate. One method compares each item with every later item. Another remembers the values it has already seen.

def has_duplicate(values):    seen = set()    for value in values:        if value in seen:            return True        seen.add(value)    return False

| Approach | Time | Auxiliary space |
| --- | --- | --- |
| Compare unique pairs | O(n²) worst case | O(1) |
| Keep a set of seen values | O(n) expected; O(n²) worst case | O(n) worst case |

For ordinary hashable values and typical hash behavior, set membership and insertion have expected constant cost, making a full pass expected linear time. Severe collisions can degrade performance. Hashing and comparing very large objects may also require additional work.

## The trade-off in practice

The pair method stores very little but repeats comparisons. The set method stores information to avoid repeating the search. It also requires hashable values: a list cannot itself be a set element. The right choice depends on memory limits, the data type, and the workload.

## Preprocessing changes the balance

If you repeatedly ask whether IDs are present, building a set once can be worthwhile. For q membership queries, scanning a list each time takes O(qn) in the worst case. Building a set and using it for queries takes expected O(n + q), with O(n) extra storage, under the hashing assumptions above.

A single query on a short list may not justify the extra structure. Efficiency is a design decision tied to a workload, not a contest to use the most elaborate data structure.

## 3.9 • EXPERIMENT A

## Count operations before timing code

An operation counter gives a reproducible result that does not depend on processor speed. Save the following code as experiments/count_operations.py in the suggested GitHub project.

def scan_count(n):    count = 0    for _ in range(n):        count += 1    return countdef pair_count(n):    count = 0    for i in range(n):        for j in range(i + 1, n):            count += 1    return countif __name__ == "__main__":    print("n,scan,pairs")    for n in (10, 20, 40, 80):        print(f"{n},{scan_count(n)},{pair_count(n)}")

| n | Scan count | Unique-pair count | Pair-count ratio |
| --- | --- | --- | --- |
| 10 | 10 | 45 | — |
| 20 | 20 | 190 | 4.22 |
| 40 | 40 | 780 | 4.11 |
| 80 | 80 | 3160 | 4.05 |

The scan count doubles exactly. The pair-count ratio approaches 4 as n grows because the quadratic term becomes dominant. The ratio is not exactly 4 at these finite sizes because n(n − 1)/2 also contains a linear term.

These counters measure loop-body executions. They add their own overhead, so use separate timing code if your goal is to benchmark an implementation without instrumentation.

## 3.9 • EXPERIMENT B

## Measure carefully and report honestly

Use timeit to repeat a small operation. This example times a complete summation of a prepared list. Save it as experiments/time_scan.py; it needs only Python’s standard library.

import platformimport sysfrom timeit import repeatdef total(values):    result = 0    for value in values:        result += value    return resultif __name__ == "__main__":    print(sys.version.split()[0], platform.platform())    print("n,best_seconds_per_call")    for n in (1_000, 2_000, 4_000, 8_000):        values = [1] * n        runs = repeat(lambda: total(values),                      number=200, repeat=5)        print(f"{n},{min(runs) / 200:.9f}")

## What this measurement includes

Each result is the minimum of five batches, divided by the 200 calls in a batch. List creation happens outside the timed region. The callable and loop overhead are included. The minimum is useful for reducing interference from other activity; it is not the average response time of a real application.

## What to record with your results

Python version, operating system, processor, input sizes, and input construction.

The exact code revision, repetition settings, and whether setup or output is timed.

Raw measurements and the statistic reported; keep count data separate from time data.

A roughly doubling runtime supports a linear-growth hypothesis over this tested range. It does not prove an asymptotic bound. Small inputs, interpreter overhead, and memory behavior can distort ratios. The official timeit documentation also notes that garbage collection is disabled by default during timing.

## 3.10 • AVOIDING TRAPS

## Common misconceptions about complexity

| Misconception | More accurate reasoning |
| --- | --- |
| “O(n) means exactly n operations.” | It gives an eventual upper bound up to a constant factor. |
| “Big-O always means worst case.” | The case must be stated separately. |
| “Two loops mean O(n²).” | Sequential loops add; nested loops require inspection. |
| “O(1) means instant.” | The work is bounded independently of input size, but can be costly. |
| “A faster benchmark proves better growth.” | One measurement cannot establish asymptotic behavior. |
| “Average case is halfway between best and worst.” | It is an expectation under a specified input distribution. |
| “A built-in call takes one operation.” | A single Python statement can traverse, copy, or sort many items. |
| “Less code means less memory.” | Temporary objects and recursion can allocate substantial storage. |
| “O(n) is always faster than O(n²).” | Constants and input sizes affect practical performance. |
| “Removing half the pairs makes it linear.” | n(n − 1)/2 still has a quadratic leading term. |

## A six-question analysis checklist

What measures the input size? Do I need more than one variable?

Which operation am I counting, and what cost model am I using?

Which case or input distribution am I analyzing?

How many times does each block execute, including called functions?

What memory is allocated, and am I counting input and output separately?

Do experiments support my explanation, without being presented as proof?

PRACTICE • APPLY THE CHAPTER

## Reason first, then run the code

For each answer, state the input size, your counted operation, and any assumptions. Use tight growth descriptions where possible.

## 1 • A largest-value scan

A nonempty list contains 75 scores. How many comparisons does the function in Section 3.1 make? What are its time and auxiliary-space growth rates?

## 2 • A search distribution

A successful linear search checks a list of 20 items with one equally likely match position. Find the expected comparison count. Then allow a 25% probability of failure, keeping successful positions uniform.

## 3 • Sequential versus nested

for i in range(n):    work()for i in range(n):    for j in range(3):        work()

Assume work() takes constant time and constant extra space. Count its calls and classify the total time.

## 4 • Halving

Start remaining at 64 and repeatedly apply remaining //= 2 while remaining > 1. How many iterations occur? What happens to that count when the initial value doubles?

## 5 • Memory accounting

A function receives a list of n integers, copies it with values[:], scans the copy, and returns one integer. Report input storage, auxiliary space, and total memory under the chapter’s convention.

## 6 • Reproducible experiment

Extend Experiment A to n = 160. Predict both counts before running it. Add assertions for n = 0, 1, and 5. Explain why these finite checks do not prove the growth bound for all n.

## 7 • A decision with constraints

You need one duplicate check on a large list of hashable IDs. Compare pair scanning and a set, including memory limits and the assumptions behind expected linear time.

PRACTICE • ANSWERS

## Check the reasoning, not just the label

## 1 • Largest value

There are 74 comparisons. Every item after the first is compared with the running maximum. Time is Θ(n); auxiliary space is O(1). Including the input list gives O(n) total space.

## 2 • Expected search cost

With guaranteed success, the expected count is (20 + 1)/2 = 10.5. With success probability 0.75, it is 0.75 × 10.5 + 0.25 × 20 = 12.875. An expected count can be fractional even though every individual run uses a whole number of comparisons.

## 3 • Sequential versus nested

The first block calls work() n times; the second calls it 3n times. The total is 4n, so time is Θ(n). The fixed inner limit does not introduce another factor that grows with n.

## 4 • Halving

Six iterations take 64 to 1. Starting at 128 takes seven. Doubling a power-of-two input adds one iteration; the growth is Θ(log n).

## 5 • Space

Input storage is O(n), auxiliary space is O(n) for the copy, and the returned integer occupies O(1) space under the fixed-size model. Total space remains O(n): adding two linear terms does not make the result quadratic.

## 6 • Counts and checks

At n = 160, the scan count is 160 and the pair count is 160 × 159 / 2 = 12,720. Small tests can catch mistakes; the summation establishes the general count.

assert scan_count(0) == 0assert scan_count(1) == 1assert scan_count(5) == 5assert pair_count(0) == 0assert pair_count(1) == 0assert pair_count(5) == 10

## 7 • Trade-off

A set usually gives expected O(n) time with O(n) extra memory, assuming suitable hashing and bounded-cost values. Pair scanning has O(n²) worst-case time but O(1) auxiliary space. A strict memory limit can make the slower method relevant; severe hash collisions can undermine the expected-time advantage.

GITHUB COMPANION • REPRODUCIBLE STRUCTURE

## Make the chapter easy to explore on GitHub

Keep the Word chapter as the readable guide and place runnable experiments beside it. The following is a suggested repository layout; it does not imply that a repository has been created or published.

| Repository path | Purpose |
| --- | --- |
| README.md | Explain the chapter, run commands, and assumptions |
| docs/Chapter_3_Measuring_Algorithm_Efficiency.docx | Keep this editable chapter |
| experiments/count_operations.py | Copy Experiment A from Section 3.9 |
| experiments/time_scan.py | Copy Experiment B from Section 3.9 |
| results/operation_counts.csv | Record deterministic counts |
| results/timing_notes.md | Record environment and timing observations |

## A README template to copy

# Chapter 3: Measuring Algorithm EfficiencyExplore operation counts, growth rates, and memorytrade-offs using small Python experiments.## RequirementsPython 3; standard library only.## Run from the repository rootpython experiments/count_operations.pypython experiments/time_scan.py## InterpretationCounts are deterministic; timings vary by environment.The model treats small-value operations as constant time.See the Word chapter for assumptions and worked answers.

Depending on your installation, use python3 instead of python. Keep filenames consistent with the commands. Run both experiments locally before sharing, and record the commit identifier with timing results so someone else can reproduce the exact implementation.

## A meaningful commit message

“Add Chapter 3 efficiency guide and operation-count experiments” explains what changed. When updating the analysis, update the matching code, results, and README together.

CHAPTER CLOSE • REFERENCE DESK

## The habits to carry forward

An efficiency claim is strongest when someone else can reconstruct it. Define the input, state the case, count the work, account for memory, and explain your assumptions. Then use measurements to investigate practical behavior.

| When you see… | Ask… |
| --- | --- |
| A loop | How many iterations, and what happens inside? |
| Nested loops | Are their limits independent, fixed, or dependent? |
| A function call | Does it scan, copy, sort, recurse, or allocate? |
| A complexity label | Which case, which input size, and is the bound tight? |
| A benchmark | Which environment, data, repetition method, and code revision? |

## Selected references

NIST Dictionary of Algorithms and Data Structures. “big-O notation.” A concise definition of the asymptotic upper bound.https://xlinux.nist.gov/dads/HTML/bigOnotation.html

Cornell University, CS 2112. “Asymptotic complexity.” Course notes on growth rates and asymptotic analysis.https://courses.cs.cornell.edu/cs2112/2022fa/lectures/complexity/index.html

Python documentation. “timeit — Measure execution time of small code snippets.” Details of repeat, number, setup, and timing interpretation.https://docs.python.org/3/library/timeit.html

## Chapter checkpoint

You are ready to move on when you can explain why two sequential scans are linear, why unique-pair comparisons are quadratic, why an average-case claim needs a distribution, and why a constant-space scan can still have linear total storage when its input is included.

All graphs in this chapter show explicitly labeled mathematical models. The operation-count table is calculated from the provided loops. No machine-specific timing results are invented.
