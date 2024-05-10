# linked list cocept
#"node1" --> "node2" --> ... --> "node n" --> None 

class linkedlist  :
    def __init__(self,value,next=None) -> None:
        self.data = value
        self.nextNode = next
node1 = linkedlist("3") 
node2 = linkedlist("7")
node3 = linkedlist("1")

node1.nextNode = node2 # "node1" --> "node2" ("3" --> "7")
node2.nextNode = node3 # "node2" --> "node3" ("7" --> "1")

# checking it
currentNode = node1 
while True : 
    print(f"'{currentNode.data}' -->",end="")
    if currentNode.nextNode == None : 
        break
    currentNode = currentNode.nextNode # node 1 will ne node 2 and node 2 will node 3 by this line.