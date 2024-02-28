



class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next


start=None     # pointer pointing to the first node






def insertBeg(data):
    global start
    node=Node(data,next=start)
    if start==None:
        start=node
    else:
        start=node
        start.next.prev=node



def insertMid(data,pos):
    if pos<=0 or pos>get_lenght():
        print('Invalid position!')
    elif pos==1:
        insertBeg(data)
    else:
        p=start
        count=0
        node=Node(data)
        while p!=None:
            count+=1
            if count==pos:
                node.next=p
                p.prev.next=node
                node.prev=p.prev
                p.prev=node
                break
            p=p.next


def insertEnd(data):
    global start
    node=Node(data)
    if start==None:
        start=node
    else:
        p=start
        while p.next!=None:
            p=p.next
        p.next=node
        p.next.prev=p



def get_lenght():
    p=start
    count=0
    while p!=None:
        count+=1
        p=p.next
    return count



def delFirst():
    global start
    if start==None:
        print('Nothing to delete...')
    else:
        start=start.next
        if start==None:
            pass
        else:
            start.prev=None


def delMid(pos):
    p=start
    count=0
    if pos<=0 or pos>get_lenght():
        print('invalid postion!')
    elif pos==1:
        delFirst()
    elif pos==get_lenght():
        delEnd()
    else:
        while p!=None:
            count+=1
            if count==pos:
                p.prev.next=p.next
                p.next.prev=p.prev
                break
            p=p.next


def delEnd():
    if get_lenght()==0 or start.next==None:
        delFirst()
    else:
        p=start
        while p.next!=None:
            p=p.next
        p.prev.next=None
        del p    # actually last node is not deleted.it is detached.so to delete it, i have used this





def traverseF():
    p=start
    if p==None:
        print('linked list is empty...')
    else:
        while p!=None:
            print(p.data,'-->',end='')
            p=p.next


def traverseR():
    p=start
    if start==None:
        print('linked list is empty...')
    else:
        while p.next!=None:
            p=p.next
        while p!=None:
            print('<--',p.data,end='')
            p=p.prev






if __name__=='__main__':
    insertEnd(1)
    # insertEnd(2)
    # insertEnd(3)
    # insertEnd(4)
    traverseF()
    print()
    traverseR()

