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

class Solution
{
public:
    int gcd(int a, int b)
    {
        // Everything divides 0
        if (a == 0)
            return b;
        if (b == 0)
            return a;

        // base case
        if (a == b)
            return a;

        // a is greater
        if (a > b)
            return gcd(a - b, b);
        return gcd(a, b - a);
    }

    ListNode *insertGreatestCommonDivisors(ListNode *head)
    {
        ListNode *travelNode = head;
        ListNode *nextNode;

        while (travelNode->next != nullptr)
        {
            nextNode = travelNode->next;
            travelNode->next = new ListNode(gcd(travelNode->val, nextNode->val), nextNode);
            travelNode = nextNode;
        }
        return head;
    }
};