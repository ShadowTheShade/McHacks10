from django.db import models

# Create your models here.
NUM_SETS = 5
SETS = range(1, NUM_SETS + 1)

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    set = models.IntegerField(
        choices=zip(SETS, SETS),
        default=SETS[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def move(self, solved):
        new_set = self.set + 1 if solved else SETS[0]

        if new_set in SETS:
            self.set = new_set
            self.save()

        return self


