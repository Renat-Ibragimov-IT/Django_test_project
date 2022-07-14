from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="profile")
    dob = models.DateField(verbose_name="Date of Birth", null=True,
                           help_text="We need it to show you relevant content")

