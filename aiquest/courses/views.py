from django.shortcuts import render

# Create your views here.

def course_details(request):
    return render(request,'ITEMS/item_details.html')

def dj_course_details(request):
    return render(request,'ITEMS/dj_item_details.html')

def ml_course_details(request):
    return render(request,'ITEMS/ml_item_details.html')

def dl_course_details(request):
    return render(request,'ITEMS/dl_item_details.html')

def stat_course_details(request):
    return render(request,'ITEMS/stat_item_details.html')

def data_analysis_course_details(request):
    return render(request,'ITEMS/danalysis_item_details.html')

def big_data_course_details(request):
    return render(request,'ITEMS/big_data_item_details.html')