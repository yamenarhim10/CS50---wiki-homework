from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def renderEntry(request, entry):
    return render(request, "encyclopedia/testentry.html", {"entry": entry})

