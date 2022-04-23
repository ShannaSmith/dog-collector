#from xml.dom import domreg
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#Add the dog class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Twilight', 'Havapoo', 'evil', 8),
  Dog('Sage', 'Giant Schnauzer', 'black and playful', 2),
  Dog('Nyla', 'Pomeranian', 'neurotic', 4)
]
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
    return  render(request, 'about.html')
def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})