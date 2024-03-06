import unittest

from MyCoolLinkedList import MyCoolLinkedList


class MyCoolLinkedListTest(unittest.TestCase):
    def test_str(self):
        my_list = MyCoolLinkedList()
        my_list.my_object = 10

        my_list2 = MyCoolLinkedList()
        my_list2.my_object = 2837

        my_list3 = MyCoolLinkedList()
        my_list3.my_object = "p"

        my_list.next = my_list2
        my_list2.next = my_list3

        self.assertEqual(my_list.__str__(), "10/2837/p")

    def test_append_my_object(self):
        my_list = MyCoolLinkedList()
        my_list.append_my_object("Hallo")
        my_list.append_my_object("Welt")

        self.assertEqual(my_list.my_object, "Hallo")
        self.assertEqual(my_list.next.my_object, "Welt")

    def test_get_my_object(self):
        my_list = MyCoolLinkedList()
        my_list.my_object = 10

        my_list2 = MyCoolLinkedList()
        my_list2.my_object = 2837

        my_list3 = MyCoolLinkedList()
        my_list3.my_object = "p"

        my_list.next = my_list2
        my_list2.next = my_list3

        self.assertEqual(my_list.get_my_object(2), "p")

    def test_get_sub_list(self):
        my_list = MyCoolLinkedList()
        my_list.my_object = 10

        my_list2 = MyCoolLinkedList()
        my_list2.my_object = 2837

        my_list3 = MyCoolLinkedList()
        my_list3.my_object = "p"

        my_list.next = my_list2
        my_list2.next = my_list3

        self.assertEqual(my_list.get_sub_list(1), my_list2)

    def test_delete_my_object(self):
        my_list = MyCoolLinkedList()
        my_list.my_object = 10

        my_list2 = MyCoolLinkedList()
        my_list2.my_object = 2837

        my_list3 = MyCoolLinkedList()
        my_list3.my_object = "p"

        my_list.next = my_list2
        my_list2.next = my_list3

        my_list_control = MyCoolLinkedList()
        my_list_control.my_object = 10

        my_list2_control = MyCoolLinkedList()
        my_list2_control.my_object = "p"

        my_list_control.next = my_list2_control

        self.assertEqual(my_list.delete_my_object(1).__str__(), my_list_control.__str__())

    def test_append_list(self):
        my_test_list1 = MyCoolLinkedList()
        my_test_list1.append_my_object(1)
        my_test_list1.append_my_object(2)
        my_test_list1.append_my_object(3)
        my_test_list2 = MyCoolLinkedList()
        my_test_list2.append_my_object(4)
        my_test_list2.append_my_object(5)
        my_test_list2.append_my_object(6)

        self.assertEqual(my_test_list1.append_list(my_test_list2).__str__(), "1/2/3/4/5/6")
        pass

if __name__ == '__main__':
    unittest.main()
