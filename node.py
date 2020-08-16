"""
node.py
author: James heliotis
description: A linkable node class for use in stacks, queues, and linked lists
"""

class LinkedNode:

    __slots__ = "value", "next"

    def __init__( self, value,next=None ):
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def setValue(self,newValue):
        self.value=newValue

    def getNext(self):
        return self.link

    def setNext(self,nextNode):
        self.next=nextNode

    def __str__( self ):
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str( self.value )

    def __repr__( self ):
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "LinkedNode(" + repr( self.value ) + "," + \
               repr( self.next ) + ")"

def test():
    nodes = LinkedNode( 1, LinkedNode( "two", LinkedNode( 3.0 ,None) ) )
    n = nodes
    while n != None:
        print( n.value )#
        n = n.next
    print()
    print( nodes )
    print( repr( nodes ) )

if __name__ == "__main__":
    test()
