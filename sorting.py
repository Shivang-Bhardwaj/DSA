#-----------------------comparison based sorting -----------------------------








# l=[21,100,34,22,3,45,67,20,22,-1]


# def bubble_sort(A,n):
#     for round in range(n-1):
#         for i in range(n-round-1):
#             if A[i]>A[i+1]:
#                 A[i],A[i+1]=A[i+1],A[i]
#     print(A)






# def selection_sort(A,n):
#     for round in range(n-1):
#         smallest=round
#         for j in range(round+1,n):
#             if A[j]<A[smallest]:
#                 smallest=j
#         if smallest!=round:
#             A[round],A[smallest]=A[smallest],A[round]
#     print(A)







# def insertion_sort(A,n):
#     for i in range(1,n):
#         key=l[i]
#         j=i-1
#         while j>=0 and key<A[j]:
#             A[j+1]=A[j]
#             j=j-1
#         A[j+1]=key
#     print(A)







# def left(parent):
#     return 2*parent+1
# def right(parent):
#     return 2*parent+2

# def Max_heapify(A,heap_size,index):
#     l=left(index)
#     r=right(index)
#     if l<heap_size and A[index]<A[l]:
#         largest=l
#     else:
#         largest=index
#     if r<heap_size and A[largest]<A[r]:
#         largest=r
#     if largest!=index:
#         A[largest],A[index]=A[index],A[largest]
#         Max_heapify(A,heap_size,largest)

# def Build_a_Maxheap(A,n):
#     parent=n//2
#     while parent>=0:
#         Max_heapify(A,n,parent)
#         parent=parent-1

# def heap_sort(A,n):
#     Build_a_Maxheap(A,n)
#     heap_size=n
#     for i in range(n-1,0,-1):
#         A[0],A[heap_size-1]=A[heap_size-1],A[0]
#         heap_size=heap_size-1
#         Max_heapify(A,heap_size,0)
#     print(A)







# def Merge(A,start,mid,end):
#     l=[]
#     i=start
#     j=mid+1
#     while i<=mid and j<=end:
#         if A[i]<=A[j]:
#             l.append(A[i])
#             i+=1
#         else:
#             l.append(A[j])
#             j+=1
#     while i<=mid:
#         l.append(A[i])
#         i+=1

#     while j<=end:
#         l.append(A[j])
#         j+=1
#     A[start:end+1]=l
        

# def Merge_Sort(A,start,end):
#     if start<end:
#         mid=(start+end)//2
#         Merge_Sort(A,start,mid)
#         Merge_Sort(A,mid+1,end)
#         Merge(A,start,mid,end)
# Merge_Sort(l,0,9)
# print(l)








# def partition(A,low,high):
#     pivot=low
#     i=low
#     for j in range(low+1,high+1):
#         if A[j]<A[pivot]:
#             i+=1
#             A[i],A[j]=A[j],A[i]
#     A[i],A[pivot]=A[pivot],A[i]
#     print(A[low:high+1],end='')
#     return i

# def Quick_sort(A,low,high):
#     if low<high:
#         q=partition(A,low,high)
#         print(q)
#         Quick_sort(A,low,q-1)
#         Quick_sort(A,q+1,high)

# Quick_sort(l,0,9)
# print(l)








# ----------------------non comparison based sorting -----------------------------
                                # or 
# --------------------- linear time sorting---------------------------------




# l=[4,1,3,4,3]

# def counting_sort(A,n):
#     k=max(A)
#     B=A.copy()
#     C=[]
#     for i in range(k+1):
#         C.append(0)
#     for i in range(n):
#         C[A[i]]=C[A[i]]+1
#     for i in range(1,k+1):
#         C[i]=C[i]+C[i-1]
#     for i in range(n-1,-1,-1):
#         B[C[A[i]]-1]=A[i]
#         C[A[i]]=C[A[i]]-1
#     print(B)

# counting_sort(l,5)





    