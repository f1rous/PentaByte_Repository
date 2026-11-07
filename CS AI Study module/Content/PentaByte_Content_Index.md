# PentaByte Learning Content --- Index

> **Module:** Algorithms, Data Structures, and Connectionist AI\
> **Audience:** Beginning university students\
> **Language:** Python 3\
> **Coverage:** Units I--V, Chapters 1--18

This index is the navigation page for the Markdown learning materials in
the `Content` folder. The chapters follow one continuous learning
pathway: first understand and solve problems, then organize and process
data, then understand neural networks, and finally combine these ideas
in a practical project.

## How to use this folder

1.  Follow the units in numerical order, beginning with Unit I.
2.  Open the linked unit file for the main lesson content.
3.  In Unit I, use the separate chapter files when you need the expanded
    standalone versions of Chapters 1--3. The `Unit 1.md` file provides
    the consolidated Unit I version.
4.  Use the companion Python notebooks in the `Code` folder when a
    lesson includes a practical demonstration.
5.  Refer to the `Assets` folder for supporting chapter visuals.

## Unit overview

  ------------------------------------------------------------------------------------
  Unit             Focus                          Chapters Main content file
  ---------------- ----------------- --------------------- ---------------------------
  **Unit I**       Computational                      1--3 [Unit
                   Thinking and                            1.md](Unit-1/Unit%201.md)
                   Python                                  
                   Foundations                             

  **Unit II**      Core Data                          4--8 [Unit
                   Structures and                          2.md](Unit-2/Unit%202.md)
                   Problem-Solving                         
                   Algorithms                              

  **Unit III**     Connectionist AI:                 9--12 [Unit
                   Data, Neurons,                          3.md](Unit-3/Unit%203.md)
                   and Networks                            

  **Unit IV**      Connectionist AI:                13--16 [Unit
                   Learning,                               4.md](Unit-4/Unit%204.md)
                   Testing, and                            
                   Applications                            

  **Unit V**       Integration and                  17--18 [Unit
                   Practical Project                       5.md](Unit-5/Unit%205.md)
  ------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Unit I --- Computational Thinking and Python Foundations

**Learning pathway:** Problem → Algorithm → Python program → Efficiency
analysis

### Chapter 1 --- From Problems to Algorithms

Learn to turn an everyday task into a precise, testable computational
solution.

-   Computational thinking: decomposition, pattern recognition, and
    abstraction
-   Defining inputs, outputs, assumptions, and constraints
-   Modeling a real-world problem
-   Algorithms, programs, and control structures
-   Pseudocode, flowcharts, and algorithm tracing
-   Correctness, termination, and edge cases
-   Worked example: finding the largest value in a collection

**Files:** - [Consolidated Unit I content](Unit-1/Unit%201.md) -
[Expanded Chapter 1](Unit-1/Introductory%20Chapter/CHAPTER-1.md)

### Chapter 2 --- Essential Python for the Guide

Build the Python skills needed to read, modify, and test the examples in
the module.

-   Running Python scripts and notebooks
-   Variables, assignment, and basic data types
-   Operators, expressions, and type conversion
-   Input, output, and formatted results
-   Conditional statements and Boolean logic
-   `for` loops, `while` loops, and `range`
-   Functions, parameters, return values, and scope
-   Strings, indexing, slicing, and list operations
-   Imports, debugging, and assertions
-   Translating pseudocode into Python
-   Worked example: processing student scores

**Files:** - [Consolidated Unit I content](Unit-1/Unit%201.md) -
[Expanded Chapter 2](Unit-1/Introductory%20Chapter/CHAPTER-2.md)

### Chapter 3 --- Measuring Algorithm Efficiency

Understand how an algorithm's time and memory requirements change as its
input grows.

-   Input size and basic operation counts
-   Measured running time versus growth rate
-   Best-case, average-case, and worst-case analysis
-   Big-O notation and upper bounds
-   Common growth rates, including O(1), O(log n), O(n), O(n log n),
    O(n²), and O(2ⁿ)
-   Sequential loops, nested loops, and dependent loop bounds
-   Space complexity and time--space trade-offs
-   Small Python experiments and common analysis mistakes

**Files:** - [Consolidated Unit I content](Unit-1/Unit%201.md) -
[Expanded Chapter 3](Unit-1/Subsection%20Chapter/CHAPTER-3.md)

------------------------------------------------------------------------

## Unit II --- Core Data Structures and Problem-Solving Algorithms

**Learning pathway:** Store information → Choose a structure → Find and
sort records → Represent connections → Explore a route

**Main file:** [Unit 2.md](Unit-2/Unit%202.md)

### Chapter 4 --- Data Organization, Arrays, and Python Lists

-   Understand indexed collections, arrays, and Python lists.
-   Access, add, update, remove, and traverse list items.
-   Store simple student records and choose suitable update operations.

### Chapter 5 --- Stacks, Queues, Dictionaries, and Sets

-   Compare stack and queue behavior and recognize linked nodes.
-   Use dictionaries and sets; understand the basic idea of hashing.
-   Choose a data structure that fits a practical problem.

### Chapter 6 --- Trees, Heaps, and Graph Representations

-   Recognize trees as hierarchical structures and heaps as priority
    structures.
-   Represent graphs with vertices, edges, and adjacency lists.
-   Build and modify a simple campus-map representation.

### Chapter 7 --- Searching and Elementary Sorting

-   Trace linear search and binary search.
-   Trace insertion sort and use Python's built-in sorting.
-   Compare search operations and connect repeated halving with O(log
    n).

### Chapter 8 --- Graph Traversal and Shortest Paths

-   Explore a graph using breadth-first search (BFS), a queue, and
    visited locations.
-   Trace a BFS example and reconstruct a route.
-   Modify a connection and test an unreachable destination.

