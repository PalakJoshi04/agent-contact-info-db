from django.db import models
from .validators import *


class ContactInfo(models.Model):
    mobileNumber = models.PositiveIntegerField()
    phoneNumber = models.PositiveIntegerField()
    emailID = models.EmailField(max_length=50)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True, validators=[validate_city])
    state = models.CharField(max_length=20, blank=True, null=True, validators=[validate_state])
    landmark = models.CharField(max_length=20, blank=True, null=True, validators=[validate_landmark])
    pincode = models.IntegerField(blank=True, null=True)


class Agent(ContactInfo):
    first_name = models.CharField(max_length=20, validators=[validate_first_name])
    last_name = models.CharField(max_length=20, validators=[validate_last_name])
    education = models.TextField(max_length=1000)
    company_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=20)
    agent_notes = models.TextField(max_length=1000)
    addresses = models.ManyToManyField(Address)

    @property
    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('first_name',)
