from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.CharField(max_length= 250)

    def __str__(self):
        return self.name
    
