# Algorithms, Data Structures, and Connectionist AI

**Version**: V1.0

**Last updated**: 2026-10-22

**Overall status**: Outline only — content development in progress

## 2. Intended Learners

**Target audience**: Beginners studying algorithms, data structures, and connectionist AI.

The materials should define unfamiliar terminology, explain important steps clearly, and avoid assuming that learners already understand advanced computer science concepts.

The team's precise target audience and expected programming experience should be confirmed before the lessons are finalized.

## 3. Intended Learning Outcomes

At the end of the module, learners should be able to:

Define an algorithm and explain how it solves a computational problem.

Trace a simple algorithm and determine its output for a given input.

Explain the purpose of common searching and sorting algorithms.

Describe the purpose and basic operations of common data structures.

Compare data structures using their organization, operations, and relevant trade-offs.

Explain the basic idea of connectionist AI and how artificial neurons combine inputs.

Describe the roles of weights, biases, and activation functions in a basic artificial neuron.

Work through introductory examples and answer questions demonstrating their understanding.

Identify sources and explain the reasoning behind their solutions.

These outcomes are provisional and should be aligned with the team's final scope and the teacher's expectations.

## 4. Prerequisite Knowledge

The lessons should introduce concepts in an order that supports beginners.

Prerequisite

Expected knowledge

How the module will support learners

Basic mathematics

Arithmetic and comparisons

Explain calculations step by step

Basic logical reasoning

Following ordered instructions and simple conditions

Use traces, pseudocode, and diagrams

Basic computing concepts

Understanding inputs, outputs, and stored information

Define terminology when first introduced

Programming experience

Helpful, but the assumed level is not yet confirmed

Use language-independent examples where practical

The team should confirm whether a particular programming language or additional mathematical knowledge is required.

## A Beginner’s Guide to Problem-Solving and Neural Networks with Python

**Project book outline — revised draft**
**Audience:** Beginning university students
**Implementation language:** Python
**Scope:** Computational thinking, core algorithms and data structures, artificial neural networks, and practical integration

---

## Learning Objectives

By the end of the guide, readers should be able to:

1. Break a problem into smaller tasks and express a solution using pseudocode.
2. Write, trace, and test simple Python programs.
3. Compare algorithms using correctness, time complexity, and space complexity.
4. Select suitable data structures and explain their main operations.
5. Implement and compare fundamental searching, sorting, and graph algorithms.
6. Calculate the output of an artificial neuron and explain how neural networks learn.
7. Evaluate a simple classifier using data held out from training.
8. Combine algorithms, data structures, and neural networks in a small project while explaining limitations.

## Book Structure

| **Part** | **Focus**                                     | **Chapters** |
| -------- | --------------------------------------------- | ------------ |
| I        | Computational Thinking and Python Foundations | 1–3          |
| II       | Core Data Structures                          | 4–7          |
| III      | Algorithm Design and Problem-Solving          | 8–11         |
| IV       | Connectionist AI and Neural Networks          | 12–16        |
| V        | Integration and Practical Projects            | 17–18        |

## Standard Chapter Format

- Learning objectives and prerequisite concepts
- A motivating question or everyday example
- Key concepts and terminology
- Diagrams and step-by-step worked examples
- Pseudocode and Python implementation, where applicable
- Correctness checks, edge cases, and common mistakes
- Performance or model evaluation, where applicable
- Chapter summary and key terms
- Review questions and practical exercises
- References and further reading

**Optional extension** identifies material beyond the main beginner learning path.

---

# Part I — Computational Thinking and Python Foundations

## Chapter 1 — From Problems to Algorithms

- 1.1 Computational thinking: decomposition, pattern recognition, and abstraction
- 1.2 Defining a problem: inputs, outputs, assumptions, and constraints
- 1.3 Modeling a real-world problem
- 1.4 Algorithms and programs: their relationship
- 1.5 Sequence, selection, and repetition
- 1.6 Writing clear pseudocode
- 1.7 Flowcharts and standard symbols
- 1.8 Tracing an algorithm with a table
- 1.9 Correctness, termination, and edge cases
- 1.10 Worked example: finding the largest value in a collection

## Chapter 2 — Essential Python for the Guide

- 2.1 Running Python scripts and notebooks
- 2.2 Variables, assignment, and basic data types
- 2.3 Operators, expressions, and type conversion
- 2.4 Input, output, and formatted results
- 2.5 Conditional statements and Boolean logic
- 2.6 Loops: `for`, `while`, and `range`
- 2.7 Functions, parameters, return values, and scope
- 2.8 Strings, indexing, slicing, and basic list operations
- 2.9 Imports and standard-library modules
- 2.10 Errors, debugging, and simple assertions
- 2.11 Translating pseudocode into a working Python program
- 2.12 Worked example: processing a small set of student scores

