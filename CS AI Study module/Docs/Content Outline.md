# Algorithms, Data Structures, and Connectionist AI

## A Beginner’s Guide to Learning Through Problems

**Team:** PentaByte  
**Document:** Focused Project Content Outline  
**Outline prepared by:** Swapnil Milon Mondal (苏明)  
**Role:** Content Lead  
**Date:** 22 October 2026  
**Audience:** Beginning university students with little or no programming experience  
**Language for examples:** Python, using supplied beginner notebooks  
**Production window:** One month for the study guide, PPT, and videos

## **Purpose and Scope**

Introduce beginners to algorithms, data structures, and connectionist AI through small, understandable problems. Help readers build confidence, modify simple examples, and explore further. We focus on essential concepts, clear explanations, and practical examples. Keep the content manageable for completing the study guide, presentation, and videos within one month.

## **Learning Goals**

By the end, readers should be able to:

1. Turn an everyday problem into clear steps and a small Python program.  
2. Choose a basic data structure for storing or organizing information.  
3. Trace simple searching, sorting, and route-finding algorithms.  
4. Explain how connected artificial neurons make predictions and learn from examples.  
5. Run, inspect, and modify a small classifier while recognizing its limitations.

## Structure and Chapter Pattern

| Part | Focus | Chapters |
| :---: | :---: | :---: |
| **I** | Computational Thinking and Python Foundations | **1–3** |
| **II** | Core Data Structures | **4–7** |
| **III** | Algorithm Design and Problem-Solving | **8–11** |
| **IV** | Connectionist AI and Neural Networks | **12–16** |
| **V** | Integration and Practical Projects | **17–18** |

Each chapter follows one short sequence: **start with a problem → introduce the necessary idea → work through an example → try one small change**. Use a diagram, trace table, or short code snippet where it helps. Include a brief answer or hint and one key takeaway. These are teaching elements within the three sections, not extra subchapters.

Use the reference files’ approachable questions, everyday analogies, diagrams, case examples, and short recap style. Keep the subject focused on algorithms, data structures, and connectionist AI; the broad Big Data and Software/Symbolic AI surveys are not additional units. Treat reference examples as teaching inspiration and verify factual claims before using them in the deliverables.

Reuse student records for early examples, a small campus map for graphs, and the Iris flower dataset for AI. Most activities should involve tracing, predicting, or modifying supplied examples; readers do not need to build every algorithm from scratch.

---

# Part I — Computational Thinking and Python Foundations

## **Chapter 1 — From Problems to Algorithms**

**Starting problem:** How can we find the highest score in a class?

**1.1** Identify the inputs, expected output, and smaller steps.  
**1.2** Write and trace a simple algorithm using pseudocode.  
**1.3** Work through the highest-score example; try repeated scores and an empty list.

**Worked example:** Trace scores `[72, 85, 68, 91, 85]`; the highest is 91\. Ask what the program should report if no scores are available.

## **Chapter 2 — Essential Python for the Guide**

**Starting problem:** How can we turn our score-processing steps into a working program?

**2.1** Run a prepared notebook; use variables, numbers, lists, and output.  
**2.2** Read and modify conditions, loops, and a simple function.  
**2.3** Complete a short score-summary program; change the pass mark and predict the result.

**Worked example:** Reuse those five scores, count how many meet a pass mark of 60, then change the mark to 80\. Expected counts: 5 and 3\.

## **Chapter 3 — Measuring Algorithm Efficiency**

**Starting problem:** What changes when a class has 30 students instead of 3,000?

**3.1** Count basic operations and introduce time complexity as growth with input size.  
**3.2** Recognize O(1), O(n), and O(n²) visually; introduce O(log n) through repeated halving in Chapter 8\.  
**3.3** Compare keeping one highest score with copying the whole list to introduce extra memory and space complexity.

**Worked example:** Contrast scanning 5 and 50 scores. Keeping only the current maximum uses a fixed amount of extra storage; making another list grows with the input.

---

