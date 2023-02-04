from django.shortcuts import render
from django.http import HttpResponse
from . import scrape_homes


def index(response):
    props_dic = scrape_homes.create_custom_property_dic(
        scrape_homes.expanded_links,
        scrape_homes.expanded_images,
        scrape_homes.expanded_addresses,
        scrape_homes.expanded_prices,
        scrape_homes.expanded_features)

    return render(response, "main/index.html", {"props_dic": props_dic})


def about(response):
    return render(response, "main/about.html", {})
