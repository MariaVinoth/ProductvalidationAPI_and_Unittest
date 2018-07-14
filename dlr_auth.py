class dealer_auth:

    blank = '';
    def __init__(self,dlr_id,dlr_key):
        self.dlr_id = dlr_id
        self.dlr_key = dlr_key

    def dlr_validate(self):
        result = []
        reject_id = "FAKEID"
        reject_key = "FAKEKEY"

        if(self.dlr_id == dealer_auth.blank and self.dlr_key == dealer_auth.blank) or (self.dlr_id == reject_id or  self.dlr_key == reject_key ):
            result.append("Failure")
            result.append("Not authorized")

        return result




