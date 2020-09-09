class Node:
  def __init__(self,ele):
    self.element=ele
    self.next=None
    self.prev=None
class DCLL:
    def __init__(self):
     self.head=None
    def insertbeg(self,ele):
        newnode=Node(ele)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head
            newnode.prev=self.head
        else:
            newnode.next=self.head
            position=self.head
            while position.next!=self.head:
             position=position.next
            position.next=newnode
            newnode.prev=position
            self.head=newnode
    def insertmid(self,pos,ele):
        newnode=Node(ele)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head
            newnode.prev=self.head
        else:
            position=self.head
            while position.next!=self.head and position.element!=pos:
               position=position.next
            newnode.next=position.next
            position.next.prev=newnode
            position.next=newnode
            newnode.prev=position
    def insertend(self,ele):
        newnode=Node(ele)
        if self.head == None:
         self.head=newnode
        else:
         position=self.head
         while position.next != self.head:
            position=position.next
         position.next=newnode
        newnode.previous=position
        newnode.next=self.head
        self.head.previous=newnode
    def deletebeg(self):
         if self.head==None:
             print("List is empty....")
         elif self.head.next==self.head:
            print("deleted item ",self.head.element)
            self.head=None
         else: 
            position=self.head
            while position.next!=self.head:
             position=position.next
            print("deleted item ",self.head.element)
            self.head=self.head.next
            position.next=self.head
            self.head.prev=position
    def deletemid(self,ele):
        if self.head==None:
            print("list is empty")
        else:
            position=self.head
            while position.next!= self.head and position.element!=ele:
                position=position.next
            print("deleted item",position.element)
            position.prev.next=position.next
            position.next.prev=position.prev
    def deleteEnd(self,ele):
        if self.head==None:
             print("list is empty")
        else:
             position=self.head
             while position.next!=self.head:
                 position=position.next
             print("deleted item",position.element)
             position.prev.next=self.head
             self.head.prev=position.prev
    def find(self,ele):
        position=self.head
        flag=False
        if self.head.element==ele:
             flag=True
        else:
            position=self.head
            while position!=self.head:
                 if position==ele:
                   flag=True
                   break
                 position=position.next
        if flag:
             print("element found")
        else:
            print("element not found")
    def traverse(self):
        if self.head==None:
            print("list is empty")
        else:
             print(self.head.element,end=" ")
             position=self.head.next
             while position!=self.head:
                print(position.element,end=" ")
                position=position.next
             print()

dcll=DCLL()
while True:
  print("1.Insert beg,2.Insert mid,3.Insert end")
  print("4.delete beg 5.delete mid,6.delete end")
  print("7.find,8.traverse,9.exit")
  ch=int(input("enter your choice"))
  if ch==1:
    ele=int(input("enter element"))
    dcll.insertbeg(ele)
  elif ch==2:
    pos=int(input("enter position"))
    ele=int(input("enter element"))
    dcll.insertmid(pos,ele)
  elif ch==3:
    ele=int(input("enter element"))
    dcll.insertend(ele)
  elif ch==4:
    dcll.deletebeg()
  elif ch==5:
    ele=int(input("enter element"))
    dcll.deletemid(ele)
  elif ch==6:
    dcll.deleteEnd(ele)
  elif ch==7:
    ele=int(input("enter element"))
    dcll.find(ele)
  elif ch==8:
    dcll.traverse()
  elif ch==9:
     break
