
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeList(head1, head2):
    if (head1 is None) and (head2 is None):
        return None
    if (head1 is None) and (head2 is not None):
        return head2
    if (head1 is not None) and (head2 is None):
        return head1
    if head1.data <= head2.data:
        head1.next = mergeList(head1.next, head2)
    else:
        temp = head2
        head2 = head2.next
        temp.next = head1
        head1 = temp
        head1.next = mergeList(head1.next, head2)
    return head1