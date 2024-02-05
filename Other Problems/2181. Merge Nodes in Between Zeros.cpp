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
    ListNode* mergeNodes(ListNode* head) {
        if (head->next == NULL) {
            return head;
        }
        ListNode* zerStart = head;
        ListNode* travelNode = head->next;
        int sum;
        while(true){
            sum = 0;
            while(travelNode->val != 0){
                sum += travelNode->val;
                travelNode = travelNode->next;
            }
            zerStart->val = sum;
            if (travelNode->next == NULL){
                zerStart->next = NULL;
                return head;
            }
            zerStart->next = travelNode;
            zerStart = zerStart->next;
            travelNode = travelNode->next;
        }
    }
};


// Another solution found in the discusiion section
 ListNode* mergeNodes(ListNode* head) {
     head=head->next;
     ListNode* start=head;
     while(start){
	    ListNode* end= start;   /* Point to first node of current part for getting sum */
        int sum=0;
        while(end->val!=0) sum+= end->val , end=end->next;
        start->val=sum;   /*assign sum to first node between two 0*/
        start->next=end->next;   /*make this connect to first node of next part*/
        start=start->next;    /*go..to..next..part*/
	 }
     return head;
}