# Part II — Core Data Structures

## Chapter 4 — Data Organization, Arrays, and Python Lists

**Starting problem:** How should we store and update a class’s scores?

**4.1** Understand indexed collections: the basic idea of arrays and Python lists.  
**4.2** Access, add, update, remove, and loop through list items.  
**4.3** Modify a score list and choose the operations needed for a new student.

**Worked example:** Add a score of 76, correct 68 to 78, and remove one registration. Show the list after each operation.

## **Chapter 5 — Linked Lists, Stacks, and Queues**

**Starting problem:** Why do an undo button and a waiting line process items differently?

5.1 Recognize a linked list through a node-and-link diagram only.  
5.2 Compare stacks (last in, first out) and queues (first in, first out).  
5.3 Trace an undo stack and a help-desk queue; modify a supplied example.

**Worked example:** Add tasks A, B, and C. Predict the removal order for an undo stack and a service queue: C–B–A versus A–B–C.

## **Chapter 6 — Hash Tables, Dictionaries, and Sets**

**Starting problem:** How can we find a student by ID and remove duplicate registrations?

**6.1** Understand key–value lookup and the basic purpose of hashing.  
**6.2** Use a dictionary for records and a set for unique values.  
**6.3** Look up student IDs and remove duplicates; choose a list, dictionary, or set.

**Worked example:** Find the name for student ID S02 in a dictionary; reduce registrations `["S01", "S02", "S01"]` to two unique IDs.

## **Chapter 7 — Trees, Heaps, and Graph Representations**

**Starting problem:** How do we represent folders, urgent tasks, and connected campus locations?

**7.1** Recognize a tree as a hierarchy and a heap as a way to support priority selection.  
**7.2** Represent a small graph using vertices, edges, and an adjacency list.  
**7.3** Build a five-location campus map and add one new connection.

**Depth limit:** Trees and heaps receive brief visual introductions; only the graph representation needs code.

**Worked example:** Connect Dorm, Library, Canteen, Lab, and Gate. Draw the map first, then write the same connections as an adjacency list.

---

# Part III — Algorithm Design and Problem-Solving

## **Chapter 8 — Searching and Elementary Sorting**

**Starting problem:** How can we find a student record and put scores in order?

**8.1** Trace linear search and binary search; explain why binary search requires sorted data.  
**8.2** Trace insertion sort as arranging cards in your hand, then use Python’s built-in sorting.  
**8.3** Search and sort sample records; compare the number of search checks.

**Worked example:** Find 85 in `[68, 72, 85, 91, 96]`. Compare a sequential scan with checking the middle; then trace insertion sort on `[85, 68, 91, 72]`.

## Chapter 9 — Recursion and Divide and Conquer

**Starting problem:** How can splitting a large sorting task make it easier to understand?

**9.1** Understand recursion through a base case and a smaller version of the problem.  
**9.2** Trace merge sort visually: split, solve, and combine.  
**9.3** Merge two short sorted lists and complete a missing step in the trace.

**Depth limit:** No full merge-sort implementation or recurrence calculations.

**Worked example:** Split `[8, 3, 6, 2]` into smaller lists and combine sorted pieces into `[2, 3, 6, 8]`. Let readers finish the final merge.

## **Chapter 10 — Graph Traversal and Shortest Paths**

**Starting problem:** Which route crosses the fewest connections on our campus map?

**10.1** Explore a graph using breadth-first search, a queue, and visited locations.  
**10.2** Trace a supplied BFS example and reconstruct a route.  
**10.3** Change a connection and test an unreachable destination.

**Key boundary:** Fewest edges means a shortest route in an unweighted graph; it does not necessarily mean the shortest physical distance.

**Worked example:** Use edges Dorm–Library, Dorm–Canteen, Library–Lab, Canteen–Gate, and Gate–Lab. Find a route from Dorm to Lab, then remove both links to Lab.

## **Chapter 11 — Algorithm Design Strategies**

**Starting problem:** Does choosing the best-looking option now always give the best answer?

