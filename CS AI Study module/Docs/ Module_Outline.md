# Module Outline — Algorithms, Data Structures & Connectionist AI

**Version:** V1.0  
**Last updated:** 2026-10-21  
**Overall status:** Outline only — content development in progress

## 1. Module Purpose

This module introduces learners to fundamental concepts in algorithms, data structures, and connectionist artificial intelligence.

The learning materials will progress from basic computational problem-solving to ways of organizing data and introductory neural-network concepts. Explanations, worked examples, visual demonstrations, and learner activities will be used to help beginners apply the concepts.

## 2. Intended Learners

**Target audience:** Beginners studying algorithms, data structures, and connectionist AI.

The materials should define unfamiliar terminology, explain important steps clearly, and avoid assuming that learners already understand advanced computer science concepts.

The team's precise target audience and expected programming experience should be confirmed before the lessons are finalized.

## 3. Intended Learning Outcomes

By the end of the module, learners should be able to:

1. Define an algorithm and explain how it solves a computational problem.
2. Trace a simple algorithm and determine its output for a given input.
3. Explain the purpose of common searching and sorting algorithms.
4. Describe the purpose and basic operations of common data structures.
5. Compare data structures using their organization, operations, and relevant trade-offs.
6. Explain the basic idea of connectionist AI and how artificial neurons combine inputs.
7. Describe the roles of weights, biases, and activation functions in a basic artificial neuron.
8. Work through introductory examples and answer questions demonstrating their understanding.
9. Identify sources and explain the reasoning behind their solutions.

These outcomes are provisional and should be aligned with the team's final scope and the teacher's expectations.

## 4. Prerequisite Knowledge

The lessons should introduce concepts in an order that supports beginners.

| Prerequisite | Expected knowledge | How the module will support learners |
|---|---|---|
| Basic mathematics | Arithmetic and comparisons | Explain calculations step by step |
| Basic logical reasoning | Following ordered instructions and simple conditions | Use traces, pseudocode, and diagrams |
| Basic computing concepts | Understanding inputs, outputs, and stored information | Define terminology when first introduced |
| Programming experience | Helpful, but the assumed level is not yet confirmed | Use language-independent examples where practical |

The team should confirm whether a particular programming language or additional mathematical knowledge is required.

## 5. Learning Sequence and Development Status

The following is a proposed sequence. All sections are marked `Outline only` until actual content has been developed and checked.

### Unit 1 — Algorithm Fundamentals

**Status:** Outline only

**Learning outcomes**
- Define an algorithm.
- Identify inputs, processing steps, and outputs.
- Trace a simple algorithm in execution order.
- Represent an algorithm using pseudocode or a flowchart.

**Planned subtopics**
1. What is an algorithm?
2. Inputs, processing, and outputs.
3. Sequence, selection, and repetition.
4. Pseudocode and flowcharts.
5. Correctness and simple algorithm tracing.

**Planned example:** Trace an algorithm that finds the largest number in a list.

**Learner activity:** Given a list of numbers, record the current largest value after each comparison.

**Expected outcome:** The learner can explain the steps and determine the correct output.

### Unit 2 — Searching and Sorting Algorithms

**Status:** Outline only

**Learning outcomes**
- Explain the purpose of searching and sorting.
- Trace basic searching and sorting algorithms.
- Compare approaches by their assumptions and behavior.
- Interpret introductory time-complexity descriptions.

**Planned subtopics**
1. Linear search.
2. Binary search and its sorted-input requirement.
3. Basic sorting methods.
4. Comparing algorithm behavior.
5. Introduction to time complexity and Big O notation.

**Planned example:** Compare linear search and binary search on a suitable list.

**Learner activity:** Trace each search method and compare the number of comparisons in the example.

**Expected outcome:** The learner can trace both methods and explain why binary search requires sorted input.

### Unit 3 — Data Structure Fundamentals

**Status:** Outline only

**Learning outcomes**
- Explain what a data structure is.
- Describe how data can be organized.
- Identify common data structures and their basic operations.
- Choose an appropriate structure for a simple problem.

**Planned subtopics**
1. Introduction to data structures.
2. Arrays and lists.
3. Linked lists.
4. Stacks.
5. Queues.
6. Comparing structures and their trade-offs.

**Planned example:** Demonstrate how a stack and a queue handle a sequence of items differently.

**Learner activity:** Determine the removal order for items added to a stack and a queue.

**Expected outcome:** The learner can explain the difference between last-in, first-out and first-in, first-out behavior.

