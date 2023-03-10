from rest_framework.exceptions import APIException

class UserIdNotAvailable(APIException):
    default_detail = 'Specified user id is not available'

class InterestsIdNotAvailable(APIException):
    default_detail = 'Specified interest id is not available'

