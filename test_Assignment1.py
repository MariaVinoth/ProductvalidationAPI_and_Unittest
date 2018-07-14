from xml.dom import minidom
import unittest
import Assignment1


class TestAssignment1(unittest.TestCase):


    def test_dlr_xml_validate(self):
        input_doc1 = minidom.parse('test1.xml')
        input_doc2 = minidom.parse('test2.xml')
        input_doc3 = minidom.parse('test3.xml')
        input_doc4 = minidom.parse('test4.xml')

        dealer1 = input_doc1.getElementsByTagName('dealer')
        dealer2 = input_doc2.getElementsByTagName('dealer')
        dealer3 = input_doc3.getElementsByTagName('dealer')
        dealer4 = input_doc4.getElementsByTagName('dealer')

        self.assertEqual(Assignment1.dlr_xml_validate(dealer1),[])
        self.assertEqual(Assignment1.dlr_xml_validate(dealer2),["Failure","Not authorized"] )
        self.assertEqual(Assignment1.dlr_xml_validate(dealer3), ["Failure","Not authorized"])
        self.assertEqual(Assignment1.dlr_xml_validate(dealer4), ["Failure","Not authorized"])

    def test_addr_xml_validate(self):
        input_doc1 = minidom.parse('test1.xml')
        input_doc2 = minidom.parse('test2.xml')
        input_doc3 = minidom.parse('test3.xml')
        input_doc4 = minidom.parse('test4.xml')

        address1 = input_doc1.getElementsByTagName('deliveryaddress')
        address2 = input_doc2.getElementsByTagName('deliveryaddress')
        address3 = input_doc3.getElementsByTagName('deliveryaddress')
        address4 = input_doc4.getElementsByTagName('deliveryaddress')

        self.assertEqual(Assignment1.addr_xml_validate(address1),[])
        self.assertEqual(Assignment1.addr_xml_validate(address2), ["Failure","Invalid Order","Invalid delivery address"])
        self.assertEqual(Assignment1.addr_xml_validate(address3), ["Failure","Invalid Order","Invalid delivery address"])
        self.assertEqual(Assignment1.addr_xml_validate(address4), ["Failure","Invalid Order","Invalid delivery address"])


if __name__ == '__main__':
    unittest.main()

