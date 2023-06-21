from django.shortcuts import render
from django.views import View
from courses.models import Course

# Create your views here.
def home(request):
    cr = Course.objects.all()
    return render(request,'HOME/index.html', {'cr':cr})

class ProductDetailsView(View):
    def get(self,request,pk):
        course = Course.objects.get(pk=pk)
        return render (request,'ITEMS/item_detail.html',{"course":course})

def about_us(request):
    return render(request,'HOME/about_us.html')


