import unittest
from write_xml import write_data_xml

class Testwrite_xml(unittest.TestCase):

    def setUp(self):
        result1 = ["Failure","Not authorized"]
        self.wrt_xml1 = write_data_xml(result1)
        result2 = ["Failure","Invalid Order","Invalid delivery address"]
        self.wrt_xml2 = write_data_xml(result2)
        result3 = ["Failure","Invalid Order","Invalid order item entry"]
        self.wrt_xml3 = write_data_xml(result3)
        result4 = [[1234,2,"Success", ""],[5678,25,"Failure","Invalid part"]]
        self.wrt_xml4 = write_data_xml(result4)
        result5 = [[1234, 2, "Success", ""], [5578, 3, "Success", ""],[1212,5,"Failure","Out of stock"]]
        self.wrt_xml5 = write_data_xml(result5)
        result6 = [[1234, 2, "Success", ""], [5578, 3, "Success", ""], [1213, 4, "Failure", "Out of stock"]]
        self.wrt_xml6 = write_data_xml(result6)
        result7 = [[9834, 2, "Failure", "Out of stock"],[2333, 3, "Failure", "no longer manufactured"]]
        self.wrt_xml7 = write_data_xml(result7)
        result8 = [[1555, 2, "Failure", "no longer manufactured"]]
        self.wrt_xml8 = write_data_xml(result8)
        result9 = [[1354, 2, "Failure", "Invalid part"],[1334, 2, "Failure", "Out of stock"],[1234,2,"Success", ""]]
        self.wrt_xml9 = write_data_xml(result9)


    def test_dlr_fail(self):
        result = "<order><result>Failure</result><error>Not authorized</error></order>"
        self.assertEqual(self.wrt_xml1.dlr_fail()[1],result)

    def test_ord_invalid(self):
        result2 = "<order><result>Failure</result><error>Invalid Order</error><errormessage>Invalid delivery address</errormessage></order>"
        result3 = "<order><result>Failure</result><error>Invalid Order</error><errormessage>Invalid order item entry</errormessage></order>"
        self.assertEqual(self.wrt_xml2.ord_invalid()[1],result2)
        self.assertEqual(self.wrt_xml3.ord_invalid()[1],result3)

    def test_order_result(self):
        result4 = "<order><orderitems><item><partnumber>1234</partnumber><quantity>2</quantity><result>Success</result><errormessage /></item><item><partnumber>5678</partnumber><quantity>25</quantity><result>Failure</result><errormessage>Invalid part</errormessage></item></orderitems></order>"
        result5 ="<order><orderitems><item><partnumber>1234</partnumber><quantity>2</quantity><result>Success</result><errormessage /></item><item><partnumber>5578</partnumber><quantity>3</quantity><result>Success</result><errormessage /></item><item><partnumber>1212</partnumber><quantity>5</quantity><result>Failure</result><errormessage>Out of stock</errormessage></item></orderitems></order>"
        result6 = "<order><orderitems><item><partnumber>1234</partnumber><quantity>2</quantity><result>Success</result><errormessage /></item><item><partnumber>5578</partnumber><quantity>3</quantity><result>Success</result><errormessage /></item><item><partnumber>1213</partnumber><quantity>4</quantity><result>Failure</result><errormessage>Out of stock</errormessage></item></orderitems></order>"
        result7 = "<order><orderitems><item><partnumber>9834</partnumber><quantity>2</quantity><result>Failure</result><errormessage>Out of stock</errormessage></item><item><partnumber>2333</partnumber><quantity>3</quantity><result>Failure</result><errormessage>no longer manufactured</errormessage></item></orderitems></order>"
        result8 = "<order><orderitems><item><partnumber>1555</partnumber><quantity>2</quantity><result>Failure</result><errormessage>no longer manufactured</errormessage></item></orderitems></order>"
        result9 = "<order><orderitems><item><partnumber>1354</partnumber><quantity>2</quantity><result>Failure</result><errormessage>Invalid part</errormessage></item><item><partnumber>1334</partnumber><quantity>2</quantity><result>Failure</result><errormessage>Out of stock</errormessage></item><item><partnumber>1234</partnumber><quantity>2</quantity><result>Success</result><errormessage /></item></orderitems></order>"
        self.assertEqual(self.wrt_xml4.order_result()[1],result4)
        self.assertEqual(self.wrt_xml5.order_result()[1], result5)
        self.assertEqual(self.wrt_xml6.order_result()[1], result6)
        self.assertEqual(self.wrt_xml7.order_result()[1], result7)
        self.assertEqual(self.wrt_xml8.order_result()[1], result8)
        self.assertEqual(self.wrt_xml9.order_result()[1], result9)

if __name__ == '__main__':
    unittest.main()
