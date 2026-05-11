from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Item
from .forms import ItemForm

# Create your views here.


def index(request):
    #Getting items from the database
    item_list = Item.objects.all()
    
    #Creating context
    context = {
        'item_list': item_list
    }

    #Passing the context object to the render method along with the templates
    return render(request,"myapp/index.html",context) #Rendering the html template

def detail(request,id):
    item = Item.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request,'myapp/detail.html',context)
    # return HttpResponse(f'This is the detail view for item {item}')

def create_item(request):
    form = ItemForm()
    return render(request,'myapp/item-form.html')