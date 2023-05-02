class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        # create a new instance of our Node class using the given value
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    def add_to_back(self,val):
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner=runner.next
        runner.next=new_node
        return self
    def print_values(self):
        if self.head ==None:
            return self
        runner = self.head
        while runner != None:
            print(runner.value)
            runner=runner.next
        return self
    def remove_from_front(self):
        if self.head ==None:
            return self
        temp = self.head.next
        del self.head
        self.head=temp
        return self
    def remove_from_back(self):
        if self.head ==None:
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        removed = runner
        del runner
        runner = self.head
        while runner.next != removed:
            runner = runner.next
        runner.next = None
        del removed
        return self
    def remove_val(self,val):
        if self.head.value == val:
            self.remove_from_front()
        else:
            runner = self.head
            while runner.next != None and runner.value != val:
                runner = runner.next
            if runner.next == None and runner.value == val:
                self.remove_from_back()
            elif runner.next != None and runner.value==val:
                previous = self.head
                while previous.next != runner:
                    previous = previous.next
                previous.next = runner.next
                del runner
            else:
                print("Value doesn't exist")
        return self
    def insert_at(self,val,n):
        new_node = SLNode(val)
        length=0
        if self.head != None:
            length += 1
            runner = self.head
            while runner.next != None:
                runner = runner.next
                length += 1
        if n>length or n<0:
            print("Index Out of Range")
        elif n==0:
            self.add_to_front(val)
        elif n==length:
            runner.next = new_node
        else:
            counter = 1
            runner=self.head
            while counter != n:
                runner = runner.next
                counter+=1
            new_node.next = runner.next
            runner.next = new_node
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values().remove_from_front().print_values().remove_from_back().print_values()
print()
test_list = SList()
test_list.add_to_front(1).add_to_back(2).add_to_back(3).add_to_back(4).add_to_back(5).print_values()
print()
test_list.remove_val(6).remove_val(2).print_values().remove_val(1).print_values().remove_val(5).print_values()
print()

test_list2 = SList()
test_list2.add_to_front(1).add_to_back(2).add_to_back(4).add_to_back(5).print_values()
print()
test_list2.insert_at(3,2).print_values()
print()
test_list2.insert_at(0,0).insert_at(6,6).print_values()