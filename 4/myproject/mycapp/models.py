from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    hobby = models.CharField(max_length=100, blank=True, null=True)
    previous_workplace = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Preferences(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    favorite_categories = models.TextField(blank=True, null=True)
    preferred_brands = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.profile}"
