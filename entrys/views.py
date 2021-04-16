from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Entry, Comment


def index(request):
    entrys = Entry.objects.all()
    return render(request, "entrys/index.html", {'entrys':entrys})

def singleEntry(request, entryId):
    entry = get_object_or_404(Entry, pk=entryId)
    try: 
        comments = Comment.objects.filter(entryId = entry)
    except:
        comments = [] 
    return render(request, "entrys/entry.html", {'entry':entry, 'comments':comments})

def commentEntry(request, entryId):
        entry = get_object_or_404(Entry, pk=entryId)
        comments = Comment.objects.filter(entryId = entry)
        if(request.POST['username'] and request.POST['content']):
            username, content = request.POST['username'], request.POST['content']
            comment = Comment(username = username, content = content, entryId = entry)
            comment.save()
            return HttpResponseRedirect(reverse('entrys:singleEntry', args=(entryId,)))
        else: 
            return render(request, "entrys/entry.html", {
                'entry': entry, 
                'error': 'Falta usuario o el contenido',
                'comments': comments
            })
            
 




    

