from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import Entry, Comment


class index(generic.ListView):
    template_name = "entrys/index.html"
    model = Entry
    context_object_name = "entrys"
    paginate_by = 4

class singleEntry(generic.DetailView):
    template_name = "entrys/entry.html"
    model = Entry
    context_object_name = "entry"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(id=self.kwargs['pk'])
        return context
    
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
            
 




    

