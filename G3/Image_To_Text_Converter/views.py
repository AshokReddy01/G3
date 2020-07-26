from django.shortcuts import render
import cv2
from  PIL import Image
import pytesseract
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html',{'name':'Ashok'})

def about(request):
    return render(request,"components.html")




def convert(request):
    try:
        
        img = request.FILES['file']
        img = Image.open(img)
        
        text = pytesseract.image_to_string(img)

        
    except Exception:
        text = "Error in converting"
    
    finally:
        return render(request, 'convert.html',{'name':text})