class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def append(self, item):
        print(len(self.storage)+"<"+self.capacity)
        if len(self.storage) < self.capacity:
            self.storage.insert(0,item)
        else:
            self.storage.insert(self.oldest, item)
            if self.oldest == len(self.storage)-1:
                self.oldest = 0
            else:
                self.oldest +=1
        

    def get(self):
        return self.storage