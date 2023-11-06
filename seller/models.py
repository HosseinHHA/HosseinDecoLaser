from django.db import models


class Seller(models.Model):
    gender_choices = (
        ('male', 'MALE'),
        ('female', 'FEMALE')
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=6, choices=gender_choices)
    birth_date = models.DateField()
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profiles_seller/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
