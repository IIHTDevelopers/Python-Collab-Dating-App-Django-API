
from django.contrib import admin
from .models import UserModel,InterestsModel,LikesModel,DisLikesModel,MatchModel
admin.site.register(UserModel)
admin.site.register(InterestsModel)
admin.site.register(MatchModel)
admin.site.register(LikesModel)
admin.site.register(DisLikesModel)




