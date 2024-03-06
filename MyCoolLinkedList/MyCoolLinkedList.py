class MyCoolLinkedList:
    def __init__(self):
        self.my_object = None
        self.next = None

    def append_my_object(self, myObject):
        if self.my_object is None:
            self.my_object = myObject
        else:
            if self.next is None:
                self.next = MyCoolLinkedList()
                self.next.my_object = myObject
            else:
                self.next.append_my_object(myObject)

    def get_my_object(self, index):
        if index != 0:
            if self.next is None: return None
            return self.next.get_my_object(index - 1)
        else:
            return self.my_object

    def delete_my_object(self, index):
        if index == 0: return self.next

        b = MyCoolLinkedList()
        for i in range(index):
            if self.get_my_object(i) is not None:
                b.append_my_object(self.get_my_object(i))

        b.append_list(self.get_sub_list(index + 1))
        return b

    def get_sub_list(self, start_index):
        if start_index == 0:
            return self
        else:
            if self.next is None: return None
            return self.next.get_sub_list(start_index - 1)

    def append_list(self, myList):
        if myList is not None and myList.my_object is not None:
            self.append_my_object(myList.get_my_object(0))

            while myList.next is not None:
                myList = myList.next
                self.append_my_object(myList.get_my_object(0))
        return self

    def __str__(self):
        if self.my_object is None: return ""
        if self.next is None: return self.my_object.__str__()
        return self.my_object.__str__() + "/" + self.next.__str__()
