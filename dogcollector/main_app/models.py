from django.db import models
from django.urls import reverse
# A tuple of 2-tuples
Outtings =(
    ('W', 'Walk'),
    ('H', 'Hike'),
    ('P', 'Dog Park')
)
# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    def __str__(self):
        return f"The dog named {self.name} has id of {self.id}"
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
class Exercise(models.Model):
    date = models.DateField('exercise date')
    outting = models.CharField(
        max_length=1,
        #add the 'choices' field option
        choices=Outtings,
       # set the default value for outting to be 'W'
       default=Outtings[0][0]
        )
        #Create a dog_id FK
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    def __str__(self):
        # method for obtaining the friendly value of a Field.choice
        return f"{self.get_outting_display()} on {self.date}"
    