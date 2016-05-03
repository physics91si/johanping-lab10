#Write a set class

class NewSet(object):
    def __init__(self,set):
        self.set = set
    def does_contain(self,other):
        return other in self.set
    def adder(self,other):
        newlist = self.set
        if other not in self.set:
            newlist.append(other)
        return newlist
    def remover(self,other):
        newlist = self.set
        if other in self.set:
            newlist.remove(other)
            return newlist
        else:
            print("I'm sorry, that is not in the set.")
    def size(self):
        return len(self.set)
    def __union__(self, b):
        list = self.set
        for i in range(0,len(b)):
            if b[i] not in list:
                list.append(b[i])
        return list
    def __intersection__(self,b):
        list = []
        for i in range(0,len(b)):
            if b[i] in self.set:
                list.append(b[i])
        return list
    def __sub__(self,other):
        list = self.set
        for i in range(0,len(self.set)):
            if list[i] in other:
                list.remove(list[i])
        return list
            
    