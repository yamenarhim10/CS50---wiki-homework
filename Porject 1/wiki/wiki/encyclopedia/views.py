from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def renderEntry(request, entry):
    entries = util.list_entries()
    if entry in entries:
        return render(request, "encyclopedia/testentry.html", {"entry": f"Your entry {entry}, Found  "})
    else:
        return render(request, "encyclopedia/testentry.html", {"entry": f"Your entry {entry}, wasn't Found  "})
    