## Chapter 3 — Measuring Algorithm Efficiency

- 3.1 Input size and basic operations
- 3.2 Measured running time versus growth rate
- 3.3 Best-case, average-case, and worst-case analysis
- 3.4 Big-O notation and upper bounds
- 3.5 Common growth rates: O(1), O(log n), O(n), O(n log n), O(n²), and O(2ⁿ)
- 3.6 Analyzing sequential loops and nested loops
- 3.7 Space complexity: input storage and auxiliary space
- 3.8 Time–space trade-offs
- 3.9 Comparing operation counts with small Python experiments
- 3.10 Common misconceptions about complexity

---

# Part II — Core Data Structures

## Chapter 4 — Data Organization, Arrays, and Python Lists

- 4.1 Data structures and abstract data types
- 4.2 Access, search, insertion, deletion, update, and traversal
- 4.3 Linear and non-linear structures
- 4.4 Objects, references, mutation, and copying in Python
- 4.5 Fixed-size arrays and dynamic arrays
- 4.6 Python lists as dynamic-array-based collections
- 4.7 List operations and their time costs
- 4.8 Resizing and amortized append cost: an intuitive introduction
- 4.9 Choosing between lists and tuples
- 4.10 Worked example: maintaining a collection of sensor readings

## Chapter 5 — Linked Lists, Stacks, and Queues

- 5.1 Minimal Python classes for nodes: `class`, `__init__`, and attributes
- 5.2 Singly linked lists: nodes and references
- 5.3 Traversal, search, insertion, and deletion
- 5.4 Arrays versus linked lists: costs and trade-offs
- 5.5 Stacks and the last-in, first-out principle
- 5.6 Stack operations and a Python list implementation
- 5.7 Queues and the first-in, first-out principle
- 5.8 Efficient queues and deques with `collections.deque`
- 5.9 Worked examples: balanced parentheses and a task queue
- 5.10 Optional extension: doubly linked lists, circular lists, and circular queues

## Chapter 6 — Hash Tables, Dictionaries, and Sets

- 6.1 Key–value storage and membership queries
- 6.2 Hash functions and table indices
- 6.3 Collisions and why they occur
- 6.4 Separate chaining and open addressing
- 6.5 Load factor and resizing
- 6.6 Average-case and worst-case operation costs
- 6.7 Python dictionaries, sets, and hashable keys
- 6.8 Worked examples: word frequencies and duplicate removal
- 6.9 Choosing between a list, dictionary, and set

## Chapter 7 — Trees, Heaps, and Graph Representations

- 7.1 Tree terminology: root, parent, child, leaf, depth, and height
- 7.2 Binary trees and binary search trees
- 7.3 Iterative search and insertion in a binary search tree
- 7.4 Balanced versus skewed trees and their performance
- 7.5 Min-heaps, max-heaps, and priority queues
- 7.6 Priority-queue operations with Python’s `heapq`
- 7.7 Graph terminology: vertices, edges, paths, cycles, and connectivity
- 7.8 Directed, undirected, weighted, and unweighted graphs
- 7.9 Adjacency lists and adjacency matrices
- 7.10 Comparing graph representations and storage costs
- 7.11 Worked example: representing a small campus map
- 7.12 Optional extension: binary search tree deletion

---

# Part III — Algorithm Design and Problem-Solving

## Chapter 8 — Searching and Elementary Sorting

- 8.1 Linear search: trace, implementation, and complexity
- 8.2 Binary search and the sorted-data requirement
- 8.3 Binary search boundaries, termination, and edge cases
- 8.4 Choosing between linear search, binary search, and hash-based lookup
- 8.5 Selection sort
- 8.6 Bubble sort and early termination
- 8.7 Insertion sort
- 8.8 Comparing best-case and worst-case behavior
- 8.9 Stability and in-place sorting
- 8.10 Python’s `sorted`, `list.sort`, and key functions
- 8.11 Worked example: searching and sorting student records

## Chapter 9 — Recursion and Divide and Conquer

- 9.1 Base cases, recursive cases, and progress toward termination
- 9.2 Tracing recursive calls and the call stack
- 9.3 Recursive and iterative solutions
- 9.4 Recursive processing of numbers, lists, and strings
- 9.5 Tree traversal: preorder, inorder, and postorder
- 9.6 Divide, solve, and combine
- 9.7 Merge sort: merging, recursion, and implementation
- 9.8 Quicksort: pivot selection, partitioning, and implementation
- 9.9 Comparing time complexity, auxiliary space, and stability
- 9.10 Recursion depth and common implementation mistakes
- 9.11 Optional extension: simple recurrence relations and heap sort

