Research of 吳宜展

Algorithms, Data Structures & Connectionist AI

	Algorithms  
Definition:   
An Algorithm is a set of step-by-step instructions for solving a problem or completing a task, similar to a recipe. In computing, algorithms tell a computer how to process inputs such as data to produce an output, such as a decision, prediction, or sorted list. Some algorithms are simple and fixed, while others “learn” patterns from data, as in machine learning.  
[https\://hai.stanford.edu/ai-definitions/what-is-an-algorithm](https://hai.stanford.edu/ai-definitions/what-is-an-algorithm) 

Core topics: 

- Analysis & Complexity

	Metrics : Time, Space Complexity

[https\://www\.geeksforgeeks.org/dsa/analysis-of-algorithms/](https://www.geeksforgeeks.org/dsa/analysis-of-algorithms/)   
Time  
Instructions take time.  
How fast does the algorithm perform?  
What affects its runtime?

Space  
Data structures take space  
What kind of data structures can be used?  
How does choice of data structure affect the runtime?  
[https\://www\.geeksforgeeks.org/dsa/complete-guide-on-complexity-analysis/](https://www.geeksforgeeks.org/dsa/complete-guide-on-complexity-analysis/) 

	Cases :   
Worst-Case (O): The maximum number of steps an algorithm can take; used most often to guarantee an upper bound.  
Best-Case (Ω): The minimum number of steps for the most favorable input.  
Average-Case (Θ): The expected number of steps across all possible random inputs.  
Amortized: The average cost per operation over a sequence of multiple operations.

- Algorithmic Paradigms \- common concepts and ideas behind algorithm design patterns.

Divide and Conquer Algorithms  
breaks down a problem into smaller subproblems (solved independently)  (divide), recursively solves each subproblem (conquer), and then combines the result of each subproblem to form the overall solution.

Brute-Force Algorithms  
A brute-force algorithm solves combinatorial problems by systematically enumerating all potential solutions in order to identify the best candidate solution.

Greedy Algorithms  
A greedy algorithm solves combinatorial problems by repeatedly applying a simple rule to select the next element to include in the solution.

Reduction Algorithms  
Rather than solve the problem directly, a reduction algorithm solves problems by transforming them into other problems

[https\://openstax.org/books/introduction-computer-science/pages/3-4-algorithmic-paradigms](https://openstax.org/books/introduction-computer-science/pages/3-4-algorithmic-paradigms) 

- Core Problem Domains

Algorithm core problem domains encompass the foundational categories of computational challenges that algorithms are designed to solve

- \++

	Data Structures  
Definition  
A data structure is a way of organizing and storing data in a computer so that it can be accessed and used efficiently. It refers to the logical or mathematical representation of data, as well as the implementation in a computer program.

Core topics:

- Foundation  
1. Abstract Data Types (ADTs)

Abstract Data Type (ADT) is a conceptual model. They define what a data structure does without dictating how it does it. By separating the logical properties from the physical implementation, ADTs allow for cleaner, more maintainable code.  
[https\://www\.geeksforgeeks.org/dsa/abstract-data-types/](https://www.geeksforgeeks.org/dsa/abstract-data-types/) 

Differences Between ADTs and UDTs  
Advantages  
Modularity: Simplifies complex systems by breaking them into smaller, manageable pieces.  
Security & Integrity: Information hiding prevents unauthorized or accidental modification of internal data.  
Reusability: Once defined, the interface can be reused across different projects regardless of the backend logic.  
Disadvantages  
Performance Overhead: The layers of abstraction can sometimes lead to slightly higher memory or CPU usage.  
Initial Complexity: Designing a robust ADT requires more upfront planning and a steeper learning curve for beginners.

2. Linear vs Non-linear

Linear  
A linear data structure is a data structure in which elements are arranged sequentially, one after another.  
Array  
An array is a collection of elements of the same data type stored in contiguous memory locations. It allows efficient access to elements using an index.  
String  
A string is a sequence of characters arranged in a linear order. It is used to represent and process text, with operations such as accessing, searching, comparing, and modifying characters.  
Linked List  
A linked list is a linear data structure in which elements are stored as nodes, and each node contains data and a reference to the next node.  
Stack  
A stack is a linear data structure that follows the LIFO (Last In, First Out) principle. It allows elements to be added and removed only from one end, called the top.  
Queue  
A queue is a linear data structure that follows the FIFO (First In, First Out) principle. It allows elements to be inserted from one end, called the rear, and removed from the other end, called the front.

Non-linear  
Data structures where data elements are not placed sequentially or linearly are called non-linear data structures.  
Hash Table  
A hash table is a data structure that uses a hash function to map keys to positions, enabling efficient insertion, deletion, and search.  
Tree  
A tree is a non-linear, hierarchical data structure consisting of nodes connected through edges. It organizes data in a parent-child relationship, where each node can have zero or more child nodes.  
Heap  
A heap is a specialized tree-based data structure that satisfies the heap property between parent and child nodes. It is commonly used for implementing priority queues and performing heap sort.  
Graph  
A graph is a non-linear data structure consisting of vertices (nodes) and edges. It represents relationships or connections between different nodes.

[https\://www\.geeksforgeeks.org/dsa/data-structure-meaning/](https://www.geeksforgeeks.org/dsa/data-structure-meaning/) 

1. Hash-based

Hashing is a technique used in data structures that efficiently stores and retrieves data in a way that allows for quick access.

[https\://www\.geeksforgeeks.org/dsa/hashing-data-structure/](https://www.geeksforgeeks.org/dsa/hashing-data-structure/) 

- \++

	  
	Connectionist AI  
Definition  
Connectionist AI, also known as neural networks or sub-symbolic AI, represents knowledge through connections and weights within a network of artificial neurons. It is inspired by the structure and functioning of the human brain.

[https\://www\.geeksforgeeks.org/artificial-intelligence/difference-between-symbolic-and-connectionist-ai/](https://www.geeksforgeeks.org/artificial-intelligence/difference-between-symbolic-and-connectionist-ai/) 

Core topics:

- Fundamentals  
- Major Architechtural Families  
1. Feedforward Networks (MLPs)  
2. Convolutional Neural Networks (CNNs)  
3. Recurrent Neural Networks (RNNs)

Deep Learning Models

Models in Connectionist AI

Generative Adversarial Networks

Transfer Learning

Feedforward Neural Networks (FNN)

Feedforward Neural Networks (FNN) are the simplest type of artificial neural network architecture where data flows in one direction from input to output without any cycles or feedback loops. This design is effective for tasks such as classification and regression, where the relationship between input features and outputs is direct and does not require memory of previous inputs.

Recurrent Neural Networks (RNN)

Types of Architecture

Understanding Connectionist AI

Recurrent Neural Networks (RNN) are designed to work with sequential data by incorporating feedback loops in their architecture. This allows the network to maintain a form of memory, making it suitable for tasks such as time series prediction and natural language processing, where the context of previous inputs is crucial for understanding current data.

Convolutional Neural Networks (CNN)

Convolutional Neural Networks (CNN) are specifically designed for processing structured grid data such as images. They utilize convolutional layers to automatically detect and learn features in images, enabling tasks like image recognition and classification. CNNs are particularly powerful due to their ability to capture spatial hierarchies in data.

Exploring the Architecture and Models of Neural Networks

Neurons: Basic Units of Processing

Neurons are the fundamental building blocks of a neural network, functioning as the primary units of information processing. Each neuron receives input, processes it, and passes on the output to other neurons in the network.

Layers: Input, Hidden, and Output Layers

Basic Architecture of Neural Network

A neural network consists of various layers: the input layer receives the initial data, hidden layers perform calculations and feature extraction, and the output layer delivers the final results. Each layer plays a critical role in transforming inputs into outputs.

Weights: Connections Between Neurons

Weights are numerical values assigned to the connections between neurons. They determine the strength and influence of input signals. During the learning process, these weights are adjusted to minimize the error in outputs, enabling the network to learn from data.

Understanding Connectionist AI: Mimicking Human Intelligence

Connectionist AI refers to a branch of artificial intelligence that utilizes neural networks to process information similarly to the human brain. This approach is significant as it allows machines to learn from data patterns and improve decision-making through experience, leading to advancements in various AI applications such as image recognition and natural language processing.

Connectionist AI: Architecture & Models

This presentation delves into the foundational aspects of Connectionist AI, exploring its architecture and various models. It aims to provide a comprehensive understanding of how neural networks function and their different types, including Feedforward, Recurrent, and Convolutional Neural Networks.

[https\://prezi.com/p/zexn-vbxhsui/understanding-connectionist-ai/](https://prezi.com/p/zexn-vbxhsui/understanding-connectionist-ai/) 

4. Transformers & Attention

[https\://www\.d2l.ai/chapter\_attention-mechanisms-and-transformers/index.html](https://www.d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)   
[https\://cs231n.stanford.edu/slides/2025/lecture\_8.pdf](https://cs231n.stanford.edu/slides/2025/lecture_8.pdf) 

- Learning Paradigms & Techniques  
- \++

Part 1: Algorithms  
Description: Algorithms are finite, step-by-step procedures for solving computational problems, and they are the core of computer science. They are typically classified by their design paradigm (e.g., divide-and-conquer, dynamic programming) or their problem domain (e.g., sorting, searching, graph traversal). The efficiency of an algorithm is analyzed using asymptotic notations (Big-O), which describe how its runtime or memory requirements scale with input size, a critical factor in AI for handling large datasets.

Important Topics to Explore:

Sorting Algorithms: Bubble, Selection, Merge, Quick Sort.  
Sorting refers to rearrangement of a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of elements in the respective data structure.   
[https\://www\.geeksforgeeks.org/dsa/sorting-algorithms/](https://www.geeksforgeeks.org/dsa/sorting-algorithms/)   
[https\://www\.geeksforgeeks.org/dsa/introduction-to-sorting-algorithm/](https://www.geeksforgeeks.org/dsa/introduction-to-sorting-algorithm/) 

Sorting Basics  
In-place Sorting: An in-place sorting algorithm uses constant space for producing the output (modifies the given array only. Examples: Selection Sort, Bubble Sort, Insertion Sort and Heap Sort.  
Internal Sorting: Internal Sorting is when all the data is placed in the main memory or internal memory. In internal sorting, the problem cannot take input beyond allocated memory size.  
External Sorting : External Sorting is when all the data that needs to be sorted need not to be placed in memory at a time, the sorting is called external sorting. External Sorting is used for the massive amount of data. For example Merge sort can be used in external sorting as the whole array does not have to be present all the time in memory,  
Stable sorting: When two same items appear in the same order in sorted data as in the original array called stable sort. Examples: Merge Sort, Insertion Sort, Bubble Sort.  
Hybrid Sorting: A sorting algorithm is called Hybrid if it uses more than one standard sorting algorithms to sort the array. The idea is to take advantages of multiple sorting algorithms. For Example IntroSort uses Insertions sort and Quick Sort. 

Types of Sorting Techniques  
There are various sorting algorithms are used in data structures. The following two types of sorting algorithms can be broadly classified:

Comparison-based: We compare the elements in a comparison-based sorting algorithm)  
Non-comparison-based: We do not compare the elements in a non-comparison-based sorting algorithm)

![][image1]

Searching Algorithms: Linear Search, Binary Search.  
Searching Algorithms  
Last Updated :  
3 Mar, 2026  
Searching algorithms are essential tools in computer science used to locate specific items within a collection of data. In this tutorial, we are mainly going to focus upon searching in an array. When we search an item in an array, there are two most common algorithms used based on the type of input array.

Linear Search : It is used for an unsorted array. It mainly does one by one comparison of the item to be search with array elements. It takes linear or O(n) Time.  
Binary Search : It is used for a sorted array. It mainly compares the array's middle element first and if the middle element is same as input, then it returns. Otherwise it searches in either left half or right half based on comparison result (Whether the mid element is smaller or greater). This algorithm is faster than linear search and takes O(Log n) time.

[https\://www\.geeksforgeeks.org/dsa/searching-algorithms/](https://www.geeksforgeeks.org/dsa/searching-algorithms/) 

Graph Algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra’s Shortest Path, Minimum Spanning Trees (Prim, Kruskal).

Graph is a non-linear data structure like tree data structure. A Graph is composed of a set of vertices(V) and a set of edges(E). The vertices are connected with each other through edges.

The limitation of tree is, it can only represent hierarchical data. For situations where nodes or vertices are randomly connected with each other other, we use Graph.  
Example situations where we use graph data structure are, a social network, a computer network, a network of locations used in GPS and many more examples where different nodes or vertices are connected without any hierarchic or constraint on structure.  
The following images show different types of graphs that see when solving graph problems.

[https\://www\.geeksforgeeks.org/dsa/graph-data-structure-and-algorithms/](https://www.geeksforgeeks.org/dsa/graph-data-structure-and-algorithms/) 

Algorithm Design Paradigms: Divide and Conquer, Dynamic Programming, Greedy Algorithms, Backtracking.  
Classification by Design Method: There are primarily three main categories into which an algorithm can be named in this type of classification. They are:   
 

Greedy Method: In the greedy method, at each step, a decision is made to choose the local optimum, without thinking about the future consequences.   
Example: Fractional Knapsack, Activity Selection.  
Divide and Conquer: The Divide and Conquer strategy involves dividing the problem into sub-problem, recursively solving them, and then recombining them for the final answer.   
Example: Merge sort, Quicksort.  
Dynamic Programming: The approach of Dynamic programming is similar to divide and conquer. The difference is that whenever we have recursive function calls with the same result, instead of calling them again we try to store the result in a data structure in the form of a table and retrieve the results from the table. Thus, the overall time complexity is reduced. "Dynamic" means we dynamically decide, whether to call a function or retrieve values from the table.   
Example: 0-1 Knapsack, subset-sum problem.  
Linear Programming: In Linear Programming, there are inequalities in terms of inputs and maximizing or minimizing some linear functions of inputs.   
Example: Maximum flow of Directed Graph  
Reduction(Transform and Conquer): In this method, we solve a difficult problem by transforming it into a known problem for which we have an optimal solution. Basically, the goal is to find a reducing algorithm whose complexity is not dominated by the resulting reduced algorithms.   
Example: Selection algorithm for finding the median in a list involves first sorting the list and then finding out the middle element in the sorted list. These techniques are also called transform and conquer.  
Backtracking: This technique is very useful in solving combinatorial problems that have a single unique solution. Where we have to find the correct combination of steps that lead to fulfillment of the task.  Such problems have multiple stages and there are multiple options at each stage. This approach is based on exploring each available option at every stage one-by-one. While exploring an option if a point is reached that doesn't seem to lead to the solution, the program control backtracks one step, and starts exploring the next option. In this way, the program explores all possible course of actions and finds the route that leads to the solution.    
Example: N-queen problem, maize problem.  
Branch and Bound: This technique is very useful in solving combinatorial optimization problem that have multiple solutions and we are interested in find the most optimum solution. In this approach, the entire solution space is represented in the form of a state space tree. As the program progresses each state combination is explored, and the previous solution is replaced by new one if it is not the optimal than the current solution.   
Example: Job sequencing, Travelling salesman problem.

Classification by Design Approaches : There are two approaches for designing an algorithm. these approaches include 

Top-Down Approach :  
Bottom-up approach  
Top-Down Approach: In the top-down approach, a large problem is divided into small sub-problem. and keep                repeating the process of decomposing problems until the complex problem is solved.  
Bottom-up approach: The bottom-up approach is also known as the reverse of top-down approaches.  
In approach different, part of a complex program is solved using a programming language and then this is combined into a complete program.

[https\://www\.geeksforgeeks.org/dsa/algorithms-design-techniques/](https://www.geeksforgeeks.org/dsa/algorithms-design-techniques/) 

Part 2: Data Structures  
Description: A data structure is a specialized format for organizing, processing, retrieving, and storing data. The choice of data structure profoundly impacts an algorithm's efficiency, speed, and memory usage. Data structures are broadly categorized into linear (elements arranged sequentially) and non-linear (elements arranged hierarchically or in interconnected networks), providing different trade-offs for operations like insertion, deletion, and access.

Important Topics to Explore:

Linear Data Structures: Arrays, Linked Lists (Singly, Doubly), Stacks (LIFO), Queues (FIFO).

[https\://www\.geeksforgeeks.org/dsa/introduction-to-linear-data-structures/](https://www.geeksforgeeks.org/dsa/introduction-to-linear-data-structures/) 

Key Operations & Analysis: Time and Space Complexity for access, insertion, deletion, and search.

[https\://www\.geeksforgeeks.org/dsa/time-complexity-and-space-complexity/](https://www.geeksforgeeks.org/dsa/time-complexity-and-space-complexity/) 

Application Contexts: When to use arrays vs. linked lists, stacks for function calls, trees for hierarchical data, and graphs for network modeling.

Important Topics to Explore:

Core Components: Neurons (Nodes), Weights, Biases, Activation Functions (ReLU, Sigmoid, Softmax).

[https\://www\.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/](https://www.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/) 

Network Architectures: Feedforward Neural Networks (FNNs), Convolutional Neural Networks (CNNs) for vision, Recurrent Neural Networks (RNNs/LSTMs) for sequential data.

Learning Process: Forward Propagation, Backpropagation, Gradient Descent.

[https\://www\.geeksforgeeks.org/deep-learning/neural-networks-a-beginners-guide/](https://www.geeksforgeeks.org/deep-learning/neural-networks-a-beginners-guide/) 

Learning Paradigms: Supervised Learning (Classification, Regression), Unsupervised Learning (Clustering, Dimensionality Reduction), Reinforcement Learning.

[https\://www\.geeksforgeeks.org/machine-learning/types-of-machine-learning/](https://www.geeksforgeeks.org/machine-learning/types-of-machine-learning/) 

Part 4: Limitations, Blindspots, and Directions for Comprehensive Research  
Your prompt and the provided materials cover the fundamentals well, but a comprehensive research plan should acknowledge the following blindspots and limitations to provide a more critical and well-rounded perspective:

Scalability and "Toy Problems": Both algorithmic solutions and connectionist models are often tested on simplified or "toy" problems. A critical limitation is that performance can degrade significantly when scaling to real-world complexity, where factors like data noise, non-stationarity, and edge cases are prevalent.

The "Black Box" Problem in Connectionist AI: Unlike traditional algorithms whose logic is transparent, deep neural networks are often criticized as "black boxes." Their internal decision-making processes are not easily interpretable, which is a major barrier to adoption in high-stakes domains like healthcare and finance. Research Direction: Investigate Explainable AI (XAI) methods (e.g., LIME, SHAP) as a counter-trend.

Bias and Fairness: Algorithms and AI models are not neutral; they can inherit and amplify biases present in their training data or design. This is a critical sociotechnical limitation, especially for connectionist models trained on large, potentially uncurated datasets. Research Direction: Explore the field of Fairness in AI and algorithmic auditing.

Data Dependency and Generalization: Connectionist AI is highly dependent on large volumes of high-quality, labeled data. A primary failure mode is "poor generalization"—the inability to perform well on data outside its training distribution—which raises questions about robustness and reliability. Research Direction: Examine techniques like transfer learning, data augmentation, and the study of out-of-distribution generalization.

The Symbolic-Connectionist Divide: The provided materials focus heavily on connectionist AI. A comprehensive study should contrast it with Symbolic AI (rule-based, logic-driven systems). This comparison is essential for understanding the trade-offs between interpretability (symbolic) and adaptability (connectionist) and the emerging field of Neuro-Symbolic AI, which aims to integrate both.

PPT Draft :   
[https\://www\.canva.com/design/DAHYu1vbOjY/KSZz3\_bNoCs2EC2kkxYeyQ/edit](https://www.canva.com/design/DAHYu1vbOjY/KSZz3_bNoCs2EC2kkxYeyQ/edit)   
[https\://www\.canva.com/design/DAHYvMo9g7k/8lruz-FUvrPSwqpaza8DQg/edit](https://www.canva.com/design/DAHYvMo9g7k/8lruz-FUvrPSwqpaza8DQg/edit)  
[https\://www\.canva.com/design/DAHYnzoZU-c/TO4uLE2EMoW7BsibcKGYMw/edit](https://www.canva.com/design/DAHYnzoZU-c/TO4uLE2EMoW7BsibcKGYMw/edit)  

[image1]: <data:image/png;base64,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>