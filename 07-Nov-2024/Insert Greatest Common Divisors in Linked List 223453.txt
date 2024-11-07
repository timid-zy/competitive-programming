# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

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
    int gcd(int a, int b) {
    if (b == 0) return  a;

    return gcd(b, a%b);
}

public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* prev = head;
        ListNode* curr = head->next;

        while (curr != nullptr) {
            ListNode* newNode = new ListNode(gcd(prev->val, curr->val));
            prev->next = newNode;
            newNode->next = curr;
            prev = curr;
            curr = curr->next;
        }

        return head;
    }
};