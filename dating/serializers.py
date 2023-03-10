
from rest_framework.serializers import ModelSerializer
from dating.models import UserModel,InterestsModel,LikesModel,DisLikesModel,MatchModel

class UserSerializer(ModelSerializer):
    class Meta:
        model=UserModel
        fields='__all__'

class InterestsSerializer(ModelSerializer):
    class Meta:
        model=InterestsModel
        fields='__all__'

class MatchSerializer(ModelSerializer):
    class Meta:
        model=MatchModel
        fields='__all__'

class LikesSerializer(ModelSerializer):
    class Meta:
        model=LikesModel
        fields='__all__'

class DisLikesSerializer(ModelSerializer):
    class Meta:
        model=DisLikesModel
        fields='__all__'

