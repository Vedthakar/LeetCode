/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode head;
    struct ListNode* tail = NULL;
    struct ListNode* tmp = NULL;
    tail = &head;
    while(list1 != NULL && list2 != NULL){
        if(list1->val < list2->val){
            tmp = list1->next;
            tail->next = list1;
            tail = tail->next;
            list1->next = NULL;
            list1 = tmp;
        }else{
            tmp = list2->next;
            tail->next = list2;
            tail = tail->next;
            list2->next = NULL;
            list2 = tmp;
        }
    }
    if(list1 != NULL){
        tail->next = list1;
    }else if(list2 != NULL){
        tail->next = list2;
    }
    return head.next;
}