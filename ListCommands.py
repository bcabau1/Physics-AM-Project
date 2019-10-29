class Node(object):

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_prev(self):
        return self.prev_node

    def set_prev(self, p):
        self.prev_node = p

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def to_string(self):
        return "Node value: " + str(self.data)

    def has_next(self):
        if self.get_next() is None:
            return False
        return True


class DoublyLinkedList(object):

    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.set_prev(new_node)
            self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                if this_node.get_prev() is not None:
                    if this_node.has_next():  # delete a middle node
                        this_node.get_prev().set_next(this_node.get_next())
                        this_node.get_next().set_prev(this_node.get_prev())
                    else:  # delete last node
                        this_node.get_prev().set_next(None)
                        self.last = this_node.get_prev()
                else:  # delete root node
                    self.root = this_node.get_next()
                    this_node.get_next().set_prev(self.root)
                self.size -= 1
                return True  # data removed
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == self.root:
                return False
            else:
                this_node = this_node.get_next()

    def print_list(self):
        print("Print List..........")
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())


def main():
    file = input("Enter file name: ")
    f = open(file)
    file1 = input("Write to file name: ")
    f1 = open(file1, "w")
    line = f.readline()
    xspeed = 3
    xdist = 0
    yspeed = 3
    ydist = 0
    linkedlist = DoublyLinkedList()
    for line in f:
        #line = f.readline()
        if line == '':
            break
        line = line.strip()
        line = line.split(';')
        line = list(map(float, line))
        for item in line:
            item = item * 1000
            item = int(item)
            linkedlist.add(item)
        if linkedlist.size > 2:
            print(linkedlist.print_list())
            temp1 = (linkedlist.last.get_prev()).get_data()
            temp2 = (((linkedlist.last.get_prev()).get_prev()).get_prev()).get_data()
            temp3 = linkedlist.last.get_data()
            temp4 = ((linkedlist.last.get_prev()).get_prev()).get_data()
            ydist = (temp2 - temp1)
            xdist = (temp4 - temp3)
            if xdist == 0:
                xdist = 1
            yspeed = (ydist * xspeed)/xdist
            if yspeed == 0:
                yspeed = xspeed
            print(temp1, temp2, temp3, temp4, "\n", xdist, ydist, yspeed, xspeed)
            f1.write("2HS X =" + str(xspeed) + " Y =" + str(yspeed) + "\n")
            f1.write("2HM X =" + str(temp3) + " Y =" + str(temp1) + "\n")
            linkedlist.remove(temp1)
            linkedlist.remove(temp3)


    f.close(), f1.close()


main()
