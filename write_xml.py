import xml.etree.ElementTree as ET
from xml.dom import minidom


class write_data_xml:

    def __init__(self,result):
        self.result = result

    def dlr_fail(self): #Generate the XML structure for dealer error
        xml_result1 = []
        order = ET.Element('order')
        sub_elm1 = ET.SubElement(order,'result')
        sub_elm2 = ET.SubElement(order, 'error')
        sub_elm1.text = self.result[0]
        sub_elm2.text = self.result[1]

        xml_data = ET.ElementTree(order)
        root = xml_data.getroot()
        xml_result1.append(minidom.parseString(ET.tostring(root)).toprettyxml(indent="   "))
        xml_result = ET.tostring(order)
        xml_result1.append(xml_result.decode("utf-8"))
        return (xml_result1)

    def ord_invalid(self):  #Generate XML structure for invalid order
        xml_result1 = []
        order = ET.Element('order')
        sub_elm1 = ET.SubElement(order, 'result')
        sub_elm2 = ET.SubElement(order, 'error')
        sub_elm3 = ET.SubElement(order, 'errormessage')
        sub_elm1.text = self.result[0]
        sub_elm2.text = self.result[1]
        sub_elm3.text = self.result[2]

        xml_data = ET.ElementTree(order)
        root = xml_data.getroot()
        xml_result1.append(minidom.parseString(ET.tostring(root)).toprettyxml(indent="   "))
        xml_result = ET.tostring(order)
        xml_result1.append(xml_result.decode("utf-8"))
        return (xml_result1)

    def order_result(self):  #Generate XML structure for the status of the order
        xml_result1 = []
        item = {}
        partnumber = {}
        quantity = {}
        result = {}
        errormessage = {}

        order = ET.Element('order')
        orderitems = ET.SubElement(order, 'orderitems')
        result_len = len(self.result)
        for indx in range(result_len):
            item[indx] = ET.SubElement(orderitems, 'item')
            partnumber[indx] = ET.SubElement(item[indx], 'partnumber')
            quantity[indx] = ET.SubElement(item[indx], 'quantity')
            result[indx] = ET.SubElement(item[indx], 'result')
            errormessage[indx] = ET.SubElement(item[indx], 'errormessage')
            partnumber[indx].text = str(self.result[indx][0])
            quantity[indx].text = str(self.result[indx][1])
            result[indx].text = str(self.result[indx][2])
            errormessage[indx].text = str(self.result[indx][3])

        xml_data = ET.ElementTree(order)
        root = xml_data.getroot()
        xml_result1.append(minidom.parseString(ET.tostring(root)).toprettyxml(indent="   "))
        xml_result = ET.tostring(order)
        xml_result1.append(xml_result.decode("utf-8"))
        return (xml_result1)
