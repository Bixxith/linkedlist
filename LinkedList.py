class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None


    # Adds a new node to the end of the Linked List
    def append(self, data):
        newNode = Node(data)
        head = self.head

        # Checks to see if there is any other nodes, if not then it sets itself as the head node.
        if not self.head:
            self.head = newNode

        # Loops through until it reaches the final node to place itself
        else:
            while head.next:
                head = head.next
            head.next = newNode


    # Adds a new node to the front of the Linked List
    def prepend(self, data):
        newNode = Node(data)

        # Checks to see if there is any other nodes, if not then it sets itself as the head node.
        if not self.head:
            self.head = newNode

        # Swaps places with the head node
        else:
            newNode.next = self.head
            self.head = newNode


    # Removes and returns the data from the last node
    def pop(self): 
        if self.length() > 0:
            tail = self.head

            for i in range(self.length()-2):
                tail = tail.next

            # Copies the node before deleting it so that we can return the data from it after deletion
            holder = tail.next
            tail.next = None

            return holder.data


    # Prints all of the nodes contained in the list and also prints the length of the list.
    def printList(self):
        curNode = self.head

        while curNode:
            print(curNode.data, end=' ')
            curNode = curNode.next
        print(f'\nLength is {self.length()}')


    # Returns the data from the node at the specified index
    def returnbyIndex(self, pos):
        copyNode = self.head
        counter = 0
        if pos >= self.length():
            raise Exception(f'Invalid Index.  Please choose an index between 0 and {self.length()-1}')
        while counter != pos:
            counter += 1
            copyNode = copyNode.next
        if not copyNode:
            print('FUCK')
        return copyNode
    

    # Deletes the nodes containing the specified values by checking where they occur in the index and then passing the index list to the deletePosition function.
    def deleteValue(self, value):
        curNode = self.head
        counter = 0
        indexList = []

        while curNode:
            if curNode.data == value:
                print(curNode.data, value)
                indexList.append(counter)
            curNode = curNode.next
            counter += 1
        indexList.sort(reverse=True)

        for i in indexList:
            self.deletePosition(i)


    # Deletes the node in a certain index position and makes sure the nodes maintain a connection.
    def deletePosition(self, pos):
        joinNode1 = self.head
        joinNode2 = self.head

        if pos == 0:
            deleteFirst = self.head
            self.head = deleteFirst.next

        elif pos == self.length():

            for i in range(pos-1):
                joinNode1 = joinNode1.next 
            joinNode1.next = None

        elif pos < self.length():

            for i in range(pos-1):
                joinNode1 = joinNode1.next 

            for i in range(pos+1):
                joinNode2 = joinNode2.next

            joinNode1.next = joinNode2


    # Inserts a node based on the given index
    def insertbyIndex(self, data, pos):
        copyNode1 = self.head
        copyNode2 = self.head
        newNode = Node(data)
        if pos == 0:
            self.prepend(data)
        elif pos == self.length():
             self.append(data)
        else:
            for i in range(pos):
                copyNode1 = copyNode1.next
            print(copyNode1.data)
            newNode.next = copyNode1

            for i in range(pos-1):
                copyNode2 = copyNode2.next
            copyNode2.next = newNode
            

    # Returns the number of nodes contained in the linked list.
    def length(self):
        curNode = self.head
        counter = 1
        while curNode.next:
            counter += 1
            curNode = curNode.next
        return counter


    # Swaps two specified nodes by index position.   ### NOT FINISHED ###
    def nodeSwap(self, pos1, pos2):
        node1 = self.returnbyIndex(pos1)
        node1 = node1.data
        node2 = self.returnbyIndex(pos2)
        node2 = node2.data

        self.deletePosition(pos1)
        self.insertbyIndex(node2, pos1)

        self.deletePosition(pos2)
        self.insertbyIndex(node1, pos2)


    # Reverses the linked list 
    def reverse(self):
        prevNode = None
        curNode = self.head
        while curNode:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        self.head = prevNode


    # Removes all duplicates contained in the linkedlist.
    def removeDupes(self):
        counter = 0
        copyNode = self.head
        dupes = set()
        while copyNode:
            if not copyNode.data in dupes:
                dupes.add(copyNode.data)
                counter += 1
                copyNode = copyNode.next
            else:
                self.deletePosition(counter)
                copyNode = copyNode.next


    # return nth to last node
    def returnNthtoLast(self, nth):
        length = self.length()
        nthIndex = length - nth
        return(self.returnbyIndex(nthIndex))


    # Counts the number of times each item in the linkedlist occurs.
    def countOccurances(self):
        occurs = dict()
        copyNode = self.head
        while copyNode:
            if not copyNode.data in occurs:
                occurs[copyNode.data] = 1
            else:
                occurs[copyNode.data] += 1
            copyNode = copyNode.next
        for x in occurs:
            print(f'{x} occurs {occurs[x]} times')


    # move tail to head
    def moveTailtoHead(self):
        self.nodeSwap(0, self.length()-1)   


    # Creates a new list to return the sum of two lists ### LEET CODE ###
    def sum(self, list2):
        slist1 = []
        slist2 = []
        copyNode = self.head

        while copyNode:
            slist1.append(copyNode.data)
            copyNode = copyNode.next

        copyNode2 = list2.head

        while copyNode2:
            slist2.append(copyNode2.data)
            copyNode2 = copyNode2.next

        sum1 = ''
        sum2 = ''

        for i in range(len(slist1)-1, -1, -1):
            sum1 += str(slist1[i])
        for j in range(len(slist2)-1, -1, -1):
            sum2 += str(slist2[j])

        sum3 = str(int(sum1)+int(sum2))
        twoSum = LinkedList()

        for k in range(len(sum3)):
            twoSum.append(sum3[k])

        twoSum.printList()
    

    # Checks the loop to see if it loops.  If the loop makes it all the way around and finds a node with the data TRUE then it prooves a loop.
    # If the checker makes it all the way to the end it will throw an AttributeError because the finaly node will be of the Nonetype and this will mean that it does not loop.
    def checkLoop(self):
        copyNode = self.head

        try:
            while copyNode.data != True:
                copyNode.data = True
                copyNode = copyNode.next
            print('Does Loop')

        except AttributeError:
            print("Does Not Loop")


    # Attaches the tail of the linkedlist to the head so that the linkedlist loops.
    def loopList(self):
        copyNode = self.head

        while copyNode.next:
            copyNode = copyNode.next
        copyNode.next = self.head


