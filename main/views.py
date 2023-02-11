# from django import request
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import scrape_homes
from .forms import SearchPostals


def index(request):
    form = SearchPostals()

    postal_code = None

    if request.GET.get('postal_code'):
        pc = request.GET.get('postal_code')
        props_dic = scrape_homes.create_custom_property_dic(pc)

        return render(request, "main/index.html", {"form": form, "props_dic": props_dic})
    else:
        return render(request, "main/index.html", {"form": form})


def about(response):
    return render(response, "main/about.html", {})
