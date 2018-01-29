from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Trip(models.Model):
    destination = models.CharField(max_length=50)
    transport = models.CharField(max_length=9)
    trip_logo = models.CharField(max_length=1000,blank=True )
    is_available = models.BooleanField(default=True)
    trip_id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=6)
    no_of_days = models.CharField(max_length=2)

    def __str__(self):
        return str(self.destination) +' - ' + str(self.price) +'$ - no of days : '+ str(self.no_of_days)

class Question(models.Model):
    ques_id = models.ForeignKey(Trip,related_name='questions')
    statement = models.TextField(null=True,max_length=6000)
    user_id = models.ForeignKey(User,related_name='questions')
    answer = models.TextField(default=' ')


    def __str__(self):
        return 'Question on trip no. : '+self.ques_id +'-' + self.statement +' ? - ' +self.answer

class book(models.Model):
    book_ques_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    book_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_trip_id = models.ForeignKey(Trip,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_user_id + '-' + self.book_trip_id


