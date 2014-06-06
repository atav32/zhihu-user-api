from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from search.forms import SearchForm

class SearchPageView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        template_name = 'search.html'
        return render(request, template_name)
