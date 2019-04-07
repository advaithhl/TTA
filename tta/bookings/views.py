from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'bookings/view.html', {'bookings':bookings})


def new_booking(request):
    return HttpResponse('New Bookings are not available yet!')