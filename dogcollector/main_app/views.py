#from xml.dom import domreg
from django.shortcuts import render, redirect
# import the Class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Toy # importing my model
from .forms import ExerciseForm  # importing my exercise  to instantiate it
# Create your views here.
from django.http import HttpResponse


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'


class DogUpdate(UpdateView):
    model = Dog
    # disallow the renaming of a dog by excluding the name field
    fields = ['breed', 'description', 'age', 'toy']


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
    #Get the Toys the dog doesn't have
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
     # instantiate ExerciseForm to be rendered in the template
    exercise_form = ExerciseForm()
    # include the dog and exercise_form in the context
    return render(request, 'dogs/detail.html', {'dog': dog, 'exercise_form': exercise_form,
    #Add the toys to be displayed
    'toys': toys_dog_doesnt_have
    })
    



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

def assoc_toy(request, dog_id, toy_id):
  # Note: you can pass a toy's id instead of the whole object
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id=dog_id)
    
class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
   