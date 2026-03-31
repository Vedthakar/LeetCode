/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    if(head == NULL || head->next == NULL) return head;
    int is_odd = 1;
    struct ListNode oddlist;
    struct ListNode evenlist;
    struct ListNode* elist = NULL;
    struct ListNode* olist = NULL;
    struct ListNode* p = head;
    oddlist.val = 0;
    oddlist.next = NULL;
    evenlist.next = NULL;
    evenlist.val = 0;
    elist = &evenlist;
    olist = &oddlist;
    while(p != NULL){
        if(is_odd == 1){
            elist->next = p;
            elist = elist->next;
            is_odd = 0;
        }else{
            olist->next = p;
            olist = olist->next;
            is_odd = 1;
        }
        p = p->next;
    }
    elist->next = oddlist.next;
    olist->next = NULL;
    struct ListNode* result = evenlist.next;
    return result;
}