### Unit 4 — Trees, Graphs, and Data Organization

**Status:** Outline only

**Learning outcomes**
- Describe the basic structure of trees and graphs.
- Identify nodes, edges, roots, and leaves where applicable.
- Recognize simple situations in which trees or graphs are useful.

**Planned subtopics**
1. Tree terminology and structure.
2. Basic tree traversal concepts.
3. Graphs, vertices, and edges.
4. Simple graph representations.
5. Introductory applications.

**Planned example:** Represent a small network of connected locations as a graph.

**Learner activity:** Identify the nodes and edges in a supplied diagram.

**Expected outcome:** The learner can interpret a simple tree or graph and describe its connections.

### Unit 5 — Introduction to Connectionist AI

**Status:** Outline only

**Learning outcomes**
- Explain the basic idea of connectionist AI.
- Describe the role of artificial neurons in a neural network.
- Identify inputs, weights, bias, and activation functions.
- Work through a simple artificial-neuron calculation.

**Planned subtopics**
1. Introduction to connectionist AI.
2. Biological inspiration and artificial neurons.
3. Inputs and weights.
4. Bias and weighted sums.
5. Activation functions.
6. Basic neural-network structure.

**Planned example:** Calculate the weighted sum of a single artificial neuron using small numerical inputs.

**Learner activity:** Given inputs, weights, and a bias, calculate the neuron's weighted sum and apply a specified activation function.

**Expected outcome:** The learner can perform the calculation and explain the role of each component.

### Unit 6 — Neural Network Learning and Applications

**Status:** Outline only

**Learning outcomes**
- Explain at an introductory level how a neural network adjusts its parameters during learning.
- Distinguish training from inference.
- Identify examples of problems to which connectionist AI can be applied.
- Recognize basic limitations and the importance of evaluating results.

**Planned subtopics**
1. Training data and model predictions.
2. Loss or error as a measure of prediction quality.
3. Introductory parameter adjustment.
4. Training versus inference.
5. Applications, limitations, and responsible use.

**Planned example:** Use a small conceptual example to explain how a model prediction can be compared with an expected result.

**Learner activity:** Explain the difference between training a model and using an already trained model to make a prediction.

**Expected outcome:** The learner can describe the basic learning process without assuming advanced mathematical knowledge.

## 6. Status Definitions

Use the following labels consistently throughout the repository.

| Status | Meaning |
|---|---|
| Outline only | Scope and planned learning activities are identified, but substantive lesson content is not yet complete. |
| Drafted | A substantive first draft exists. |
| Peer reviewed | Another team member has reviewed the material and the outcome has been recorded. |
| Checked | Relevant explanations, examples, answers, sources, and file references have been verified. |
| Needs revision | A known issue or gap requires further work. |

A section should not be marked peer reviewed or checked until the corresponding work has actually taken place.

## 7. Review and Quality Assurance Plan

Each developed section should be reviewed for:

- Accuracy of definitions, claims, calculations, and examples.
- Clarity for the intended beginner audience.
- Correctness of practice questions and explained answers.
- Suitability and readability of diagrams and other visuals.
- Validity and attribution of sources.
- Functionality of relative links and supporting assets.

Record at least one concrete review outcome in `docs/review-log.md`, identifying what was checked, what was found, and what was corrected or confirmed.

## 8. Planned Use in the Final Learning Resources

**Study guide:** The Markdown lessons will provide the explanations, terminology, worked examples, activities, answers, and references.

**Presentation slides:** Important concepts, algorithm traces, comparison tables, diagrams, and neural-network calculations can be adapted into visual slides.

**Video tutorials:** Selected lessons can become focused demonstrations showing a worked algorithm, a data structure operation, or an artificial-neuron calculation.

The Markdown content is the shared foundation; producing all three finished resources is not required for this Stage 1 assignment.

## 9. Current Gaps and Next Actions

The following items must be resolved as development proceeds:

- Confirm the team's final module scope and whether all proposed units are required.
- Confirm individual responsibilities and allocate sections.
- Identify reliable references for each topic.
- Develop substantive Markdown content rather than leaving sections at outline level.
- Add and verify diagrams, worked examples, activities, and explained answers.
- Conduct and document peer review.
- Update section statuses based on actual progress.
- Prepare repository evidence, the content PDF, the submission report, and the final ZIP.

## 10. References

Add the sources actually consulted for the module and its lesson content. Each entry should identify the author or organization, title, URL or publication details, and access date where applicable.

Do not treat this outline as a completed bibliography. Verify each source and connect it to the relevant learning material.
