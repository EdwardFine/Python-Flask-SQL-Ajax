class DList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_end(self,val):
        new_node = DLNode(val)
        if self.tail == None and self.head == None:
            self.start_list(new_node)
        else:
            tracker = self.tail
            tracker.next = new_node
            new_node.previous = tracker
            new_node.next = self
            self.tail = new_node
        return self
    def add_to_start(self,val):
        new_node = DLNode(val)
        if self.tail == None and self.head == None:
            self.start_list(new_node)
        else:
            runner = self.head
            runner.previous = new_node
            new_node.next = runner
            new_node.previous = self
            self.head = new_node
        return self
    def start_list(self,node):
        self.head = node
        self.tail = node
        node.next = self
        node.previous = self
        return self
    def print_nodes(self):
        runner = self.head
        while runner != self:
            print(f"Value: {runner.value}\nNext: {runner.next}\nPrevious: {runner.previous}")
            runner = runner.next
        return self
    def delete_val(self,val):
        runner = self.head
        tracker= self.tail
        try:
            while runner.value != val and tracker.value != val:
                runner = runner.next
                tracker = tracker.previous
        except AttributeError:
            print("Value does not exist")
            return self
        if runner.value == val:
            temp_previous = runner.previous
            temp_next = runner.next
        else:
            temp_previous = tracker.previous
            temp_next = tracker.next
        temp_previous.next = temp_next
        temp_next.previous = temp_previous
        return self
    def delete_index(self,n):
        length = 0
        runner=self.head
        while runner != self:
            length +=1
            runner=runner.next
        if n<0 or n>=length:
            print("Index out of range")
        elif n==0:
            self.remove_start()
        elif n==length-1:
            self.remove_end()
        else:
            current_node = self.head
            count =0
            while count != n:
                current_node = current_node.next
                count +=1
            next_node = current_node.next
            previous_node = current_node.previous
            next_node.previous = previous_node
            previous_node.next = next_node
            del current_node
        return self
    def remove_start(self):
        temp = self.head
        self.head = temp.next
        temp.next.previous = self
        return self
    def remove_end(self):
        temp = self.tail
        self.tail = temp.previous
        temp.previous.next = self
        return self
    def insert_node(self,val,n):
        new_node = DLNode(val)
        if self.tail == None and self.head == None:
            self.start_list(new_node)
        else:
            length = 0
            runner=self.head
            while runner != self:
                length +=1
                runner=runner.next
            if n<0 or n>length:
                print("Index out of range")
                del new_node
            elif n==0:
                self.add_to_start(val)
                del new_node
            elif n==length:
                self.add_to_end(val)
                del new_node
            else:
                counter =0
                index_node=self.head
                while counter != n:
                    index_node = index_node.next
                    counter += 1
                back_one = index_node.previous
                new_node.next = index_node
                new_node.previous = back_one
                index_node.previous= new_node
                back_one.next = new_node
        return self

class DLNode:
    def __init__(self,val):
        self.value = val
        self.next = None
        self.previous = None


testList = DList()
testList.add_to_end(2).add_to_end(3).add_to_start(1).print_nodes()
testList.delete_val(8).print_nodes()
testList.insert_node(2.5,2).print_nodes().add_to_end(5).insert_node(4,4).delete_val(2).print_nodes()
testList.delete_index(4).print_nodes().delete_index(0).print_nodes()