## Chapter 10 — Graph Traversal and Shortest Paths

- 10.1 Traversal, visited sets, and cycle handling
- 10.2 Breadth-first search using a queue
- 10.3 Reconstructing a path using predecessor records
- 10.4 Why BFS finds shortest paths by edge count in unweighted graphs
- 10.5 Depth-first search using recursion
- 10.6 Depth-first search using an explicit stack
- 10.7 Comparing BFS and DFS
- 10.8 Disconnected graphs and unreachable destinations
- 10.9 Traversal complexity with adjacency lists: O(V + E)
- 10.10 Worked example: finding a route across a campus map
- 10.11 Optional extension: Dijkstra’s algorithm for non-negative edge weights

## Chapter 11 — Algorithm Design Strategies

- 11.1 Brute force as a starting point and baseline
- 11.2 Recognizing divide-and-conquer problems
- 11.3 Greedy choices and the need to justify them
- 11.4 Worked greedy example: activity selection
- 11.5 Counterexample: when greedy coin selection fails
- 11.6 Repeated subproblems and overlapping work
- 11.7 Memoization and bottom-up dynamic programming
- 11.8 Worked dynamic-programming example: counting ways to climb stairs
- 11.9 Comparing correctness, time, and memory across approaches
- 11.10 Choosing a strategy from the problem’s constraints

---

# Part IV — Connectionist AI and Neural Networks

## Chapter 12 — AI, Machine Learning, and Connectionism

- 12.1 Artificial intelligence and its different approaches
- 12.2 Rule-based systems and learning from data
- 12.3 Relationships among AI, machine learning, and deep learning
- 12.4 Supervised, unsupervised, and reinforcement learning
- 12.5 Classification and regression
- 12.6 Connectionism and networks of interacting artificial neurons
- 12.7 Biological inspiration and the limits of the analogy
- 12.8 Features, labels, samples, and datasets
- 12.9 A machine-learning workflow: define, prepare, train, evaluate, and use
- 12.10 When a neural network is useful—and when simpler methods suffice

## Chapter 13 — Artificial Neurons and Forward Propagation

- 13.1 Essential notation: vectors, weighted sums, and functions
- 13.2 Inputs, weights, bias, and neuron output
- 13.3 Computing z = Σ(wᵢxᵢ) + b and a = f(z)
- 13.4 Activation functions: step, sigmoid, tanh, and ReLU
- 13.5 A fully worked numerical example of one neuron
- 13.6 The perceptron and linear decision boundaries
- 13.7 The XOR example and limitations of a single perceptron
- 13.8 Input, hidden, and output layers
- 13.9 Fully connected feedforward networks
- 13.10 Forward propagation through a small network
- 13.11 Output choices for regression and classification
- 13.12 Python implementation of a neuron and a small forward pass

## Chapter 14 — How Neural Networks Learn

- 14.1 Predictions, targets, and loss
- 14.2 Mean squared error and cross-entropy: introductory examples
- 14.3 Parameters, gradients, and the meaning of a derivative
- 14.4 Gradient descent and the learning rate
- 14.5 A numerical example of updating a parameter
- 14.6 Backpropagation as an efficient way to compute gradients
- 14.7 An intuitive chain-rule example
- 14.8 The training loop: forward pass, loss, gradients, and update
- 14.9 Epochs, batches, and iterations
- 14.10 Initialization and feature scaling
- 14.11 Common training problems and reading a loss curve
- 14.12 Optional extension: deriving and implementing a tiny network’s gradients

## Chapter 15 — Building and Evaluating a Simple Classifier

- 15.1 Selecting a small classification task and dataset
- 15.2 Essential NumPy arrays and shapes for the experiment
- 15.3 Inspecting features, labels, class balance, and missing values
- 15.4 Creating training, validation, and test splits
- 15.5 Preventing data leakage during preprocessing
- 15.6 Establishing a simple baseline
- 15.7 Training a small neural network with a Python library
- 15.8 Choosing settings using validation data
- 15.9 Underfitting, overfitting, and generalization
- 15.10 Accuracy, confusion matrices, precision, and recall
- 15.11 Evaluating the final model on the held-out test set
- 15.12 Reproducibility: random seeds, dependencies, and recorded results
- 15.13 Worked experiment: classifying Iris flowers with a small multilayer perceptron

## Chapter 16 — Deep Learning, Applications, and Responsible Use

