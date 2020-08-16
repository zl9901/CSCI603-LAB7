from node import LinkedNode

class HashMap:

    __slots__ = "cap","factor","items","count","threshold"

    def __init__(self,factor,cap,count,threshold):
        self.factor = factor
        self.cap=cap
        self.items=[]
        self.count=count
        self.threshold=threshold
        for i in range(cap):
            # self.items.append(None)
            self.items.append(LinkedNode(None))



    def __str__(self):
        index=self.findindex(10)
        str=" "
        node = LinkedNode(None)
        node.next=self.items[index].next
        while node is not None:
            str+=(node.value+"  ")
            node=node.next
        return str



    def get(self,Val):
        newnode=LinkedNode(None)
        index=self.findindex(Val)
        newnode.next=self.items[index].next
        while newnode is not None:
            if hash(newnode.value) is hash(Val):
                return newnode.value
            newnode=newnode.next



    def findindex(self,Val):
        index=hash(Val)%len(self.items)
        if index>=0:
            return index
        else:
            return -index

    def add(self,index,Val):
        node=LinkedNode(Val)
        node.next=self.items[index].next
        self.items[index].next=node
        self.count+=1
        if self.count>=int(self.threshold):
            self.resize(len(self.items)*2)


    def put(self,Val):
        index=self.findindex(Val)
        entry=self.items[index].next
        while entry is not None:
            if hash(entry.value) is  hash(Val):
                return
            else:
                entry=entry.next
        self.add(index,Val)


    def remove(self,Val):
        index=self.findindex(Val)
        pre=None
        entry=self.items[index].next
        while entry is not None:
            if hash(entry.value) is hash(Val):
                if pre is None:
                    self.items[index].next=entry.next
                else:
                    pre.next=entry.next
                return entry.value
            pre=entry
            entry=entry.next

    def resize(self,capacity):
        table=[]
        for j in range (capacity):
            table.append(LinkedNode(None))
        # print(table)

        for k in range (len(self.items)):
            old=self.items[k].next
            while old is not None:
                temp = old.next
                index=self.findindex(old.value)
                old.next=table[index].next
                table[index].next=old
                old=temp

        self.items=table
        self.threshold=int(len(self.items)*self.factor)



def test():
    # hp=HashMap(0.75,16,0,16*0.75)
    # print(hp.items)
    # hp.add(0,100)
    # print(hp.items)
    # hp.put(80)
    # print(hp.items)
    # print(hp.get(80))
    # print()
    #
    # print(hp.remove(80))
    # print(hp.items)
    # hp.resize(4)
    hp=HashMap(0.75,4,0,4*0.75)
    print(hp.items)
    hp.put(1)
    print(hp.items)
    hp.put(2)
    print(hp.items)
    hp.put(3)
    print(hp.items)
    hp.put(4)
    print(hp.items)


if __name__ == "__main__":
    test()
