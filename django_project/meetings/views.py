from django.shortcuts import render, get_object_or_404
from django.forms import modelfor_factory

from .models import Meeting


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

MeetingForm = modelform_factory(meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, 'meetings/new.html', {"form": })
