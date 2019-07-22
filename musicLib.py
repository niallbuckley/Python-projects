class Track(object):
    def __init__(self,name,artiste,timesplayed):
        self._name=name
        self._artiste=artiste
        self._timesplayed=timesplayed

    def __str__(self):
        return("%s,%s,%s"%(self._name,self._artiste,self._timesplayed))
    def play(self):
        self._timesplayed+=1
    def get_Name(self):
        return self._name
    def get_Artiste(self):
        return self._artiste


class DLLNode:
    def __init__(self,item,prevnode,nextnode):
        self.element=item
        self.next=nextnode
        self.prev=prevnode

    
class List:
    def __init__(self):
        self.head=DLLNode(None,None,None)
        self.tail=DLLNode(None,self.head,None)
        self.head.next=self.tail
        self.size=0
        self.cursor=None
        self.current=None

    def get_current(self):
        if self.cursor is None:
            print("List is empty")
        else:
            return self.cursor.element
    
    def add_current(self,item):
        newnode=DLLNode(item,None,None)
        if self.cursor is None:
            #Is Empty
            self.cursor=newnode
            self.head.next=self.cursor
            self.tail.prev=self.cursor
            self.cursor.next=self.tail
            self.cursor.prev=self.head
        
        else:
            #Not Empty
            newnode.next=self.current.next
            self.current.next=newnode
            newnode.prev=self.current
        self.current=newnode
        self.size+=1
    def move_to_front(self):
        if self.size==0:
            print("Library is empty cannot reset")
        else:
            self.cursor=self.head.next
        
  
    def remove_current(self):
        if self.size==0:
            return None
        else:
            cur_next=self.cursor.next
            cur_prev=self.cursor.prev
            cur_prev.next=cur_next
            cur_next.prev=cur_prev
            self.cursor.next=None
            self.cursor.prev=None
            self.cursor=cur_next
            self.size-=1
            
    def next(self):
        if self.size==0:
            print("Library is empty cannot go to next")
        elif self.cursor.next==self.tail:
            self.cursor=self.head.next
        else:
            self.cursor=self.cursor.next
           
        
        
        
    def prev(self):
        if self.size==0 or self.cursor is None:
            print("List is Empty")
        elif self.cursor.prev==self.head:
            self.cursor=self.tail.prev
        else:
            self.cursor=self.cursor.prev
                    
                     
    def length(self):
        return self.size
     
    def Sort_first(self):
        for i in range(self.size):
            self.cursor=self.head.next
            count=0
            while self.cursor.next!=self.tail and count!=self.size-1:
                count+=1
                if self.cursor.element.get_Name()>self.cursor.next.element.get_Name():
                    oldcursor=self.cursor.next
                    self.cursor.next=self.cursor.next.next
                    self.cursor.next.prev=self.cursor
                    self.cursor.prev.next=oldcursor
                    oldcursor.prev=self.cursor.prev
                    self.cursor.prev=oldcursor
                    oldcursor.next=self.cursor
                else:
                   List.next(self)
                   
    def Sort_second(self):
        for i in range(self.size):
            self.cursor=self.head.next
            count=0
            while self.cursor.next!=self.tail and count!=self.size-1:
                count+=1
                if self.cursor.element.get_Artiste()>self.cursor.next.element.get_Artiste():
                    oldcursor=self.cursor.next
                    self.cursor.next=self.cursor.next.next
                    self.cursor.next.prev=self.cursor
                    self.cursor.prev.next=oldcursor
                    oldcursor.prev=self.cursor.prev
                    self.cursor.prev=oldcursor
                    oldcursor.next=self.cursor
                else:
                    List.next(self)
    def Search(self,substring):
        in_='False'
        for i in range(self.size):
            if substring in self.cursor.element.get_Name() or substring in self.cursor.element.get_Artiste():
                in_='True'
            elif self.cursor.next==self.tail:
                self.cursor=self.head.next
            else:
                self.cursor=self.cursor.next
        print(in_)
    def play(self):
        if self.cursor is None:
            print("Library is Empty")
        else:
            self.cursor.element.play()
        
    def __str__(self):
        """ Return a string representation of the list. """
        outstr = ""
        node = self.head.next
        while  node and node!=self.tail:
            outstr = outstr + '(' + str(node.element) +")"+  "\n" 
            node = node.next
        return outstr


class MusicLibrary:
    def __init__(self):
        self.lib=List()
    def add_track(self,track):
        self.lib.add_current(track)
    def get_current(self):
        print("Current Track: %s"%(self.lib.get_current()))
    def next_track(self):
        self.lib.next()
    def prev_track(self):
        self.lib.prev()
    def reset(self):
        self.lib.move_to_front()
    def play(self):
        self.lib.play()
        print("Currently Playing: %s"%(self.lib.get_current()))
    def remove_current(self):
        self.lib.remove_current()
    def length(self):
        self.lib.length()
    def sort_name(self):
        self.lib.Sort_first()
    def sort_artiste(self):
        self.lib.Sort_second()
    def search_substring(self,substring):
        self.lib.Search(substring)
    
    def __str__(self):
        return("%s"%(self.lib.__str__()))
        
        
    
def main():
    
    t1=Track("Say you wont let go","James Arthur",10)
    t2=Track("The greatest","Sia feat Kendrick Lamar",190)
    t3=Track("Closer","Chainsmokers feat Halsey",100)

    MusicLib=MusicLibrary()
    MusicLib.add_track(t1)
    MusicLib.add_track(t2)
    MusicLib.add_track(t3)
    print(MusicLib)
    print("---")
    MusicLib.play()
    MusicLib.sort_name()
    MusicLib.next_track()
    MusicLib.get_current()
    print("---")
    MusicLib.prev_track()
    MusicLib.prev_track()
    MusicLib.play()
    print("---")
    MusicLib.remove_current()
    print(MusicLib)
    print("---")
    t4=Track("My Way","Calvin Harris",233)
    MusicLib.add_track(t4)
    MusicLib.sort_artiste()
    MusicLib.prev_track()
    MusicLib.play()
    print("---")
    print(MusicLib)
    print("---")
    MusicLib.sort_name()
    print(MusicLib)
    MusicLib.search_substring("Clo")
    MusicLib.search_substring("nia")
  
if __name__=='__main__':
    main()