**11.1** Compare brute force, divide and conquer, and greedy choices in plain language.  
**11.2** Try greedy coin selection with values 1, 3, and 4 for a target of 6\.  
**11.3** Compare the greedy result with the best solution and explain why checking matters.

**Depth limit:** Use this counterexample to encourage reasoning; omit dynamic programming implementation.

**Worked example:** Greedy selection gives `4 + 1 + 1`, but `3 + 3` uses fewer coins. The reader explains why a locally attractive choice can fail.

---

# Part IV — Connectionist AI and Neural Networks

## **Chapter 12 — AI, Machine Learning, and Connectionism**

**Starting problem:** Can a program recognize a flower from measurements instead of fixed rules?

**12.1** Distinguish rule-based decisions from learning patterns in data.  
**12.2** Introduce connectionism: connected artificial neurons working together.  
**12.3** Identify samples, features, and labels in a small flower-classification example.

**Worked example:** Separate a flower’s four measured features from its species label. Ask which information is available when predicting an unknown flower.

## **Chapter 13 — Artificial Neurons and Forward Propagation**

**Starting problem:** How do several measurements become one prediction?

**13.1** Introduce inputs, weights, bias, and an activation function.  
**13.2** Calculate one neuron’s output with a small weighted-sum and ReLU example.  
**13.3** Follow information through input, hidden, and output layers using a diagram.

**Worked example:** With inputs 2 and 3, weights 0.5 and −1, and bias 1, the weighted sum is −1 and ReLU returns 0\. Change the bias to 3 and recalculate.

## **Chapter 14 — How Neural Networks Learn**

**Starting problem:** How can a network improve after making a wrong prediction?

**14.1** Compare predictions with targets and introduce loss as a measure of error.  
**14.2** Explain the training cycle: predict, measure error, calculate gradients, adjust weights.  
**14.3** Read a simple training-loss curve and discuss what improvement does—and does not—show.

**Depth limit:** Explain gradient descent and backpropagation intuitively; omit calculus derivations and training code from scratch.

**Working example:** Compare two illustrative loss curves, one falling and one flat. Ask why falling training loss alone cannot establish performance on new examples.

## Chapter 15 — Building and Evaluating a Simple Classifier

**Starting problem:** Can our network classify flowers it has not trained on?

**15.1** Open a prepared Iris notebook; split training and test data and fit scaling only on    training data.  
**15.2** Run a supplied small neural-network classifier with fixed settings; compare it with always predicting the most common training label.  
**15.3** Inspect held-out accuracy, a confusion matrix, and mistakes; explain overfitting in plain language.

**Depth limit:** Use a prepared scikit-learn notebook with a small multilayer perceptron, a fixed random seed, and no hyperparameter search. Explain each code block by its purpose; do not teach a new library course. Keep the test data out of training and model selection. Do not promise a particular accuracy.

**Worked example:** Run the notebook once, report its actual test results, and inspect a misclassified sample if one exists. If none occur, explain why this still does not guarantee perfect future predictions.

## **Chapter 16 — Deep Learning, Applications, and Responsible Use**

**Starting problem:** Would good performance on a classroom dataset make an AI safe to trust everywhere?

**16.1** Introduce deep learning as neural networks with multiple hidden layers.  
**16.2** Connect the idea to two brief applications: image recognition and driving assistance.  
**16.3** Discuss a failure scenario involving unfamiliar data, bias, privacy, and human oversight.

**Depth limit:** No survey or implementation of CNNs, RNNs, LSTMs, or transformers.

**Worked example:** A driving-assistance model encounters fog unlike its training images. Ask   what could fail, what evidence is missing, and why human oversight matters.

---

# Part V — Integration and Practical Projects

## **Chapter 17 — Connecting Data Structures, Algorithms, and AI**

**Starting problem:** How can we organize and inspect the predictions from our flower             classifier? 

**17.1** Store sample IDs, measurements, actual labels, and predictions as simple records.  
**17.2** Connect record lookup, sorting, and prediction in a workflow diagram.  
**17.3** Plan a small results explorer and trace one sample through the workflow.

