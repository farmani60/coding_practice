class Queue:
    def __init__(self):
        self.queue = list()
    # Add element to the end of the queue
    def Enqueue(self, data):
        if data not in self.queue:
            self.queue.append(data)
            return True
        else:
            return False
    # Remove element from the front of the queue
    def Dequeue(self):
        if len(self.queue) == 0:
            print("No element in queue!")
        else:
            del self.queue[0]
            return self.queue
    # Print element at the front of the queue
    def Print(self):
        if len(self.queue) == 0:
            print("No element in queue!")
        else:
            print(self.queue[0])

queue = Queue()
queue.Enqueue(42)
queue.Dequeue()
queue.Enqueue(14)
queue.Print()
queue.Enqueue(28)
queue.Print()
queue.Enqueue(60)
queue.Enqueue(78)
queue.Dequeue()
queue.Dequeue()
queue.Print()