class Queue:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.Q = [None]*5

    def enqueue(self, x):
        if self.head == self.tail:
            print("Head == tail, please dequeue")
            return
        self.Q[self.tail] = x
        self.tail += 1
        if self.tail >= len(self.Q):
            self.tail = 0

    def dequeue(self):
        x = self.Q[self.head]
        self.head += 1
        if self.head >= len(self.Q):
            self.head = 0
        return x

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.Q)
print("Head: " + str(q.head) + ", tail: " + str(q.tail))
q.enqueue(5)
print(q.Q)
print("Head: " + str(q.head) + ", tail: " + str(q.tail))
x = q.dequeue()
print(q.Q)
print("Head: " + str(q.head) + ", tail: " + str(q.tail))
q.enqueue(6)
print(q.Q)
print("Head: " + str(q.head) + ", tail: " + str(q.tail))
