from django.db import models

class Survey(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    
    ECOMMERCE_CHOICES = [
        ('a', 'Telegram'),
        ('b', 'Instagram'),
        ('c', 'Facebook'),
        ('d', 'E-commerce'),
        ('e', 'Yoq'),
    ]
    ecommerce_usage = models.CharField(max_length=1, choices=ECOMMERCE_CHOICES)
    
    TURNOVER_CHOICES = [
        ('a', '+10 mln'),
        ('b', '+30 mln'),
        ('c', '+50 mln'),
        ('d', '+100 mln'),
        ('e', 'Yoq'),
    ]
    monthly_turnover = models.CharField(max_length=1, choices=TURNOVER_CHOICES)
    
    COMMISSION_CHOICES = [
        ('a', '3 foiz'),
        ('b', '5 foiz'),
        ('c', '10 foiz'),
        ('d', 'Bilmayman'),
    ]
    commission_requirement = models.CharField(max_length=1, choices=COMMISSION_CHOICES)

    def __str__(self):
        return self.full_name