# Find Kth to last element of a singly linked list
# Do we know the length of the list? 
# kth_to_last = len - (k - 1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            node = node.next
    
    def find_length(self):
        node = self
        length = 0
        while node != None:
            length += 1
            node = node.next
        return length

# finds kth to last element/node given k and first node
def kth_to_last(k, head):
    node = head
    length = head.find_length()
    Kth = length - (k-1)
    if length >= k:
        for i in range(Kth-1):
            node = node.next
        print(node.data)
    else:
        print(None)

def elegant_solution(k, head):
    p1 = head
    p2 = head
    for i in range(k):
        p1 = p1.next
    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    return p2.data


nodeA = Node(3)
nodeB = Node(7)
nodeC = Node(4)
nodeD = Node(9)
nodeE = Node(2)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print(elegant_solution(3, nodeD))