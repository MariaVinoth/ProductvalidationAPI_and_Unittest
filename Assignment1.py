from xml.dom import minidom
import dlr_auth
import ord_validation
import part_manager
import write_xml
import sys
import os.path

try:
    file = sys.argv[1]   # Receive the file name from command line
except IndexError:
    file = "orders.xml"
    print("Invalid input file-Taking the default file orders.xml")
    

if not file or not os.path.isfile(file):
    file = "orders.xml"
    print("Invalid input file-Taking the default file orders.xml")
    

input_doc = minidom.parse(file)  # Parsing the file using DOM

#Write the XML when the adress or the order item entry has errors
def write_xml_order_items(result):
    wrt_xml = write_xml.write_data_xml(result)
    final_result = wrt_xml.order_result()
    output = open("order_response.xml","w")
    output.write(final_result[0])

#Write the XML, the resultant of the part manager
def write_xml_order(result):
    wrt_xml = write_xml.write_data_xml(result)
    final_result = wrt_xml.ord_invalid()
    output = open("order_response.xml", "w")
    output.write(final_result[0])

#write the XML, when an ivalid dealer entry in the input
def write_xml_dlr(result):
    wrt_xml = write_xml.write_data_xml(result)
    final_result = wrt_xml.dlr_fail()
    output = open("order_response.xml", "w")
    output.write(final_result[0])


#validate the order - pass it to part manger for evaluation
def ord_validate(result):
    if not result:
        result3 = []
        result4= []
        for items in order_item:
            part_no = items.getElementsByTagName('partnumber')[0]
            qty = items.getElementsByTagName('quantity')[0]
            if part_no.firstChild and qty.firstChild:
                part_data = int(part_no.firstChild.data)
                qty_data = int(qty.firstChild.data)
                part_mgr = part_manager.part_manager(part_data, qty_data)
                result3 = part_mgr.ord_valid()

            else:  #when the order has blank order data
                result3.append("Failure")
                result3.append("Invalid Order")
                result3.append("Invalid order item entry")

            if not result3:
                result4.append(part_mgr.order_process())
            else:
                write_xml_order(result3)
                break

        if result4:
            write_xml_order_items(result4)

    else:
        write_xml_order(result)


#Validate the dealer
def dlr_xml_validate(dealer):
    for dlr in dealer:
        dlr_id = dlr.getElementsByTagName('dealerid')[0]
        dlr_key = dlr.getElementsByTagName('dealeraccesskey')[0]
        if dlr_id.firstChild and dlr_key.firstChild:
            dlr_id_data = dlr_id.firstChild.data
            dlr_key_data = dlr_key.firstChild.data
            val_dlr = dlr_auth.dealer_auth(dlr_id_data, dlr_key_data)
            result1 = val_dlr.dlr_validate()
        else: #when the dlr info is blank
            result1 = []
            result1.append("Failure")
            result1.append("Not authorized")

    return result1

#validate the address
def addr_xml_validate(address):
    for addrs in address:
        # name = addrs.getElementsByTagName('name')[0]
        street = addrs.getElementsByTagName('street')[0]
        city = addrs.getElementsByTagName('city')[0]
        province = addrs.getElementsByTagName('province')[0]
        postalcode = addrs.getElementsByTagName('postalcode')[0]

        if street.firstChild and city.firstChild and province.firstChild and postalcode.firstChild:
            street_data = street.firstChild.data
            city_data = city.firstChild.data
            province_data = province.firstChild.data
            postalcode_data = postalcode.firstChild.data
            val_ord_addr = ord_validation.ord_addr_validation(street_data, city_data, province_data, postalcode_data)
            result2 = val_ord_addr.ord_address_valid()

        else: #when the delivery address details are blank
            result2 = []
            result2.append("Failure")
            result2.append("Invalid Order")
            result2.append("Invalid delivery address")

    return result2



# Main portion

#retrieving blocks from XML

dealer = input_doc.getElementsByTagName('dealer')
order_item = input_doc.getElementsByTagName('item')
address = input_doc.getElementsByTagName('deliveryaddress')


if not dlr_xml_validate(dealer):
    result = addr_xml_validate(address)
    ord_validate(result)
else:
    result = dlr_xml_validate(dealer)
    write_xml_dlr(result)
