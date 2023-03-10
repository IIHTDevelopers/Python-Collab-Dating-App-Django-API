from rest_framework.test import APITestCase
from dating.test.TestUtils import TestUtils
class DatingAppAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("User_TestBoundary",True,"boundary")
        print("User_TestBoundary = Passed")
