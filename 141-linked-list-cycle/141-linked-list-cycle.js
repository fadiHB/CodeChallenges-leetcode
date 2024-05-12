/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle2 = function(head) {
    const visited = new Set();
        while (head !== null) {
        if (visited.has(head)) return true
        visited.add(head);
        head = head.next;
    }    
    return false;
};

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    if (!head || !head.next) return false;
    let slow = head, fast = head;
    do {
        slow = slow.next;
        fast = fast.next.next;
        if (fast === slow) return true
    } while (fast && fast.next);
    return false;
}
