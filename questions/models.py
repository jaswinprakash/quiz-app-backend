from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Question(models.Model):
    question = models.TextField()
    choice_1 = models.CharField(max_length=200)
    choice_2 = models.CharField(max_length=200)
    choice_3 = models.CharField(max_length=200)
    choice_4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hint = models.TextField()

    def __str__(self):
        return self.question

    def clean(self):
        if self.correct_answer not in [self.choice_1, self.choice_2, self.choice_3, self.choice_4]:
            raise ValidationError("The correct answer must be one of the available choices.")
