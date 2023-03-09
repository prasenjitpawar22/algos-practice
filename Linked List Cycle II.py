#142. Linked List Cycle II

# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

node = ListNode(0)
node1= ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

# 0 -> 10 -> 20 -> 30
#      ^            ^   
#      |            |    
#      --------------
def detectCycle(head):
    p1, p2 = head, head #slow and fast
            
    while p2!=None and p2.next!=None:
        p1=p1.next
        p2=p2.next.next
        if p1==p2:
            break
        if p2==None or p2.next==None: #if fast becomes None return None i.e no cycle present rigth
            return None
    p2=head #if cycyle found, then make fast pointer to head point
    while p2!=p1:
        p1=p1.next #+1 next fast and slow until they are same 
        p2=p2.next
    return p1      #finally return slow or fast as they will be pointing to begning element one the cycle MATH magic!! (Floyd's cycle detection)
    
ans = detectCycle(node1)
if ans:
    print(ans.val)
