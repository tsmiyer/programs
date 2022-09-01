class Node :
    def __init__(self, data):
        self.task = data
        self.next = None


class CircularQueue :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.size = self.size + 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.size = self.size + 1

    def pop(self):
        if(self.size == 0):
            print("Queue is empty !")
            return
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.size = self.size - 1

    def front(self):
        return self.head.task

    def print_queue(self):
        temp = self.head
        c = 0
        if(self.size == 0):
            print("Queue is empty !")
            return
        else:
            while(c < self.size):
                print(temp.task + " -> ", end = "")
                temp = temp.next
                c = c+1
            print(temp.task+"...")


def RoundRobinScheduler():
    print("Note :- The tasks are stored using a circular queue data structure.")
    n = int(input("Enter the number of tasks : "))
    CQ = CircularQueue()
    for i in range(n):
        CQ.push("Task " + str(i + 1))
    for i in range(1, n+1):
        print()
        print("************************")
        print("The current queue structure holds the following tasks before execution begins :")
        CQ.print_queue()
        print("The current task getting executed : "+CQ.front())
        curr = CQ.front()
        CQ.pop()
        print("The tasks which are stored in the queue while the current task is getting executed are : ")
        CQ.print_queue()
        print(curr+" has been pushed to the end of the queue.")
        CQ.push(curr)
        print("************************")


RoundRobinScheduler()