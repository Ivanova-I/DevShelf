from django.contrib.auth.models import User
from django.db import models

from catalog.models import Technology, Tag
from decimal import Decimal
from django.core.validators import  MinValueValidator , MaxValueValidator

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField()
    resource_type = models.CharField(choices=[('article', 'Article'),
                                               ('video', 'Video'),
                                               ('documentation','Documentation'),
                                               ('course','Course'),
                                               ('book','Book')
                                            ], max_length=100)
    difficulty = models.CharField(choices=[
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard')],
        default='easy')
    estimated_minutes = models.IntegerField(default=1,validators=[MinValueValidator(1),],)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[
        MinValueValidator(Decimal("0.00")),
        MaxValueValidator(Decimal("5.00")),
    ],)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    technology = models.ForeignKey(Technology, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name='resources')

    def __str__(self):
        return self.title

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    status = models.CharField(choices=[('not started', 'Not Started'),('in progress', 'In Progress'),('completed', 'Completed')], default='not started', max_length=100)
    last_position_sec = models.IntegerField(default=0)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'resource'], name='unique_user_resource_progress')
        ]

    def __str__(self):
        return f'{self.user.username}- {self.resource.title} -({self.status})'
