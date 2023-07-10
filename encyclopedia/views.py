from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if entry := util.get_entry(title):
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": f"Page for {title} doesn't exist yet"
        })
    
def search(request):
    if request.method == "POST":
        data = request.POST
        title = data["title"]

        if util.get_entry(title):
            return redirect("wiki:wiki", title=title)
        else:
            entries = util.list_entries()
            valid = list()

            for entry in entries:
                if title.lower() in entry.lower():
                    valid.append(entry)

            return render(request, "encyclopedia/index.html", {
                "entries": valid
            })