/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode*p = NULL;
    struct ListNode*tr = NULL;
    int len = 0;
    int dist = 0;
    p = &dummy;
    tr = head;
    while (tr != NULL){
        len++;
        tr = tr->next;
    }
    tr = head;
    dist = len - n;
    for(int i = 0; i < dist; i++){
        p = p->next;
        tr = tr->next;
    }
    if(tr != NULL){
        p->next = tr->next;

    }else{
        p->next = NULL;
    }
    free(tr);
    return dummy.next;
}