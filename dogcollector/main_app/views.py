#from xml.dom import domreg
from django.shortcuts import render, redirect
# import the Class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog  # importing my model
from .forms import ExerciseForm  # importing my exercise  to instantiate it
# Create your views here.
from django.http import HttpResponse


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'


class DogUpdate(UpdateView):
    model = Dog
    # disallow the renaming of a dog by excluding the name field
    fields = ['breed', 'description', 'age']


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

# Define the home view


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()  # using our model to get all the rows in our dog table in psql
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):  # path('dogs/<int:dog_id>/') - this is where dog_id comes from
    dog = Dog.objects.get(id=dog_id)
     # instantiate ExerciseForm to be rendered in the template
    exercise_form = ExerciseForm()
    # include the dog and exercise_form in the context
    return render(request, 'dogs/detail.html', {'dog': dog, 'exercise_form': exercise_form})



def add_exercise(request, dog_id):
    # create a ModelForm instance using the data in request.POST
    form = ExerciseForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_exercise = form.save(commit=False)
        new_exercise.dog_id = dog_id
        new_exercise.save()
    return redirect('detail', dog_id=dog_id)

   