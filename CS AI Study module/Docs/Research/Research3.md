# **Detailed Summary: Algorithms, Data Structures & Connectionist AI**

# **Algorithms**

## Defenition Computer science, an algorithm is any well-defined set of instructions that when followed terminates after a finite number of steps that comprise a solution to a given computational problem. Advanced algorithms may utilize loops and involve many conditionals that decide the next step based on the inputs provided, resulting in long sequences of steps before halting, but all algorithms terminate by definition.

site \=[https\://en.wikipedia.org/wiki/Algorithm](https://en.wikipedia.org/wiki/Algorithm)

## Types of Algorithms 

| Algorithm family | What it does | Representative algorithms | Typical AI/computing use |
| :---- | :---- | :---- | :---- |
| **Searching** | Finds an item, value, or solution path | Linear search, binary search, BFS, DFS, A\*, best-first search | Database lookup, route finding, puzzle solving, path planning |
| **Sorting** | Arranges data in a defined order | Insertion sort, merge sort, quicksort, heapsort, counting sort, radix sort | Ranking, preprocessing, search preparation, data organization |
| **Recursion & divide-and-conquer** | Breaks a problem into smaller subproblems, solves them, then combines results | Merge sort, binary search, quicksort, Strassen’s algorithm | Efficient sorting, numerical computation, recursive problem solving |
| **Dynamic programming** | Solves problems with overlapping subproblems and optimal substructure | Floyd-Warshall, Needleman-Wunsch, Smith-Waterman, longest common subsequence | Shortest paths, sequence alignment, planning, optimization |
| **Greedy** | Makes the locally best choice at each step | Prim’s, Kruskal’s, Huffman coding, Dijkstra’s | Minimum spanning trees, compression, routing |
| **Graph algorithms** | Analyzes relationships represented as nodes and edges | Dijkstra’s, Bellman-Ford, PageRank, topological sort, minimum spanning trees | Knowledge graphs, recommendations, navigation, dependency analysis |
| **Graph/state-space search** | Explores possible states to find a goal | BFS, DFS, A\*, beam search, backtracking, iterative deepening | Planning, game AI, constraint solving, automated reasoning |
| **Optimization** | Finds the best solution under an objective function | Gradient descent, Newton’s method, simulated annealing, linear programming | Neural-network training, scheduling, resource allocation, model fitting |
| **Constraint satisfaction** | Finds values that satisfy a set of constraints | AC-3, backtracking, DPLL, min-conflicts | Scheduling, configuration, logic puzzles, SAT solving |
| **Combinatorial & matching** | Solves selection, assignment, and matching problems | Hungarian algorithm, Gale-Shapley, Hopcroft-Karp, branch-and-bound | Task assignment, matching, scheduling, logistics |
| **String & sequence algorithms** | Compares, searches, or aligns sequences | KMP, Boyer-Moore, Rabin-Karp, Levenshtein distance, sequence alignment | Text search, NLP preprocessing, bioinformatics, plagiarism detection |
| **Numerical & linear algebra** | Performs mathematical and matrix computations | Gaussian elimination, matrix multiplication, FFT, eigenvalue methods | Machine learning, simulations, signal processing, computer vision |
| **Randomized & probabilistic** | Uses randomness for speed, sampling, or approximation | Monte Carlo, Metropolis-Hastings, Gibbs sampling, Karger’s algorithm | Sampling, Bayesian inference, approximate counting, simulation |
| **Machine learning & classification** | Learns patterns or predictions from data | k-NN, decision trees, random forests, SVMs, naive Bayes, boosting | Classification, prediction, recommendation, anomaly detection |
| **Clustering** | Groups similar unlabeled data points | k-means, k-medoids, DBSCAN, OPTICS, hierarchical clustering | Customer segmentation, topic discovery, image grouping |
| **Neural-network / connectionist** | Learns distributed patterns using weighted artificial neurons | Perceptron, backpropagation, Hopfield networks, self-organizing maps | Vision, speech, language modeling, pattern recognition |
| **Reinforcement learning** | Learns actions through rewards and interaction with an environment | Q-learning, SARSA, temporal-difference learning | Robotics, game AI, recommendation, control systems |
| **Compression & coding** | Reduces data size or adds error resilience | Huffman coding, arithmetic coding, LZ77/LZ78, Reed-Solomon codes | Storage, transmission, multimedia, error correction |
| **Cryptography** | Secures data through encryption, hashing, and authentication | AES, RSA, Diffie-Hellman, SHA-2/SHA-3, digital signatures | Secure communication, authentication, data integrity |
| **Distributed systems** | Coordinates computation across multiple machines | Paxos, Raft, leader election, vector clocks, mutual exclusion | Cloud systems, databases, consensus, fault tolerance |
| **Database & query processing** | Efficiently stores, retrieves, and combines data | Hash join, nested-loop join, sort-merge join, transaction recovery | Search engines, analytics, transactional databases |
| **Scheduling & resource management** | Allocates CPU, memory, disk, or network resources | Round-robin, earliest-deadline-first, rate-monotonic scheduling, page replacement | Operating systems, cloud computing, task scheduling |
| **Graphics & image processing** | Renders, transforms, or analyzes visual data | Ray tracing, flood fill, edge detection, segmentation, feature detection | Computer vision, games, medical imaging, AR/VR |
| **Quantum algorithms** | Uses quantum operations to solve selected computational problems | Grover’s search, Shor’s algorithm, quantum Fourier transform, quantum walks | Cryptanalysis, optimization, simulation, quantum machine learning |

Link=[https\://en.wikipedia.org/wiki/List\_of\_algorithms](https://en.wikipedia.org/wiki/List_of_algorithms)

## 

# **Data Structures**

##  Defenition

Link=[https\://en.wikipedia.org/wiki/Data\_structure](https://en.wikipedia.org/wiki/Data_structure)  
In computer science, a data structure is a way to organize and store data that is usually chosen for efficient access to data. A data structure is the physical implementation of a data type, including specifications of the data organization and storage format, as well as functions or operations for working with this data. Data structures are closely related to abstract data types The data structure describes the representation of data in memory and how operations are carried out. Some authors do not use the term "abstract data type" and simply refer to the logical and physical forms of the data structure.

## Types of Data Structures

| Data structure | Main idea | Common AI/computing use |
| :---- | :---- | :---- |
| **Array** | Contiguous, indexed storage | Image pixels, tensors, embeddings, batched data |
| **Linked list** | Nodes connected by pointers | Dynamic sequences, adjacency lists |
| **Stack** | Last-in, first-out (LIFO) | Recursion, parsing, depth-first search |
| **Queue** | First-in, first-out (FIFO) | Breadth-first search, task scheduling |
| **Hash table** | Key-to-index mapping | Fast lookup of features, symbols, or cached results |
| **Tree** | Hierarchical parent-child structure | Decision trees, search trees, parse trees |
| **Graph** | Nodes and edges | Knowledge graphs, social networks, road maps, neural-network computation graphs |
| **Heap / priority queue** | Efficient access to highest/lowest priority item | Best-first search, scheduling, Dijkstra’s algorithm |

##  Implementation  Implementing a data structure involves writing a set of [subroutines](https://en.wikipedia.org/wiki/Subroutine)—such as insertion, deletion, traversal, or lookup—that create and manipulate instances of that structure. Data structures can be implemented using a variety of programming languages and techniques.

## 

##  

# **Connectionist AI**

## Descriptions

Link=[https\://en.wikipedia.org/wiki/Connectionism](https://en.wikipedia.org/wiki/Connectionism)

# **Connectionism**

**Connectionism** is an approach to cognition and AI that models mental processes using networks of simple, interconnected units—today usually called artificial neural networks (ANNs). Knowledge is not stored as explicit symbols or rules; it is distributed across the strengths, or **weights**, of connections between units.

## **Basic Principle**

The central idea is that mental phenomena can be described as patterns of activation across a network of simple, often uniform units. Units may represent individual neurons or groups of neurons, while connections may represent synapses.

