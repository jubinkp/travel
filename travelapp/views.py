
from django.shortcuts import render

from . models import Place


def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})


