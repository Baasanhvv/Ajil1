class Queue():
    
    
    def __init__(self):
        self._data = []
    
    
    def lenn(self): #
        l= 0
        for i in self._data:
            l = l + 1
        return l

    def is_empty(self): #
        if self.lenn() == 0:
            return True
        else:
            return False
    
    def enqueue(self, a): #
        self._data = self._data + [a]
            
    def first(self): #
        if self.is_empty() == False:
            return self._data[0]
        else:
            return "Hooson"
        
    def dequeue(self):
        if self.is_empty() == 0:
            z = self._data[0]
            self._data = self._data[1:]
            return z
        else:
            return "error"
class Double_Ended(Queue):
    def add_first(self , a):
        self._data = [a] +self._data
    
    def add_last(self , a):
        self._data = self._data +[a]
    
    def last(self):
        if self.is_empty() == False:
            return self._data[-1]
        else:
            return "Hooson"
        
    def delete_last(self):
        if self.is_empty() == 0:
            z = self._data[-1]
            self._data = self._data[:-1]
            return z
        else:
            return "error"
    
    def print(self):
        return self._data