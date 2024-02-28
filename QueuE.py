
# -------------------------------------   using linked list    -----------------------------------


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next





class Queue:
    def __init__(self):     #self is the address of object
        self.front=None
        self.rear=None

    def enqueue(self,data):     # insertion
        node=Node(data)
        if self.rear==None:
            self.front=self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):      # deletion
        if self.front==None:
            print('underflow condition...')
        elif self.front==self.rear:
            self.front=self.rear=None
        else:
            self.front=self.front.next

    def traverse(self):
        if self.front==None:
            print('Queue is empty!')
        else:
            p=self.front
            while p!=None:
                print(p.data,end='->')
                p=p.next

    def size(self):
        p=self.front
        count=0
        while p!=None:
            count+=1
            p=p.next
        return count

    def Front(self):                # to see data at front
        if self.front == None:  return self.front
        return self.front.data

    def Rear(self):             # to see data at rear
        if self.rear == None:   return self.rear
        return self.rear.data

    def is_empty(self):             # to see if queue is empty
        return self.front==None






#  -----------------------------------     using array    -----------------------------------


class Queue:
    def __init__(self):
        self.front = self.rear = -1
        self.queue = []

    def enqueue(self, data):
        if self.rear == -1:
            self.queue.append(data)
            self.front +=1
            self.rear +=1
        else:
            self.queue.append(data)
            self.rear+=1

    def dequeue(self):
        if self.front == -1:
            print('underflow condition ... ')
        else:
            self.front+=1

    def traverse(self):
        if self.front == -1:
            print('queue is empty')
        else:
            p = self.front
            while p<=self.rear:
                print(self.queue[p], end = '->')
                p+=1
    @property
    def size(self):
        c=0
        p = self.front
        while p<=self.rear:
            c+=1
            p+=1
        return c

    @property
    def Front(self):
        if self.front == -1:    return self.front
        return self.queue[self.front]
    
    @property
    def Rear(self):
        if self.rear == -1: return self.rear
        return self.queue[self.rear]








        
        