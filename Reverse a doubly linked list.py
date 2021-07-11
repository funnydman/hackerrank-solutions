def reverse(llist):
    temp = llist
    curr = curr_head = DoublyLinkedListNode(None)
    while temp.next:
        temp = temp.next
    
    while temp:
        curr.next = temp
        curr.prev = temp.next
        temp = temp.prev
        curr = curr.next
        
    # this is important! edge case, loop instead
    curr.next= None
        
    return curr_head.next
