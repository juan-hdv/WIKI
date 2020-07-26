from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render
from urllib.error import HTTPError
from random import randint
from markdown2 import Markdown

from . import util

def handler404 (request, exception):
	pagename = request.get_full_path().split("/").pop()
	response = render(request, '404.html', {
		"message":f"The resource you are looking for does not exist.",
		"pagename": pagename
	})
	response.status_code = 404
	return response

def index(request):
    return render(request, "encyclopedia/index.html", {
        "pageTitle": "All Pages",
        "entries": util.list_entries()
    })

def pageShow(request, entry):
	content = util.get_entry(entry)
	if content is None:
		raise Http404 (f'<h2>Page not found: "wiki/{entry}"</h2>') # The message is useful only for debug

	mk = Markdown()
	return render(request, "encyclopedia/pageshow.html", {
		"entry": entry,
		"content": mk.convert(content)
	})

def pageSearch (request):
	result = None
	entry = request.POST["q"]
	if entry is None or entry == "":
		return HttpResponseRedirect(reverse('index'))

	content = util.get_entry(entry)
	if content is not None:
		return HttpResponseRedirect(f"/wiki/{entry}")

	# Get a list of entries which contains <entry>
	result = list(filter (lambda x:  entry.upper() in x.upper(), util.list_entries()))
	return render(request, "encyclopedia/index.html", {
        "pageTitle": "Search results",
	    "entries": result
	})

def pageNew (request):
	if request.method != "POST":
		return render(request, "encyclopedia/pagenew.html", {})

	# POST Requets
	if request.POST.get('cancel'):
		return HttpResponseRedirect(reverse('index'))

	entry = request.POST["entry"]
	# Check if entry already exists
	content = util.get_entry(entry)
	if content is not None:
		return render(request, "encyclopedia/error.html",{
			"message": f'The entry name "{entry}" already exists. Please try another entry name.'
		})

	# Save new entry
	content = request.POST["content"]
	util.save_entry(entry, content)
	if content is not None:
		return HttpResponseRedirect(f"/wiki/{entry}")

def pageEdit (request, entry):
	if request.method != "POST":
		content = util.get_entry(entry)
		if content is None:
			return render(request, "encyclopedia/error.html",{
					"message": f'The entry name "{entry}" does not exists. Contact the developer.'
				})
		else:
			return render(request, "encyclopedia/pageedit.html", {
				"entry": entry,
				"content": content
			})

	# POST Requets
	if request.POST.get('cancel'):
		return HttpResponseRedirect(reverse('index'))

	# Save edited entry
	entry = request.POST["entry"]
	content = request.POST["content"]
	util.save_entry(entry, content)
	if content is not None:
		return HttpResponseRedirect(f"/wiki/{entry}")
	else:
		return render(request, "encyclopedia/error.html",{
			"message": f'The entry name "{entry}" does not exists. Contact the developer.'
		})

def pageRandom (request):
	entries = util.list_entries()
	n = len (entries)
	nrand =  randint (0,n-1)
	entry = entries[nrand]
	return HttpResponseRedirect(f"/wiki/{entry}")

def pageDelete (request, entry):
	util.delete_entry(entry)
	return HttpResponseRedirect(reverse('index'))
