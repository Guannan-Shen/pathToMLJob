# Algorithm and Data Structure

## Algorithm

### Algorithm Complexity

**Space Complexity:** the amount of memory the program requires.

**Time Complexity:** time it takes to complete.  

All of these are judged by a defined set of input and output.  

### Common Big-O Terms

- Performance of the algorithm as the input size grows  
- "O" means the order of operation: time scale or memory scale to perform an operation
- Worst case scenario

Particularly, we have by ascending order of time complexity:

  1. O(1)  
  2. O(log n)
  3. O(n)
  4. O(n log n): heap sort and merge sort
  5. O(n^2): bubble sort, selection sort and insertion sort
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
