class ord_addr_validation:

    blank = ''

    def __init__(self,street,city,province,postalcode):
        self.street = street
        self.city = city
        self.province = province
        self.postalcode = postalcode

    def ord_address_valid(self):
        result = []
        if(self.street == ord_addr_validation.blank or self.city == ord_addr_validation.blank or self.province == ord_addr_validation.blank
            or self.postalcode == ord_addr_validation.blank):
            result.append("Failure")
            result.append("Invalid Order")
            result.append("Invalid delivery address")

        return result



