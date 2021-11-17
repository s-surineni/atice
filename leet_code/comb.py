from os.path import commonprefix

class CombinationIterator:

    def __init__(self, characters, combinationLength):
        self.c = characters
        self.len = combinationLength
        self.state = ""
        
    def next(self):
        if self.state == "":
            self.state = self.c[:self.len]
        else:
            end = len(commonprefix([self.c[::-1], self.state[::-1]]))
            place = self.c.index(self.state[-end-1])
            self.state = self.state[:-end-1] + self.c[place + 1: place + 2 + end]
        return self.state

    def hasNext(self):
        return self.state != self.c[-self.len:]
    
itr = CombinationIterator("abc", 2);
itr.next();    
itr.hasNext(); 
itr.next();    
itr.hasNext(); 
itr.next();    
itr.hasNext(); 
