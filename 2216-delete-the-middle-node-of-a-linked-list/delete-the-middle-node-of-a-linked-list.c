/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    if(head == NULL || head->next == NULL) {
        return NULL;
    }
    int len = 0;
    struct ListNode* p = NULL;
    struct ListNode* tr = NULL;
    int idx = 0;
    p = head;
    while(p != NULL){
        len++;
        p = p->next;
    }
    p = head;
    int middle = len / 2;
    while(idx < middle -1){
        idx++;
        p = p->next;
    }
    tr = p->next;//the node to delete
    if(tr != NULL){
        p->next = tr->next;
    }else{
        p->next = NULL;
    }
    free(tr);
    return head;
}