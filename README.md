# Python DSA Journey

A structured, pattern-first journey from DSA fundamentals to advanced algorithms using Python.

We will prioritize understanding and building problem-solving logic over solving a large number of problems. Lessons progress one concept and one problem at a time. A problem is added here after we have worked through it.

## Learning principles

- Logic before code: understand the problem, derive an approach, then implement it.
- Patterns over memorization: learn reusable techniques and when they apply.
- Complexity throughout: analyze time and auxiliary space for each solution.
- Python as a tool: learn relevant built-ins and modules when they become useful.
- One problem at a time: no batches or rushing; progress when the learner is ready.

## Roadmap

### 00 — Foundations
- What are data structures and algorithms?
- Problem-solving framework: understand, model, solve, test, optimize
- Brute force and optimization
- Input sizes and operation counting
- Time complexity: Big O, best/average/worst cases
- Space complexity and auxiliary space
- Complexity comparison and trade-offs

### 01 — Searching
- Linear search
- Binary search and its preconditions
- Iterative and recursive binary search
- First/last occurrence and insertion positions
- Search in rotated sorted arrays
- Binary search on the answer

### 02 — Sorting
- Bubble, selection, and insertion sort
- Merge sort and quicksort
- Counting sort and other suitable non-comparison sorts
- Stability, in-place sorting, and complexity trade-offs
- Python `sort()` and `sorted()`

## Part I — Linear Data Structures

### 03 — Arrays and Python Lists
- Arrays vs Python lists; indexing and traversal
- Access, update, insertion, deletion
- Running minimum/maximum and candidate tracking
- In-place operations
- Two-pointer foundations
- Prefix/suffix calculations and subarray foundations

### 04 — Strings
- String indexing, traversal, and immutability
- Character counting and transformations
- Palindromes, substring basics, construction costs
- Two-pointer and frequency patterns

### 05 — Hashing
- Hash tables and hash functions (conceptually)
- Python dictionaries and sets
- Lookup, membership, frequency maps
- Duplicate detection, complement lookup, grouping
- Collision concepts and average vs worst-case behavior

### 06 — Two Pointers
- Opposite-direction pointers
- Same-direction pointers
- Sorted-array and in-place patterns
- Pair and partition problems

### 07 — Sliding Window
- Fixed-size windows
- Variable-size windows
- Expand/shrink conditions
- Maintaining counts and window state

### 08 — Prefix Sums and Range Techniques
- Running, prefix, and suffix sums
- Range sum queries
- Prefix counts and subarray reasoning
- Difference arrays and preprocessing trade-offs

### 09 — Linked Lists
- Nodes and references
- Singly and doubly linked lists
- Traversal, insertion, and deletion
- Reversal, middle node, cycle detection
- Fast and slow pointers

### 10 — Stacks
- LIFO and stack implementation
- Balanced brackets and nested structures
- Monotonic stacks
- Next greater/smaller element patterns

### 11 — Queues and Deques
- FIFO, queue operations, and circular queues
- Python `collections.deque`
- Double-ended queues
- Queue applications and BFS foundations

### 12 — Recursion
- Base case and recursive case
- Call stack and tracing
- Recursion depth and complexity
- Recursive vs iterative solutions
- Foundations for backtracking and tree traversal

## Part II — Non-Linear Data Structures

### 13 — Trees
- Tree terminology and representations
- Binary trees
- Preorder, inorder, postorder
- Level-order traversal
- DFS and BFS
- Recursive and iterative traversal

### 14 — Binary Search Trees
- BST property
- Search, insert, and delete
- Minimum/maximum
- Height, balanced vs skewed trees
- Complexity analysis

### 15 — Heaps and Priority Queues
- Min-heap and max-heap concepts
- Heap operations and heapify
- Python `heapq`
- Top-K, Kth element, merge sorted sequences

