from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', help_text='Enter your name')
    email = models.EmailField(max_length=100, verbose_name='Email', help_text='Enter your email')
    phone = models.CharField(max_length=12, verbose_name='Phone', help_text='Enter your phone number')
    description = models.TextField(verbose_name='Description', help_text='Information about contact')

    def __str__(self):
        return self.name