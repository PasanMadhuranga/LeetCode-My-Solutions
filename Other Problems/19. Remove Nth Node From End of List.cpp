/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* travelNode = head;
        int length = 0;

        while (travelNode){
            travelNode = travelNode->next;
            length++;
        }
        travelNode = head;
        n = length - n;
        if (n){
            for (int i=1; i<n;i++){
                travelNode = travelNode->next;
            }
            travelNode->next = travelNode->next->next;
        }else{
            head = head->next;
        }
        return head;
    }
};


// Another solution found in the discussion section

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        ListNode* slow = head;

        for (int i=0; i<n; i++)
        {
            fast = fast->next;
        }
        if (!fast)
        {
            return head->next;
        }
        while (fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return head;
    }
};