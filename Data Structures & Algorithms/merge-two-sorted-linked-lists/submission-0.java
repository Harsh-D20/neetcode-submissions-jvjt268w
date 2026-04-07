/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy_head = new ListNode();
        ListNode start = dummy_head;
        while(list1 != null && list2 != null) {
            if(list1.val <= list2.val) {
                dummy_head.next = list1;
                list1 = list1.next;
            }
            else {
                dummy_head.next = list2;
                list2 = list2.next;
            }
            dummy_head = dummy_head.next;
        }
        if(list1 != null) {
            dummy_head.next = list1;
        }
        else if(list2 != null) {
            dummy_head.next = list2;
        }

        return start.next;
    }
}