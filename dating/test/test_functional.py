from rest_framework.test import APITestCase
from dating.models import *
from dating.test.TestUtils import TestUtils
class DatingAppAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(user_id=101,name="user1",age=25,email="user1@gmail.com",
        phone= 9841849651,gender= "Male",city="Vikarabad",country= "India")
        InterestsModel.objects.create(id=1,interested_in="Walking",not_interested_in="Running",
        hobbies="GYM",profile_url="myprofile2.com",about= "I am married",user_id= 102)
        MatchModel.objects.create(id=2,match_id=112,user_id= 102)
        LikesModel.objects.create(id=1,like_id=1112,user_id= 101)
        DisLikesModel.objects.create(id=1,dislike_id=2222,user_id= 101)
 
    def test_get_the_user_by_id(self):
        url='http://127.0.0.1:8000/user_crud_pk/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("User_TestGetTheUserById", True, "functional")
            print("User_TestGetTheUserById = Passed")
        else:
            test_obj.yakshaAssert("User_TestGetTheUserById", False, "functional")
            print("User_TestGetTheUserById = Failed")

    def test_get_all_users(self):
        url='http://127.0.0.1:8000/user_crud/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("User_TestGetAllUsers", True, "functional")
            print("User_TestGetAllUsers = Passed")
        else:
            test_obj.yakshaAssert("User_TestGetAllUsers", False, "functional")
            print("User_TestGetAllUsers = Failed")

    def test_register_user(self):
        url='http://127.0.0.1:8000/user_crud/'
        data= {
        "user_id": 102,
        "name": "User2",
        "age": 31,
        "email": "user2@gmail.com",
        "phone": 9841849651,
        "gender": "Male",
        "city": "Vikarabad,",
        "country": "India"
    }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("User_TestRegisterUser", True, "functional")
            print("User_TestRegisterUser = Passed")
        else:
            test_obj.yakshaAssert("User_TestRegisterUser", False, "functional")
            print("User_TestRegisterUser = Failed")

    def test_update_user(self):
        url='http://127.0.0.1:8000/user_crud_pk/101/'
        data={
                'gender':'Female'
            }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("User_TestUpdateUser", True, "functional")
            print("User_TestUpdateUser = Passed")
        else:
            test_obj.yakshaAssert("User_TestUpdateUser", False, "functional")
            print("User_TestUpdateUser = Failed")

    def test_delete_user(self):
        url='http://127.0.0.1:8000/user_crud_pk/101/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("User_TestDeleteUser", True, "functional")
            print("User_TestDeleteUser = Passed")
        else:
            test_obj.yakshaAssert("User_TestDeleteUser", False, "functional")
            print("User_TestDeleteUser = Failed")


#Interests Module 
    def test_create_interests(self):
        url='http://127.0.0.1:8000/interests_crud/'
        data=  {
        "id":3,    
        "interested_in": "Walking",
        "not_interested_in": "Running",
        "hobbies": "GYM",
        "profile_url": "myprofile2.com",
        "about": "I am married",
        "user_id": 102  
    }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Interests_TestCreateInterests", True, "functional")
            print("Interests_TestCreateInterests = Passed")
        else:
            test_obj.yakshaAssert("Interests_TestCreateInterests", False, "functional")
            print("Interests_TestCreateInterests = Failed")

    def test_get_the_interests_by_id(self):
        url='http://127.0.0.1:8000/interests_crud_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Interests_TestGetTheInterestsById", True, "functional")
            print("Interests_TestGetTheInterestsById = Passed")
        else:
            test_obj.yakshaAssert("Interests_TestGetTheInterestsById", False, "functional")
            print("Interests_TestGetTheInterestsById = Failed")

    def test_get_the_interests_by_user_id(self):
        url='http://127.0.0.1:8000/get_interests_by_user_id/102/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Interests_TestGetTheInterestsByUserId", True, "functional")
            print("Interests_TestGetTheInterestsByUserId = Passed")
        else:
            test_obj.yakshaAssert("Interests_TestGetTheInterestsByUserId", False, "functional")
            print("Interests_TestGetTheInterestsByUserId = Failed")

    def test_update_interests(self):
        url='http://127.0.0.1:8000/interests_crud_pk/1/'
        data= {
        "id":1,
        "interested_in": "Walking",
        "not_interested_in": "Running",
        "hobbies": "GYM",
        "profile_url": "myprofile2.com",
        "about": "I am un married",
        "user_id": 102  
         }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Interests_TestUpdateInterests", True, "functional")
            print("Interests_TestUpdateInterests = Passed")
        else:
            test_obj.yakshaAssert("Interests_TestUpdateInterests", False, "functional")
            print("Interests_TestUpdateInterests = Failed")

    def test_delete_interests(self):
        url='http://127.0.0.1:8000/interests_crud_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Interests_TestDeleteInterests", True, "functional")
            print("Interests_TestDeleteInterests= Passed")
        else:
            test_obj.yakshaAssert("Interests_TestDeleteInterests", False, "functional")
            print("Interests_TestDeleteInterests = Failed")


#Match Module 
    def test_create_match(self):
        url='http://127.0.0.1:8000/match_view/'
        data=  {
        "match_id": 112,
        "user_id": 102
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Match_TestCreateMatch", True, "functional")
            print("Match_TestCreateMatch = Passed")
        else:
            test_obj.yakshaAssert("Match_TestCreateMatch", False, "functional")
            print("Match_TestCreateMatch = Failed")


    def test_get_all_matches(self):
        url='http://127.0.0.1:8000/match_view/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Match_TestGetAllMatches", True, "functional")
            print("Match_TestGetAllMatches = Passed")
        else:
            test_obj.yakshaAssert("Match_TestGetAllMatches", False, "functional")
            print("Match_TestGetAllMatches = Failed")


#Likes Module

    def test_add_like(self):
        url='http://127.0.0.1:8000/add_like/'
        data=  {
        "like_id": 1112,
        "user_id": 101
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Like_TestAddLike", True, "functional")
            print("Like_TestAddLike = Passed")
        else:
            test_obj.yakshaAssert("Like_TestAddLike", False, "functional")
            print("Like_TestAddLike = Failed")

    def test_get_all_likes_by_user_id(self):
        url='http://127.0.0.1:8000/get_likes_by_user_id/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Like_TestGetAllLikesByUserId", True, "functional")
            print("Like_TestGetAllLikesByUserId = Passed")
        else:
            test_obj.yakshaAssert("Like_TestGetAllLikesByUserId", False, "functional")
            print("Like_TestGetAllLikesByUserId = Failed")

#DisLikes Module

    def test_add_dislike(self):
        url='http://127.0.0.1:8000/add_dislike/'
        data=  {
        "dislike_id": 2223,
        "user_id": 101
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Dislike_TestAddDislike", True, "functional")
            print("Dislike_TestAddDislike = Passed")
        else:
            test_obj.yakshaAssert("Dislike_TestAddLike", False, "functional")
            print("Dislike_TestAddDislike = Failed")

    def test_get_all_dislikes_by_user_id(self):
        url='http://127.0.0.1:8000/get_dislikes_by_user_id/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Dislike_TestGetAllDislikeByUserId", True, "functional")
            print("Dislike_TestGetAllDislikeByUserId = Passed")
        else:
            test_obj.yakshaAssert("Dislike_TestGetAllDislikeByUserId", False, "functional")
            print("Dislike_TestGetAllDislikeByUserId = Failed")