from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, )
    food = models.CharField(max_length=200)
    game = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.food

    def __abs__(self):
        return self.game


class Person(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    role = models.CharField(max_length=50)

    def as_json(self):
        return dict(
            id=self.id, input_user=self.user_name,
            email=self.email, age=self.age,
            role=self.role)
