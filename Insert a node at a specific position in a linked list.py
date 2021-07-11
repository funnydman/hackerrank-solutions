# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    temp = llist
    i = 0
    while temp and i<(position-1):
        temp = temp.next
        i+=1
    node = SinglyLinkedListNode(data)
    nn = temp.next
    temp.next= node
    node.next = nn
    return llist
    
