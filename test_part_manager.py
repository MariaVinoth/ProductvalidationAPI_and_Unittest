import unittest
from part_manager import part_manager

class Testpart_manager(unittest.TestCase):

    def setUp(self):
        self.part_mgr1 = part_manager(1234,4)
        self.part_mgr2 = part_manager(0, 4)
        self.part_mgr3 = part_manager(-12, 4)
        self.part_mgr4 = part_manager(1234, 0)
        self.part_mgr5 = part_manager(-12, -1)
        self.part_mgr6 = part_manager(0, 0)
        self.part_mgr7 = part_manager(3123,3)
        self.part_mgr8 = part_manager(1212,4)
        self.part_mgr9 = part_manager(2311,3)
        self.part_mgr10 = part_manager(4122,2)
        self.part_mgr11 = part_manager(7543,3)
        self.part_mgr12 = part_manager(7321,3)


    def test_ord_valid(self):
        self.assertEqual(self.part_mgr1.ord_valid(),[])
        self.assertEqual(self.part_mgr2.ord_valid(), ["Failure","Invalid Order","Invalid order item entry"])
        self.assertEqual(self.part_mgr3.ord_valid(), ["Failure", "Invalid Order", "Invalid order item entry"])
        self.assertEqual(self.part_mgr4.ord_valid(), ["Failure", "Invalid Order", "Invalid order item entry"])
        self.assertEqual(self.part_mgr5.ord_valid(), ["Failure", "Invalid Order", "Invalid order item entry"])
        self.assertEqual(self.part_mgr6.ord_valid(), ["Failure", "Invalid Order", "Invalid order item entry"])

    def test_order_process(self):
        self.assertEqual(self.part_mgr7.order_process(),[3123,3,"Success",""])
        self.assertEqual(self.part_mgr8.order_process(),[1212,4,"Failure","Out of stock"] )
        self.assertEqual(self.part_mgr9.order_process(),[2311,3,"Failure","Out of stock"] )
        self.assertEqual(self.part_mgr10.order_process(),[4122,2,"Failure","no longer manufactured"] )
        self.assertEqual(self.part_mgr11.order_process(),[7543,3,"Failure","Invalid part"] )
        self.assertEqual(self.part_mgr12.order_process(), [7321,3,"Failure","Invalid part"])


if __name__ == '__main__':
    unittest.main()
