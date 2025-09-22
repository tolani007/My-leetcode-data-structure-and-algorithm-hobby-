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

Time: O(n) — each node is visited at most once.

Space complexity:

Space: O(1) — in-place pointer rewiring; only a few locals plus the dummy node.
