from django.db import models
from django.contrib.auth.models import AbstractUser

DEPT_CHOICES = [
    ('computer', 'Computer'),
    ('biology', 'Biology'),
]

TYPE_CHOICES = [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
]

class stu_register(AbstractUser):
    mobile = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    department = models.CharField(choices=DEPT_CHOICES, null=True, max_length=15)
    reg_type = models.CharField(choices=TYPE_CHOICES, null=True, max_length=15)

    def __str__(self):
        return self.username

class exam_code(models.Model):
    exam_number = models.IntegerField()

    def __str__(self):
        return str(self.exam_number)

class exam_result(models.Model):
    stu_id = models.ForeignKey(stu_register, on_delete=models.CASCADE)
    result = models.CharField(max_length=5, default='Pass')
    strike = models.IntegerField(default=0)
    Tab_strike = models.IntegerField(default=0)

    def __str__(self):
        return self.stu_id.username

class questions(models.Model):
    depart = models.CharField(max_length=15)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    quest1_option1 = models.TextField()
    quest1_option2 = models.TextField()
    quest1_option3 = models.TextField()
    quest1_option4 = models.TextField()
    quest2_option1 = models.TextField()
    quest2_option2 = models.TextField()
    quest2_option3 = models.TextField()
    quest2_option4 = models.TextField()
    quest3_option1 = models.TextField()
    quest3_option2 = models.TextField()
    quest3_option3 = models.TextField()
    quest3_option4 = models.TextField()

    def __str__(self):
        return self.depart
