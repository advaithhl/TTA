from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import SearchForm

bookings = [
    {
        'train_no': 16601,
        'train_name': 'Jan Shatabdi',
        'source': 'Kollam',
        'destination': 'Kochi',
        'doj': '8 April, 2019',
        'ticket_cnt': 3
    },
    {
        'train_no': 16351,
        'train_name': 'Venad',
        'source': 'Kochi',
        'destination': 'Trivandrum',
        'doj': '20 May, 2019',
        'ticket_cnt': 4
    },
    {
        'train_no': 55901,
        'train_name': 'Malabar Express',
        'source': 'Kannur',
        'destination': 'Kollam',
        'doj': '21 June, 2019',
        'ticket_cnt': 4
    },
]


@login_required
def view_booking(request):
    return render(request, 'bookings/view.html', {'bookings': bookings})


@login_required
def wallet(request):
    return render(request, 'bookings/wallet.html')


@login_required
def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            source = search_form.cleaned_data.get('source')
            messages.success(request, f'Source: {source}')
            # redirect to results page later
            return redirect('search')
    else:
        search_form = SearchForm()
    return render(request, 'bookings/search.html', {'form': search_form})
