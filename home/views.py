from django.shortcuts import render
from django.views.generic.list import ListView
from .admin import *
# Create your views here.
def home(request):
    
    return render(request, 'index.html')


 
class MainList(ListView):
 
    # specify the model for list view
    model = Menu
    context_object_name = 'menu'
    queryset = Menu.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(MainList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['special'] = Special.objects.all()
        context['chefs'] = Chefs.objects.all()
        context['events'] = Events.objects.all()
        context['saying'] = SayingAbout.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['category'] = Category.objects.all()
        return context