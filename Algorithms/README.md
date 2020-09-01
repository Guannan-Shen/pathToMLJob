# Algorithm and Data Structure

## Algorithm

Assume a generic one-processor, **random-access machine (RAM) model** of computation as our implementation technology and understand that our algorithms will be implemented as computer programs. In the RAM model, instructions are executed one after another, with **no concurrent operations**.  

### Algorithm Complexity

**Space Complexity:** the amount of memory the program requires.

**Time Complexity:** time it takes to complete. Performance as Order of Growth of time as Growth of the data, in terms of Worst Case.  

All of these are judged by a defined set of input and output. Each step such as calculation (+ - * /), memory access, comparison takes unit time.  

### Common Big-O Terms

- Performance of the algorithm as the input size grows  
- "O" means the order of operation: time scale or memory scale to perform an operation
- Worst case scenario

Particularly, we have by ascending order of time complexity:

  1. O(1)  
  2. O(log n)
  3. O(n)
  4. O(n log n): heap sort and merge sort
  5. ![equation](https://latex.codecogs.com/gif.latex?O(n^2)): bubble sort, selection sort and insertion sort
  6. O(n!)

## Data Structure

### Common Data Structure

- Arrays: collection of elements, one or multi-dimensional.
- Linked lists: linear collection of nodes.
- Stacks and queues
    1. Stacks support push and pop, both are constant time O(1) operation, last in (push) first out (pop). Stack has been used for backtracking.
    2. Queues support adding and removing, first in first out. Queue has been used for order processing and messaging.  
- Trees
- Hash tables or Dictionary: associative array, using Hash function to map keys to values. Hash function calculate index to map values to slots in the Hash table. Collisions could happen in non One to One scenario (not injective).
    1. Unique mappings allow us to make counters and filters.
    2. Faster than other table look-up methods, especially when data size is large.
    3. Small data, array is more efficient.
    4. Can not arrange data in a predictable way, similar values may have very different slots.  
- Graph

## Techniques

### Recursion  

Recursion is a function calls itself.  

- Need a breaking condition  
- Each time the function is called, the old arguments are saved, not ove-written, but stored aside.  
- Use call stack to achieve above functionality.  

### Sorting  

    - Bubble Sort: 
      very basic sorting method, only for teaching. Performance O($n^2$), a for loop inside a for loop.  

    - Merge Sort: 
      Divide-and-conquer algorithm, O(n log n). Breaks a dataset into pieces then merge them, good for large sets of data.  

    - Quick Sort:  
      Divide-and-conquer algorithm, O(n log n) but usually better than merge sort, and operating **in place** on the data. Thus, requires less memory. Efficient for sorting a small number of elements. Worst case, if data is mostly sorted already, O(n^2).  

    - Insertion Sort:  
      An array A[1..n] containing a sequence of length n that is to be sorted. (In the code, the number n of elements in A is denoted by A.length.) A[j] is the key, the card to be inserted.  
      The idea of **Loop Invariant**, during the insertion sort:    
        At the beginning of each iteration of the for loop, which is indexed by j, the subarray consisting of elements A[1..j-1] constitutes the currently sorted hand, and the remaining subarray A[j+1..n] corresponds to the pile of cards still on the table. In fact, elements A[1..j-1] are the elements originally in positions 1 through j - 1, but now in sorted order. We state these **properties of A[1..j-1] formally as a loop invariant**.

### Search  
