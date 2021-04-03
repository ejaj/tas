from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.urls import reverse
from .validators import agent_logo, validate_max_image_size, customer_image, upload_visa, upload_passport
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Agent(models.Model):
    """
    Stores a single agent entry, related to :model:`auth.User`.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(help_text="A short label, generally used in URLs.")
    email = models.EmailField(max_length=50, unique=True)
    mobile = models.CharField(max_length=50, db_index=True)
    address = models.TextField()
    country = CountryField(blank_label='Please select a country')
    logo = models.ImageField(
        upload_to=agent_logo, editable=True, help_text="logo size must be 100 x 100 px",
        verbose_name="Agent Logo", validators=[validate_max_image_size], null=True, blank=True
    )
    status = models.BooleanField(default=True)
    created = models.ForeignKey(User, null=True, blank=True, related_name='agent_created',
                                on_delete=models.CASCADE)
    updated = models.ForeignKey(User, null=True, blank=True, related_name='agent_updated',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "1. Agent"
        db_table = 'agents'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agent:edit', kwargs={'pk': self.pk})


class Customer(models.Model):
    """
    Stores a single customer entry, related to :model:agents and :model:`auth.User`.
    """
    STATUS = (
        ('posted', 'posted'),
        ('approved', 'approved'),
        ('delivered', 'delivered')
    )

    difficulty_level = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )

    agent = models.ForeignKey(Agent, verbose_name='Agent Name', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200, db_index=True)
    address = models.TextField(null=True, blank=True)
    dob = models.DateField(max_length=10, verbose_name="Date of Birth")
    passport_number = models.CharField(max_length=50)
    passport_expire_date = models.DateField(max_length=10, null=True, blank=True)
    visa_number = models.CharField(max_length=50, null=True, blank=True)
    visa_expire_date = models.DateField(max_length=10, null=True, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0, null=True, blank=True)
    upload_passport = models.ImageField(
        upload_to=upload_passport, editable=True, help_text="upload your passport here",
        validators=[validate_max_image_size], null=True, blank=True
    )
    upload_visa = models.ImageField(
        upload_to=upload_visa, editable=True, help_text="upload your visa here",
        validators=[validate_max_image_size], null=True, blank=True
    )
    picture = models.ImageField(
        upload_to=customer_image, editable=True, help_text="logo size must be 100 x 100 px",
        verbose_name="Profile Picture", validators=[validate_max_image_size], null=True, blank=True
    )
    status = models.CharField(max_length=200, choices=STATUS, default="posted")
    created = models.ForeignKey(User, null=True, blank=True, related_name='customer_created',
                                on_delete=models.CASCADE)
    updated = models.ForeignKey(User, null=True, blank=True, related_name='customer_updated',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "2. Customer"
        db_table = 'customers'

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('customer:edit', kwargs={'pk': self.pk})


class AgentUser(models.Model):
    '''
    Store agent as login user related to :model:agents and :model:`auth.User`.
    '''
    user = models.ForeignKey(User, null=True, blank=True, related_name='agent_user',
                             on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.CASCADE)
    plain_password = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "9. Agent User"
        db_table = 'agent_users'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('agentuser:edit', kwargs={'pk': self.pk})

