def findMergeNode(head1, head2):
    visited  = []
    temp = head1
    while temp:
        visited.append(temp)
        temp = temp.next
    while head2:
        if head2 in visited:
            return visited[visited.index(head2)].data
        head2 = head2.next
