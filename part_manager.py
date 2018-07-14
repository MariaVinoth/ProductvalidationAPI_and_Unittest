class part_manager():

     #hardcoded parts 
    in_stock = {1234:5, 2212:1, 3123:5,5578:3,1212:2}
    out_stock = [1542,2311,9834,4312,1213,1334]
    no_more_manuf = [1555,2333,4122,3122]

    def __init__(self,part_no,qty):
        self.part_no = part_no
        self.qty = qty


    def ord_valid(self):
        result = []
        if(self.part_no == 0 or self.part_no <= 0 or self.qty <= 0):
            result.append("Failure")
            result.append("Invalid Order")
            result.append("Invalid order item entry")
        return result

    def order_process(self):
        result = []
        result.append(self.part_no)
        result.append(self.qty)
        if(self.part_no in part_manager.in_stock):
            if(part_manager.in_stock[self.part_no] >= self.qty):
                result.append("Success")
                result.append("")
            else:
                result.append("Failure")
                result.append("Out of stock")

        elif(self.part_no in part_manager.out_stock):
            result.append("Failure")
            result.append("Out of stock")

        elif(self.part_no in part_manager.no_more_manuf):
            result.append("Failure")
            result.append("no longer manufactured")

        else:
            result.append("Failure")
            result.append("Invalid part")

        return result
