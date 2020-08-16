from node import LinkedNode

class HashMap:

    __slots__ = "cap","factor","items","values","count","threshold"

    def __init__(self,factor,cap,count,threshold):
        self.factor = factor
        self.cap=cap
        self.items=[]
        self.values=[]
        self.count=count
        self.threshold=threshold
        for i in range(cap):
            # self.items.append(None)
            self.items.append(LinkedNode(None))
        for j in range(cap):
            self.values.append(LinkedNode(None))



    def __str__(self):#这里的toString方法有问题
        index=self.findindex(10)
        str=" "
        node = LinkedNode(None)
        node.next=self.items[index].next
        while node is not None:
            str+=(node.value+"  ")
            node=node.next
        return str



    def getKey(self,Val):
        index=self.findindex(Val)
        newnode=self.items[index].next
        while newnode is not None:
            if hash(newnode.value) is hash(Val):
                return newnode.value
            newnode=newnode.next

    def getValue(self, Key,Val):
        index = self.findindex(Key)
        pointer= self.values[index].next
        while pointer is not None:
            if pointer.value is Val:
                return pointer.value
            pointer = pointer.next



    def findindex(self,Val):
        index=hash(Val)%len(self.items)
        if index>=0:
            return index
        else:
            return -index


    def add(self,index,Key,Val):
        node=LinkedNode(Key)
        node1=LinkedNode(Val)

        node.next=self.items[index].next
        node1.next = self.values[index].next

        self.items[index].next=node
        self.values[index].next = node1

        self.count+=1
        if self.count>=int(self.threshold):
            self.resize(len(self.items)*2)



    def put(self,Key,Val):
        index=self.findindex(Key)
        entry=self.items[index].next

        while entry  is not None :
            if hash(entry.value) is  hash(Key):
                return
            else:
                entry=entry.next
        self.add(index,Key,Val)


    def remove(self,Key):
        index=self.findindex(Key)
        pre=None
        pre1=None
        entry=self.items[index].next
        entry1=self.values[index].next
        while entry is not None:
            if hash(entry.value) is hash(Key):
                if pre is None:
                    self.items[index].next=entry.next
                    self.values[index].next = entry1.next
                else:
                    pre.next=entry.next
                    pre1.next=entry1.next
                # return entry.value
            pre=entry
            pre1=entry1
            entry=entry.next
            entry1=entry1.next



    def resize(self,capacity):
        table=[]
        table1=[]
        for m in range (capacity):
            table.append(LinkedNode(None))
        # print(table)
        for n in range(capacity):
            table1.append(LinkedNode(None))

        for k in range (len(self.items)):
            old=self.items[k].next
            old1 = self.values[k].next
            while old is not None:
                temp = old.next
                temp1=old1.next
                index=self.findindex(old.value)
                old.next=table[index].next
                old1.next = table1[index].next
                table[index].next=old
                table1[index].next = old1
                old=temp
                old1=temp1

        self.items=table
        self.values=table1
        self.threshold=int(len(self.items)*self.factor)



def test():
    hp=HashMap(0.75,4,0,4*0.75)
    # print(hp.items)
    # hp.put(1)
    # print(hp.items)
    # hp.put(2)
    # print(hp.items)
    # hp.put(3)
    # print(hp.items)
    # hp.put(4)
    # print(hp.items)
    print(hp.values)
    hp.put(1,"a")
    print(hp.items)
    print(hp.values)
    print()
    hp.put(2,"b")
    print(hp.items)
    print(hp.values)
    print()
    print(hp.getKey(2))
    print(hp.getValue(2,"b"))
    print()
    hp.remove(1)
    print(hp.items)
    print(hp.values)
    print()
    hp.put(3,"c")
    hp.put(4, "d")
    print(hp.items)
    print(hp.values)



if __name__ == "__main__":
    test()
