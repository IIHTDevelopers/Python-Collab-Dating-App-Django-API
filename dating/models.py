from django.db import models

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    gender=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    is_deleted=models.BooleanField(default=False)


class InterestsModel(models.Model):
    id = models.AutoField(primary_key=True) 
    interested_in=models.CharField(max_length=100)  
    not_interested_in=models.CharField(max_length=100)
    hobbies=models.CharField(max_length=200)    
    profile_url=models.CharField(max_length=200)
    about=models.CharField(max_length=200)
    user_id = models.IntegerField()
    is_deleted=models.BooleanField(default=False)


class MatchModel(models.Model):
    id = models.AutoField(primary_key=True)
    match_id=models.IntegerField()
    user_id = models.IntegerField()
    is_deleted=models.BooleanField(default=False)


class LikesModel(models.Model):
    id = models.AutoField(primary_key=True)
    like_id=models.IntegerField()
    user_id=models.IntegerField()
    is_deleted=models.BooleanField(default=False)

class DisLikesModel(models.Model):
    id = models.AutoField(primary_key=True)
    dislike_id=models.IntegerField()
    user_id=models.IntegerField()
    is_deleted=models.BooleanField(default=False)
