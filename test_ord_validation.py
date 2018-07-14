import unittest
from ord_validation import ord_addr_validation

class Testord_validation(unittest.TestCase):

    def setUp(self):
        self.ord_valid1 = ord_addr_validation("35 Streetname","Halifax","NS","B2T1A4")
        self.ord_valid2 = ord_addr_validation("", "Halifax", "NS", "B2T1A4")
        self.ord_valid3 = ord_addr_validation("35 Streetname", "", "NS", "B2T1A4")
        self.ord_valid4 = ord_addr_validation("35 Streetname", "Halifax", "", "B2T1A4")
        self.ord_valid5 = ord_addr_validation("35 Streetname", "Halifax", "NS", "")
        self.ord_valid6 = ord_addr_validation("", "", "", "")

    def test_ord_address_valid(self):
        self.assertEqual(self.ord_valid1.ord_address_valid(),[])
        self.assertEqual(self.ord_valid2.ord_address_valid(),["Failure","Invalid Order","Invalid delivery address"])
        self.assertEqual(self.ord_valid3.ord_address_valid(), ["Failure", "Invalid Order", "Invalid delivery address"])
        self.assertEqual(self.ord_valid4.ord_address_valid(), ["Failure", "Invalid Order", "Invalid delivery address"])
        self.assertEqual(self.ord_valid5.ord_address_valid(), ["Failure", "Invalid Order", "Invalid delivery address"])
        self.assertEqual(self.ord_valid6.ord_address_valid(), ["Failure", "Invalid Order", "Invalid delivery address"])

if __name__ == '__main__':
    unittest.main()
