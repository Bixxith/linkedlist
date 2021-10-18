# LinkedList
Made from scratch linked list with different methods

### _*.append(value)_
Takes the supplied value, turns it into a node, and adds it to the end of the linkedlist.

### _*.prepend(value)_
Takes the supplied value, turns it into a node, and adds it to the beginning of the linkedlist.

### _*.pop()_
Removes the final node in the list.  It also returns the value held in that node. Functions like regular python .pop()

### _*.printList()_
Iterates through the list printing each item in the list on to a single line.  It then prints the length of the list on a seperate line.

### _*.returnByIndex(index)_
Given a position to use as an index, it returns the node located at that position.  This is used internally by other functions.
Index range functions like regular python index, starting with 0.

### _*.deleteValue(value)_
Takes the supplied value, looks for all of its occurances in the list, and then passes their indexes to the deletePosition method to be deleted.

### _*.deletePosition(index)_
Takes the supplied index number and deletes the node located at that position.

### _*.insertByIndex(value, index)_
Creates a node using the value provided and inserts it at the given index, shifting the previously located node to the right.

### _*.nodeSwap(index1, index2)_
Swaps the nodes located at index1 with the nodes located at index2.

### _*.length()_
Returns the current length of the linked list.

### _*.reverse()_
Reverses the entire linked list

### _*.removeDupes()_
Finds and deletes all duplicate values in the linked list.

### _*.returnNthToLast(Nth)_
Returns the Nth to last value in the linked list.  1st to last being the last item, 2nd to last being the next to last, etc.

### _*.counterOccurances()_
Counts how many of each value appear in the list.

### _*.moveTailtoHead()_
Swaps the head and tail currently, rather than just moving the tail.  Will revisit.

### _*.sum(llist2)_
Turns original and llist2 lists into integers and add them together to make a third list.  Idea from LeetCode

### _*.checkLoop()_
Checks to see if the linkedlist loops or not.  Not complete, broken if list contains True values or the number 1.

### _*.loopList()_
Links the tail to the head so the list loops.



