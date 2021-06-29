from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    SEX_CHOICES = ( ('F', 'Female'),
                    ('M', 'Male'), 
                    )
        
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    # photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, Null=True)
    

    def __str__(self):
        return f'Profile for user {self.user.username}'
        