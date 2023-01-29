from django.db import models

# Create your models here.
NUM_SETS = 1
SETS = range(1, NUM_SETS + 1)

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    set = models.IntegerField(
        choices=zip(SETS, SETS),
        default=SETS[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question

    def move(self, solved):
        switch={
            1: self.option1 == self.answer,
            2: self.option2 == self.answer,
            3: self.option3 == self.answer,
            4: self.option4 == self.answer
        }
        return switch.get(solved)
        


