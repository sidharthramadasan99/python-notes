#11_reverse_linked_list.py
#
#
#

def reverse_list(head):
    prev = None
    curr = head 

    while curr:
        nxt = curr.next  # save the next node
        curr.next = prev # Reverse the pointer
        prev = curr      # Move prev one step forward
        curr = nxt       # Move curr one step forward
    return prev  