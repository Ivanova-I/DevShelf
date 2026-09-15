from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from resources.models import Resource
class LearningPath(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')],
        default='easy')
    estimated_hours = models.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(0.1), MaxValueValidator(24.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    resources = models.ManyToManyField(Resource, related_name='learning_paths')

    def __str__(self):
        return self.title


