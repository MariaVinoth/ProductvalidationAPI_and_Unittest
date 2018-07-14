import unittest
from dlr_auth import dealer_auth

class Testdlr_auth(unittest.TestCase):

    def setUp(self):
        self.dlr_auth1 = dealer_auth("","")
        self.dlr_auth2 = dealer_auth("FAKEID", "FAKEKEY")
        self.dlr_auth3 = dealer_auth("XXX-1234-ABCD-1234","kkklas8882kk23nllfjj88290")


    def test_dlr_validate(self):
        self.assertEqual(self.dlr_auth1.dlr_validate(),["Failure","Not authorized"])
        self.assertEqual(self.dlr_auth2.dlr_validate(), ["Failure", "Not authorized"])
        self.assertEqual(self.dlr_auth3.dlr_validate(),[])


if __name__ == '__main__':
    unittest.main()



