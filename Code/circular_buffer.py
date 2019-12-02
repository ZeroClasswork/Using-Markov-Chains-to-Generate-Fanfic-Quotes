class CircularBuffer(list):

    def __init__(self, length):
        super(CircularBuffer, self).__init__()
        self.writer = 0
        self.reader = 0
        self.length = length

    def write(self, item):
        self.append(item)
        if len(self) > self.length:
            self.remove(self[0])
            self.reader = (self.reader - 1) % self.length
        self.writer = (self.writer + 1) % self.length
    
    def read(self):
        item = self[self.reader]
        self.reader = (self.reader + 1) % self.length
        return item

    def __str__(self):
        original = self.reader
        buffer = "["
        length = len(self) if self.length > len(self) else self.length
        for index in range(length):
            buffer += "'" + str(self.read()) + "'"
            if index <= length - 2:
                buffer += " -> "
        buffer += "]"
        self.reader = original
        return buffer

def test():
    buffer = CircularBuffer(5)
    print(buffer)
    buffer.write(2)
    print(buffer)
    buffer.write(5)
    print(buffer)
    buffer.write(6)
    print(buffer)
    buffer.write(7)
    print(buffer)
    buffer.write(8)
    print(buffer)
    print(buffer.read())
    buffer.write(10)
    print(buffer)
    print(buffer.read())
    print(buffer.read())
    print(buffer.read())
    print(buffer.read())
    print(buffer.read())
    buffer.write(23)
    print(buffer)
    buffer.write(666)
    print(buffer)

if __name__ == "__main__":
    test()