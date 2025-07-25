class Queue1:
    def __init__(self):
        self.queue1 = []

    def enqueue(self, element):
        self.queue1.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue1.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue1[0]

    def isEmpty(self):
        return len(self.queue1) == 0

    def size(self):
        return len(self.queue1)


# Create a queue
myQueue = Queue1()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue1)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue1)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())