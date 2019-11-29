class Queue(list):


    def __init__(self):
        super(Queue, self).__init__()
        self.first = None

    def enqueue(self, item):
        if self.first is None:
            self.first = item
        self.append(item)

    def dequeue(self):
        if self.first is None:
            raise IndexError
        item = self.first
        self.remove(self.first)
        if len(self) > 0:
            self.first = self[0]
        else:
            self.first = None
        return item

    def iterate(self):
        queue = "["
        for index, item in enumerate(self):
            queue += "'" + str(item) + "'"
            if index < len(self) - 1:
                queue += " -> "
        queue += "]"
        return queue

def test():
    queue = Queue()
    try:
        queue.dequeue()
    except:
        print("Dequeue original empty queue works")
    print(queue.iterate())
    queue.enqueue(("I", "was"))
    print(queue.iterate())
    queue.enqueue(("was", "told"))
    print(queue.iterate())
    queue.enqueue(("told", "no"))
    print(queue.iterate())
    queue.dequeue()
    print(queue.iterate())
    queue.dequeue()
    print(queue.iterate())
    queue.dequeue()
    print(queue.iterate())
    try:
        queue.dequeue()
        print(queue.iterate())
    except:
        print("Dequeue emptied queue works")

if __name__ == "__main__":
    test()