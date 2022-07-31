"""
make the singly linked list of the in the python
from the scrath implementation 
"""


class node:
    """
    Make the node of the list with the val and next
    default initilaized as None
    """

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class linked_list:
    """
    The linked list class to make the list
    with using the nodes
    """

    def __init__(self):
        self.head = None

    def insert_element(self, val):
        """
        The insert the element in the head or after it
        Args:
                val (int) : the node val
        Returns:
                None
        """
        new_node = node(val)
        if self.head == None:
            self.head = new_node

        else:
            curr = self.head
            while True:
                if curr.next is None:
                    curr.next = new_node
                    break
                curr = curr.next

        return "the value is inserted"

    def print_list(self):
        curr = self.head
        while True:
            if curr.next is None:
                print(curr.val)
                break
            print(curr.val)
            curr = curr.next

        return "the list is printed"

    def delete_element(self, val):
        """
        To delete the  element in the list
        Args:
                val(int) : the value to search for
        Return:
                None
        """
        # make the node
        new_node = node(val)

        curr = self.head
        # start the loop and find the curr value

        while True:
            # delete the head first if found
            if new_node.val == self.head.val:

                self.head = curr.next

                print("The elememt is deleted and it is head node")
                break

            # delete the middle node

            elif curr.next.val == new_node.val:
                # delete the value now

                curr.next = curr.next.next
                print("The element is found and deleted from the list")
                break

            elif curr.next is None:
                print("the element is not found")
                break

            curr = curr.next


if __name__ == "__main__":
    """
    The linked list is as follows
    4->5->6->7->8->9->10
    delete the element 6 from the linked list
    ------------------------------------------
    new linked list
    4->5->7->8->9->10
    """
    my_list = linked_list()
    my_list.insert_element(4)
    my_list.insert_element(5)
    my_list.insert_element(6)
    my_list.insert_element(7)
    my_list.insert_element(8)
    my_list.insert_element(9)
    my_list.insert_element(10)

    print("-----------------------deleting the value in the linked_list---------------")

    my_list.delete_element(6)

    print(" -------------------- the list values  are being printed --------------- ")

    print(my_list.print_list())
