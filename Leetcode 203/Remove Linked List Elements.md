Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:

<img width="782" height="222" alt="image" src="https://github.com/user-attachments/assets/bd272e60-067f-409a-891a-224efd864085" />



Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50


Intuition
Walk the list with a pointer that always sits before the node you might delete. If the next node’s value equals val, “skip” it by pointing around it. Using a tiny fake node (dummy) in front of head makes removing the real head trivial

Approach
Create dummy = ListNode(0, head) and set current = dummy.

While current.next exists:

If current.next.val == val, bypass it: current.next = current.next.next.

Else, advance: current = current.next.

Return dummy.next (the possibly-new head).

This handles:

Empty list (head is None)

Head(s) equal to val

Consecutive matches

Complexity
Time complexity:
Space complexity:
Time: O(n) — each node is visited at most once.
Space: O(1) — in-place pointer rewiring; only a few locals plus the dummy node.


