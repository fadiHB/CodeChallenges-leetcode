# linked-list-cycle

- Link: https://leetcode.com/problems/linked-list-cycle/

- solved using two ways  

1. **Using a Set to Check Visited Nodes**: This approach involves iterating through the linked list while keeping track of visited nodes in a Set data structure. At each step, you check if the current node has been visited before. If it has, it indicates the presence of a cycle. This method is straightforward to implement and works well for small to moderate-sized linked lists.

2. **Using the Fast and Slow Pointer Algorithm**: This approach, also known as the "Floyd's Tortoise and Hare algorithm" or "cycle detection algorithm," uses one pointers traversing the linked list at different speeds. The "fast" pointer moves one steps at a time, while the "slow" pointer moves one step at a time. If there's a cycle in the linked list, the fast pointer will eventually catch up to the slow pointer, indicating the presence of a cycle. This method is more memory-efficient and generally faster for large linked lists.

## the concept of memory references

When you create a new object in JavaScript, such as a node in a linked list, it gets its own unique memory reference.  
This reference is like an address in memory that points to the location of the object's data.  
Even if you create two objects with the exact same properties (e.g., same value and next pointer), they will each have their own distinct memory reference.

For example, consider the following scenario:

```javascript
Copy code
const node1 = { value: 1, next: null };
const node2 = { value: 1, next: null };

console.log(node1 === node2); // Output: false
```
In this example, node1 and node2 have the same value and next pointer, but they are not considered equal because they have different memory references. JavaScript compares objects by reference, not by their properties.

So, when you store nodes themselves in a Set (or Array), the Set (or Array) keeps track of the memory references of the nodes you've visited. If you encounter a node with the same memory reference again, it means you've encountered a cycle in the linked list, regardless of the values and next pointers of the nodes.

## Array & Object

When you store nodes in an array, each node object is added to the array. The array holds references to these node objects. Even if two nodes have the same properties (value and next pointer), they are distinct objects with their own memory addresses.

Consider this example:

```javascript
const node1 = { value: 1, next: null };
const node2 = { value: 1, next: null };

const arr = [];
arr.push(node1);

console.log(arr.includes(node2)); // Output: false
```

In this example, arr.includes(node2) returns false because node2 is a different object than node1, even though they have the same properties. Arrays in JavaScript compare objects by reference, not by their properties.

So, when traversing the linked list and storing nodes in an array, each node object is added to the array. If you encounter a node with the same memory reference again during traversal, it means you've encountered a cycle in the linked list.

## Set & Object


That's a great question. The reason a Set doesn't allow duplicate elements is due to how it handles equality comparison for objects.

When you add an element to a Set, the Set checks whether an element with the same value is already present. However, when it comes to objects (including nodes in this case), the equality comparison is based on the reference to the object in memory, not its properties.

Consider this example:

```javascript
const node1 = { value: 1, next: null };
const node2 = { value: 1, next: null };

const set = new Set();
set.add(node1);

console.log(set.has(node2)); // Output: false
```

In this example, set.has(node2) returns false even though node1 and node2 have the same properties. This is because they are distinct objects with different memory references.

## Array & Set

However, there are some differences between Sets and Arrays to consider:

1. **Efficiency**: Sets are typically more efficient for checking membership (i.e., whether an element is already present in the Set) compared to Arrays. Sets use hash-based data structures internally, which offer faster lookup times, especially for large collections of data. This can be advantageous if you're dealing with very large linked lists.

2. **Uniqueness**: Sets ensure that each element is unique, so you don't need to worry about duplicates. Arrays, on the other hand, can contain duplicate elements, so you might need to implement additional logic to handle duplicates if using an Array.

3. **Ordering**: Sets do not guarantee the order of elements, whereas Arrays maintain the order in which elements are added. If preserving the order of visited nodes is important for your application, an Array might be preferable.
