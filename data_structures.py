class node():

    def __init__(self, value):
        self.value = value
        self.next = None



class linked_list():

    def __init__(self, node):
        self.head = node
        self.tail = node
        self.length = 1


    def push(self, node):
        self.tail.next = node
        self.tail = self.tail.next
        self.length +=1


    def pop(self): 
        i = self.head
        while i is not None:
            if i.next is self.tail:
                i.next = None
                self.tail = i
                self.length = self.length -1
            elif self.length == 1:
                self.head = None
                self.tail = None
                self.length == 0
            else:
                i = i.next


    def print_list(self):
        i = self.head
        while i is not None:
            print(i.value)
            i = i.next
        print("Length of the list is" + " " + str(self.length) + " nodes.")
        return list


    def clear(self):
        self.head = None
        self.tail = None
        print('list cleared')