### 16 — Tries
- Prefix tree structure
- Insert, search, and prefix lookup
- Autocomplete use cases
- Time and space trade-offs

### 17 — Graphs
- Vertices, edges, directed/undirected, weighted/unweighted
- Adjacency list and matrix
- BFS and DFS
- Connected components and cycle detection
- Bipartite graphs and topological sorting
- Shortest paths: unweighted BFS, Dijkstra, Bellman–Ford, Floyd–Warshall
- Minimum spanning trees: Kruskal and Prim

### 18 — Disjoint Set Union
- Find and union
- Path compression
- Union by rank/size
- Connectivity and Kruskal applications

## Part III — Algorithms and Advanced Problem-Solving

### 19 — Greedy Algorithms
- Greedy choice and correctness reasoning
- Sorting-based greedy strategies
- Intervals, scheduling, and resource allocation
- Recognizing when greedy does not work

### 20 — Backtracking
- Decision trees and choose/explore/unchoose
- Constraints and pruning
- Subsets, combinations, permutations
- N-Queens and Sudoku-style search

### 21 — Dynamic Programming
- Overlapping subproblems and optimal substructure
- State, transition, and base cases
- Recursion, memoization, and tabulation
- Space optimization
- 1D and 2D DP
- Knapsack, grids, subsequences, strings
- DP on trees

### 22 — Range-Query Data Structures
- Coordinate compression
- Fenwick trees
- Segment trees
- Range queries, updates, and lazy propagation concepts

### 23 — Advanced Graph Algorithms
- Strongly connected components
- Bridges and articulation points
- Advanced shortest paths and connectivity problems

### 24 — Bit Manipulation
- Binary representation and bitwise operators
- Shifts, masks, set/clear/check bits
- Counting set bits and XOR patterns
- Bit-based subset techniques

### 25 — Mathematical Algorithms
- Divisibility, primes, and primality testing
- GCD and LCM; Euclidean algorithm
- Sieve of Eratosthenes
- Modular arithmetic
- Fast exponentiation
- Basic combinatorics

## Python tools introduced when relevant

| Tool | Typical use |
|---|---|
| `list`, `dict`, `set` | Core sequence and hashing work |
| `collections.Counter` | Frequency counting |
| `collections.defaultdict` | Grouping and graph representations |
| `collections.deque` | Queues, BFS, deque patterns |
| `heapq` | Heaps and priority queues |
| `bisect` | Binary-search utilities |
| `itertools` | Combinations and permutations |
| `functools.cache` | Memoization |
| `math` | Mathematical algorithms |
| `timeit` | Small performance experiments |

We will understand the underlying algorithm before relying on a Python helper.

## Complexity reference

| Complexity | Typical example |
|---|---|
| O(1) | Indexed list access |
| O(log n) | Binary search |
| O(n) | Single traversal |
| O(n log n) | Merge sort |
| O(n²) | Comparing all pairs |
| O(2^n) | Some subset enumerations |
| O(n!) | Generating all permutations |

Actual complexity depends on the algorithm and its input assumptions. Each completed problem will record time and auxiliary-space complexity.

## Progress log

| Phase | Topic | Status |
|---|---|---|
| 00 | Foundations | Not started |
| 01–02 | Searching and Sorting | Not started |
| 03–12 | Linear data structures | Not started |
| 13–18 | Non-linear data structures | Not started |
| 19–25 | Advanced algorithms | Not started |

## Completed problems

No problems completed yet. Solutions will be added topic by topic after we solve and review them together.

## Problem write-up convention

Each completed problem will include:
1. Problem statement and examples
2. Core observation / pattern
3. Plain-English approach and pseudocode
4. Python implementation
5. Dry run and edge cases
6. Time complexity
7. Auxiliary space complexity
8. Key takeaway and when to reuse the pattern

---

**Progress rule:** We move forward only when the learner is ready. This roadmap is comprehensive, but each lesson remains focused on one concept and one problem at a time.
