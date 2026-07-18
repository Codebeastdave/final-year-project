from django.db import models

class Post(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    Subjects_of_interest = [
            (PHYSICS, 'Physics'),
            (MATHEMATICS, 'Mathematics'),
            (CHEMISTRY, 'Chemistry'),
            ]
    Lastname = models.CharField(max_length=30, blank=False, null=False)

    Firstname= models.CharField(max_length=20, blank=False, null=False)

    Phone_number=models.CharField(max_length=20, blank=False, null=False)

    username = models.CharField(max_length=20, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=MALE)
    subject_of_interest = models.CharField(max_length=12, choices=Subjects_of_interest, default=MALE)
time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
