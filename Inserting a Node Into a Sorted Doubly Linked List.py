def sortedInsert(llist, data):
    # Write your code here
    if not llist:
        return llist
    temp = llist
    node = DoublyLinkedListNode(data)
    # insert before head
    if data < temp.data:
        temp.prev = node
        node.next = temp
        temp = node
        return temp 
    
    while temp.next and temp.next.data < data:
        temp = temp.next
    # inserto to the end
    if not temp.next:
        temp.next = node
        node.prev = temp
    else:
        nn = temp.next
        temp.next = node
        node.prev = temp
        node.next = nn
        nn.prev = node
    
    return llist
    
    
