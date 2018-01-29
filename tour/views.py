from django.shortcuts import render,HttpResponse,Http404,get_object_or_404
from .models import Trip
def home(request):
    return HttpResponse('<h3> Hello world </h3>')

def index(request):
    trips = Trip.objects.all()
    return render(request,'tour/index.html',{'trips':trips})

def detail(request,trip_id):
    try:
        trip = Trip.objects.get(pk = trip_id)
    except Trip.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request,'tour/detail.html', {'trip' : trip})



