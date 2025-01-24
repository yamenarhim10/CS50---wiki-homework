from django.shortcuts import render

from . import util

import markdown2
from pathlib import Path
import os

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def renderEntry(request, entry):
    entries = util.list_entries()
    if entry in entries:
        with open('entries/'+str(entry)+'.md', 'r', encoding='utf-8') as file:
            markdown_text = file.read()
        html = markdown2.markdown(markdown_text)
        print(html)
        return render(request, "encyclopedia/Entry.html", {"entry":html})
    else:
        return render(request, "encyclopedia/404 error.html", {"entry": f"Your entry {entry}, wasn't Found  "})
    

