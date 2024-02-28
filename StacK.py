#  ------------------------------------ using linked list--------------------------------------------

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

# top=None   #pointer pointing to the top of stack


class Stack:

    def __init__(self) -> None:
        self.top=None     #pointer pointing to the top of stack

    def push(self,data):
        node=Node(data,self.top)
        self.top=node 

    def pop(self):
        if self.top==None:
            print('underflow condition...')
        else:
            self.top=self.top.next

    def peek(self):
        if self.top==None:
            return self.top
        return self.top.data

    def size(self):
        p=self.top
        count=0
        while p!=None:
            count+=1
            p=p.next
        return count

    def is_empty(self):
        return self.size()==0


    def traverse(self):
        if self.top==None:
            print('Stack is empty...')
        else:
            p=self.top
            while p!=None:
                print(p.data,end=',')
                p=p.next



#  --------------------------------------- using array -------------------------------------------

class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        self.top+=1

    def pop(self):
        if self.top == -1:
            return 'underflow condition'
        self.top-=1
        return self.stack.pop()
        
    def peek(self):
        if self.top == -1:  return 'Stack is empty'
        return self.stack[self.top]