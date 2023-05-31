from django.db import models


from django.core.exceptions import ValidationError
from django.db import models

class Question(models.Model):
    statement = models.TextField()
    choice_1 = models.CharField(max_length=200)
    choice_2 = models.CharField(max_length=200)
    choice_3 = models.CharField(max_length=200)
    choice_4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.statement

    def clean(self):
        if self.correct_answer not in [self.choice_1, self.choice_2, self.choice_3, self.choice_4]:
            raise ValidationError("The correct answer must be one of the available choices.")