------------------------------------------------------------------------

## Unit III --- Connectionist AI: Data, Neurons, and Networks

**Learning pathway:** Fixed rules versus learned patterns → Samples and
features → Artificial neurons → Connected networks

**Main file:** [Unit 3.md](Unit-3/Unit%203.md)

### Chapter 9 --- AI, Machine Learning, and Connectionism

-   Compare fixed, rule-based decisions with systems that learn from
    examples.
-   Introduce machine learning and networks of connected artificial
    neurons.
-   Follow a classification task from measured features to a predicted
    label.

### Chapter 10 --- Learning from Data: Features, Labels, and Examples

-   Identify samples, numerical features, and species labels in the Iris
    dataset.
-   Distinguish training data from held-out test data.
-   Explain why useful measurements and careful data preparation matter.

### Chapter 11 --- Artificial Neurons: Weights, Bias, and Activation

-   Identify inputs, weights, and bias in an artificial neuron.
-   Calculate a weighted sum and apply an activation function such as
    ReLU.
-   Explain how changing a weight or bias changes the output.

### Chapter 12 --- Neural Network Layers and Forward Propagation

-   Identify input, hidden, and output layers in a feedforward network.
-   Trace values as they move through the network.
-   Interpret output scores and identify a predicted class.

------------------------------------------------------------------------

## Unit IV --- Connectionist AI: Learning, Testing, and Applications

**Learning pathway:** Prediction → Loss → Parameter updates → Training →
Evaluation → Responsible use

**Main file:** [Unit 4.md](Unit-4/Unit%204.md)

### Chapter 13 --- Prediction Error and Loss Functions

-   Compare a network's prediction with the correct target or label.
-   Understand loss as a numerical measure of prediction error.
-   Interpret a loss curve and explain why training loss alone is not
    enough.

### Chapter 14 --- How Neural Networks Learn: Gradient Descent and Backpropagation

-   Explain weights as adjustable connection strengths.
-   Understand gradient descent as a way to reduce loss.
-   Trace the training cycle: forward pass → loss → gradients → weight
    update → repeat.

### Chapter 15 --- Training a Simple Neural Network Classifier

-   Open the prepared Iris notebook and create training and held-out
    test data.
-   Scale features and run a supplied multilayer perceptron (MLP)
    classifier.
-   Make a controlled setting change and compare results using
    validation data.

### Chapter 16 --- Evaluating and Using Neural Networks Responsibly

-   Evaluate held-out predictions using accuracy, a confusion matrix,
    and a majority-class baseline.
-   Compare training and held-out results to discuss overfitting and
    unfamiliar data.
-   Explore applications, limitations, and responsible use.

------------------------------------------------------------------------

## Unit V --- Integration and Practical Project

**Learning pathway:** Describe and code a problem → Organize records →
Apply a trained model → Search and sort results → Explain the outcome

**Main file:** [Unit 5.md](Unit-5/Unit%205.md)

### Chapter 17 --- Connecting Data Structures, Algorithms, and AI

-   Store sample IDs, measurements, actual labels, and predictions as
    records.
-   Connect record lookup, sorting, and neural-network inference in one
    workflow.
-   Plan a results explorer and trace an individual sample through it.

### Chapter 18 --- Guided Project: Flower Prediction Explorer

-   **Build:** Store held-out predictions, find a sample by ID, and sort
    records by a measurement.
-   **Check:** Verify lookup, sorting, and classifier evaluation.
-   **Explain:** Demonstrate a prediction, search, sort, and limitation.

The project reuses the Iris dataset and the MLP classifier introduced in
Units III--IV. It brings together data structures, algorithms, and
connectionist AI in one guided notebook workflow.

------------------------------------------------------------------------

## Companion Python notebooks

The notebooks are stored outside this folder, in `Code/`.

  ------------------------------------------------------------------------------------------------
  Notebook                                                     Companion unit
  ------------------------------------------------------------ -----------------------------------
  [PentaByte Unit 01 Python                                    Unit I
  Notebook](../Code/PentaByte_Unit_01_Python_Notebook.ipynb)   

  [PentaByte Unit 02 Python                                    Unit II
  Notebook](../Code/PentaByte_Unit_02_Python_Notebook.ipynb)   

  [PentaByte Unit 03 Python                                    Unit III
  Notebook](../Code/PentaByte_Unit_03_Python_Notebook.ipynb)   

  [PentaByte Unit 04 Python                                    Unit IV
  Notebook](../Code/PentaByte_Unit_04_Python_Notebook.ipynb)   

  [PentaByte Unit 05 Python                                    Unit V
  Notebook](../Code/PentaByte_Unit_05_Python_Notebook.ipynb)   
  ------------------------------------------------------------------------------------------------

## Folder structure

``` text
Content/
├── index.md
├── Unit-1/
│   ├── Unit 1.md
│   ├── Introductory Chapter/
│   │   ├── CHAPTER-1.md
│   │   └── CHAPTER-2.md
│   └── Subsection Chapter/
│       └── CHAPTER-3.md
├── Unit-2/
│   └── Unit 2.md
├── Unit-3/
│   └── Unit 3.md
├── Unit-4/
│   └── Unit 4.md
└── Unit-5/
    └── Unit 5.md
```

## Editorial and navigation notes

-   Chapters are numbered continuously from 1 to 18 across the five
    units.
-   Unit I contains both a consolidated unit file and separate expanded
    chapter files. When revising overlapping material, keep the versions
    consistent.
-   Units II--V currently organize their chapter content inside one
    Markdown file per unit.
-   Use relative links in this index so navigation works in the
    repository and in a local copy.
-   Update this index whenever a unit, chapter, or file path is added,
    renamed, or removed.
