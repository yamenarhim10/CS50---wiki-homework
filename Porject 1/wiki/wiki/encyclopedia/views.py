from django import forms
from django.shortcuts import render
from django.urls import reverse
from . import util

import markdown2
from pathlib import Path
import os
from django.http import HttpResponseRedirect,HttpResponse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def renderEntry(request, entry):
    entries = util.list_entries()
    if entry in entries:
        html = markdown2.markdown(util.get_entry(entry))
        return render(request, "encyclopedia/Entry.html", {"entry":html})
    else:
        return render(request, "encyclopedia/404 error.html", {"entry": f"Your entry {entry}, wasn't Found  "})
    
def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        # Process the search query, e.g., search in the database
        # For demonstration, let's just return the search query
        entries = util.list_entries()
        partial_match = []
        for entry in entries:
            if search_query == entry:
                return HttpResponseRedirect(reverse("encyclopedia:entry",args=[entry]))
            elif search_query in entry:
                partial_match.append(entry)
        if partial_match:
            return HttpResponseRedirect(reverse("encyclopedia:partial_matches") + f"?matches={','.join(partial_match)}")
        else:
            return HttpResponse("No matches found.")
    else:
        return HttpResponse('This view only handles POST requests.')


def partial_matches(request):
    matches = request.GET.get('matches', '').split(',')
    print(matches)
    return render(request, "encyclopedia/partial_matches.html", {
        "matches": matches
    })