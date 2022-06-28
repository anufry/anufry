from django.shortcuts import render, get_object_or_404
from django.http import Http404 

from .models import Sheet

def sheet_detail(request, slug):
    if slug in ('',):
        raise Http404  

    post = get_object_or_404(Sheet, slug=slug,)
    return render(request, 'sheets/sheet_detail.html', {'post': post})
