from django.shortcuts import render, HttpResponse

from django.contrib.staticfiles.storage import staticfiles_storage
import csv
# pip install reportlab
from reportlab.pdfgen import canvas


# Create your views here.
def index(request):
    return render(request, "app20/index.html")


def createImage(request):
    file_path = staticfiles_storage.path('app20/images/image1.jpg')
    image_data = open(file_path, "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def createCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['Row1', 'Raj', 'Thapa', '9851145433'])
    writer.writerow(['Row2', 'Rajan', 'Rai', '9843232321', 'rajan@gmail.com'])
    return response


def createPDF(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document1.pdf"'
    p = canvas.Canvas(response)
    p.drawString(10, 10, "Hello world of python")
    p.showPage()
    p.save()
    return response


