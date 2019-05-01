from time import sleep
from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse

from .forms import AddMoneyForm, SearchForm
from .models import Train

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
    if request.method == 'POST':
        addmoney_form = AddMoneyForm(request.POST)
        if addmoney_form.is_valid():
            increment = int(addmoney_form.cleaned_data.get('amount'))
            wallet_obj = request.user.passenger.wallet
            wallet_obj.balance += increment
            wallet_obj.save()
            messages.success(request, f'Added money successfully')
            # sleep is to make the redirect more natural feeling
            sleep(0.5)
            return redirect('wallet')
    else:
        addmoney_form = AddMoneyForm()
    return render(request, 'bookings/wallet.html', {'form': addmoney_form})


@login_required
def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            src = search_form.cleaned_data.get('source')
            dst = search_form.cleaned_data.get('destination')
            doj = search_form.cleaned_data.get('doj').strftime("%b %d, %Y")
            trains = Train.objects.filter(
                source=src, destination=dst)
            if trains:
                return render(request, 'bookings/search_results.html',
                              {'trains': trains, 'source': src, 'destination': dst, 'doj': doj})
            else:
                messages.error(request, f'No trains found from {src} to {dst}')
                return redirect('search')

            '''
            base_url = reverse('search-results')
            query_string = urlencode({'src': src, 'dst': dst, 'doj': doj})
            url = f'{base_url}?{query_string}'
            return redirect(url)
            '''
    else:
        search_form = SearchForm()
    return render(request, 'bookings/search.html', {'form': search_form})