- 16.1 Shallow and deep neural networks
- 16.2 Convolutional neural networks and image data
- 16.3 Recurrent neural networks and sequential data
- 16.4 LSTMs: an introductory overview
- 16.5 Attention and transformers: an introductory overview
- 16.6 Comparing architectures by input type, task, and limitations
- 16.7 Applications in language, speech, recommendation, and time-series analysis
- 16.8 Case studies: medical imaging and autonomous vehicles
- 16.9 Data quality, bias, fairness, and privacy
- 16.10 Explainability, reliability, and distribution shift
- 16.11 Computational costs, environmental considerations, and human oversight
- 16.12 Responsible reporting of capabilities and limitations

---

# Part V — Integration and Practical Projects

## Chapter 17 — Connecting Data Structures, Algorithms, and AI

- 17.1 Turning a practical problem into a system specification
- 17.2 Choosing representations for records, relationships, and numerical features
- 17.3 Using search, sorting, and queues in data-processing workflows
- 17.4 Preparing inputs for a neural network
- 17.5 Separating model predictions from rule-based decisions
- 17.6 Comparing a non-ML baseline with an ML-assisted approach
- 17.7 Assessing runtime, memory, predictive quality, and failure cases
- 17.8 Worked system design: classifying and organizing sensor readings
- 17.9 Testing individual components and the complete workflow
- 17.10 Documenting assumptions, limitations, and possible improvements

## Chapter 18 — Practical Projects

### Project A — Searchable Student Record Manager

- Define the record format and supported queries.
- Store records using lists and dictionaries.
- Implement linear search and binary search on appropriately sorted data.
- Sort records by a selected field.
- Compare operation costs and include the cost of preparing sorted data.
- Test empty input, duplicate values, and missing records.

### Project B — Campus Route Finder

- Represent locations and connections using an adjacency list.
- Implement BFS and reconstruct a route.
- Implement DFS and compare traversal behavior.
- Handle disconnected locations and invalid inputs.
- Explain shortest paths by number of edges versus physical distance.
- Optional extension: weighted routes using Dijkstra’s algorithm.

### Project C — Beginner Neural Network Classifier

- Define the classification task and document the dataset source.
- Inspect features and labels.
- Split the data and fit preprocessing using training data only.
- Train a small neural network and compare it with a baseline.
- Use validation data to select settings.
- Evaluate once on the held-out test set and discuss errors.

### Project D — Sensor Monitoring System: Optional Integration Challenge

- Use a documented public or clearly labeled synthetic sensor dataset.
- Store readings in a bounded queue and summarize them by sensor ID.
- Implement a threshold-based baseline for identifying unusual readings.
- Train a small classifier if suitable labeled data are available.
- Combine storage, processing, and prediction in one workflow.
- Compare the baseline and classifier on held-out data.
- Report false alarms, missed cases, runtime, and limitations.

### Common Project Deliverables

- Problem statement and scope
- System diagram and choice of data structures
- Algorithm pseudocode and Python source code
- Setup instructions and dependency versions
- Test cases, expected behavior, and actual results
- Complexity analysis and model evaluation, where relevant
- Dataset and reference acknowledgments
- Limitations and improvement ideas
- Short demonstration or tutorial outline
- Contribution record and AI-assistance disclosure, where required

---

# Appendices

## Appendix A — Python Quick Reference

- Syntax, types, conditions, loops, and functions
- Lists, tuples, dictionaries, and sets
- Minimal classes and objects
- `collections.deque` and `heapq`
- NumPy array and shape essentials
- Running examples and installing required packages

## Appendix B — Pseudocode and Diagram Conventions

- Pseudocode notation
- Flowchart symbols
- Trace tables
- Tree and graph notation
- Neural-network diagram conventions

## Appendix C — Mathematical Essentials

- Exponents and logarithms
- Summation notation
- Vectors, dot products, and matrix dimensions
- Functions, slopes, and derivatives
- Basic probability notation used in classification

## Appendix D — Algorithm and Data Structure Reference Tables

- Searching and sorting complexity
- List, linked-list, stack, and queue operations
- Hash table, tree, and heap operations
- Graph representation and traversal costs
- Assumptions, average-case costs, and worst-case costs

## Appendix E — Glossary

- Computational thinking and algorithm terminology
- Data structure terminology
- Neural-network and model-evaluation terminology

## Appendix F — Exercise Hints and Selected Solutions

- Concept questions
- Algorithm traces
- Python programming exercises
- Numerical neuron and training examples
- Integrated project challenges

## Appendix G — References and Attribution

- Books, research papers, and official documentation
- Dataset and image credits
- Code sources and licenses
- AI-use statement and contributor acknowledgments
