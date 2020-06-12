class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        
        if len(self.storage) > self.capacity:
            storage.append(item)
        
        

    def get(self):
        pass