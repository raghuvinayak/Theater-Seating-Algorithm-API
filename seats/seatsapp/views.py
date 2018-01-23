from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from seatsapp.models import Layout, Flag, Seating
from django.core import serializers
import json

def layout(request):
    obj = Layout.objects.all()
    model = serializers.serialize("json", obj)
    return HttpResponse(model, content_type='application/json')

def flag(request):
    obj = Flag.objects.all()
    model = serializers.serialize("json", obj)
    return HttpResponse(model, content_type='application/json')

def seating(request):
    obj = Seating.objects.all()
    model = serializers.serialize("json", obj)
    return HttpResponse(data, content_type='application/json')

def seating_view(request):
    obj = Layout.objects.all().order_by('row', 'seat')
    
    string = ""

    for layout in obj:
        string += "Row: " + str(layout.row) + ", column: " + str(layout.seat) + "<br/>"
        string += "Rank: " + str(layout.rank) + ", section: " + str(layout.section) + "<br/>"
        string += "Name: " + str(layout.name) + "<br/>"
        string += "<br/><br/>"
        

    return HttpResponse(string)
 
# Create your views here.
