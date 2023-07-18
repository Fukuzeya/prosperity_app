from django.shortcuts import render
from django.contrib.postgres.search import SearchVector

from Batch.models import Batch
from Company.models import Company
from Response.forms import SearchForm
from Record.models import Record

# Create your views here.


def responses(request):
    company_id = request.session.get('company_id')
    company = Company.objects.get(id=company_id)
    batches = company.company_batches.filter(status = Batch.Status.SUCCESS)
    return render(request,'dashboard/responses.html',{'batches':batches})

def success_responses(request,id):
    batch = Batch.objects.get(id =id)
    responses = batch.responses.filter(status = 'SUCCESS')
    return render(request,'dashboard/response_type.html',{'responses':responses})

def failed_responses(request,id):
    batch = Batch.objects.get(id =id)
    responses = batch.responses.filter(status = 'FAILED')
    return render(request,'dashboard/response_type.html',{'responses':responses})

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Record.published.annotate(
                search=SearchVector('title', 'body'),).filter(search=query)

    return render(request,'blog/post/search.html',
                  {'form': form,'query': query,'results': results})