**Worked example:** Draw `measurements → classifier → prediction record → search/sort → results display`. Identify which steps store data, apply algorithms, and use learned parameters.

## **Chapter 18 — Practical Projects**

**One guided project: Flower Prediction Explorer.** Reuse the Chapter 15 notebook and Chapter 17 plan; no new dataset, interface, or model is required.

**18.1 Build:** store held-out prediction results in a list of dictionaries, find a sample by ID, and sort records by one measurement.  
**18.2 Check:** verify a successful lookup, an unknown ID, sorting, and the classifier’s held-out results against the baseline.  
**18.3 Explain:** demonstrate one prediction, one search, and one sorting result; describe a limitation and one possible next step.

**Completion evidence:** One working notebook with setup instructions, a small results table, a workflow diagram, and a short explanation of how storage, algorithms, and the neural network contribute. This is the shared demonstration for the PPT and videos, not an additional standalone deliverable.

**Small reader challenge:** Change the measurement used for sorting and explain the new order. Keep the trained model unchanged.

---

## **Supporting Material**

Keep the opening material to the title and credits, purpose, contents, and quick-start instructions. Consolidate appendices into a short Python/terminology reference, activity hints, and references with dataset/code credits and any required AI-use disclosure. Introduce mathematics where it is needed rather than adding a mathematics chapter.

Exclude detailed hash collision handling, amortized analysis, linked-list and tree implementation, multiple sorting implementations, DFS/Dijkstra implementations, dynamic programming, backpropagation derivations, architecture surveys, and the three additional project builds. Further exploration should use a few selected links rather than new lessons. Cite the original sources of adapted diagrams, datasets, and code. Label invented scenarios and illustrative curves clearly; report only measured results as experimental findings.

## **Shared Plan for the Three Deliverables**

The following are proposed working limits, subject to any teacher-specified length or duration requirements.

| Deliverable | Suggested scope | Reuse plan |
| :---: | ----- | ----- |
|  **Study guide** | Approximately 30–40 pages total; most chapters 1–2 pages | Three sections per chapter, one worked problem, one small practice task |
|  **PPT** | Approximately 15–18 slides | Select key diagrams and examples; finish with the shared project |
|  **Videos** | Three focused tutorials of approximately 5–7 minutes each | 1: records and searching; 2: campus-map BFS; 3: neuron intuition and the flower project |

Videos demonstrate selected ideas rather than narrating all 18 chapters. The PPT summarizes the learning journey rather than copying the guide. Use the same terminology, datasets, diagrams, and verified outputs across all three.

## **Suggested One-Month Production Plan**

The team has one month to produce all three deliverables, with checks and revisions adding to the workload. To avoid relying on extra time, aim for complete first versions by the end of Week 3 and reserve Week 4 for review and revision. These are internal planning targets, not teacher-issued deadlines.

| Week | Main work | Completion checkpoint |
| :---: | ----- | ----- |
| **1** | Agree the reduced scope, prepare notebook templates, draft Parts I–II | Beginner examples work; common layout and terminology agreed |
| **2** | Draft Parts III–IV and complete the classifier notebook | Full core-content draft and usable diagrams; peer checks underway |
| **3** | Complete Parts V and the shared project; assemble PPT and record videos | First complete versions of all three deliverables |
| **4** | Review clarity and accuracy, rerun examples, edit recordings, revise and package | Checked guide, PPT, and videos ready for submission |

**Completion checks:** A teammate unfamiliar with each example can follow it; all supplied notebooks run from start to finish; activity hints match the examples; diagrams agree with scripts; measured results, sources, captions, and required AI-use disclosures are present.

**Quality priority:** Fix unclear explanations and broken examples before adding material. If time becomes tight, simplify presentation and use existing diagrams; do not add extra models, datasets, projects, or technical sections.

                            
                                                                                                                        \_***\_\_\_Team PentaByte***  
