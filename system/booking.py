from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *
from .manager import *

def is_user(request, customer_id):
    current_customer = User.objects.get(id=customer_id)
    if not request.user == current_customer:
        return HttpResponse(404)


def create_booking(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "Create Order"
    }
    return render(request, 'order_create.html', context)

def create_booking1(request):
    form = CreateBookingForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "Create Order"
    }
    return render(request, 'order_create.html', context)

#def create_booking(request, customer_id):
@login_required
@csrf_exempt
def create_booking2(request,customer_id):
    print(customer_id)
    is_user(request, customer_id)
    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
#           customer = form.save(commit=False)
            customer = request.user
            customer.save()
#            print(customer)
            print("printing customer")
            depot = form.cleaned_data['depot']
            vehicle_type = form.cleaned_data['vehicle_type']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            # return depot

            d = Location.objects.depots(depot)
            vehicle = Car.objects.cars(d[0], vehicle_type)


            v = 0
            for item in vehicle:
                bookings = Booking.objects.bookings(depot=d[0], vehicle=item)
                if not bookings:
                    v = item
                    break

                for booking in bookings:
                    b_start = booking.start_time - datetime.timedelta(days=2)
                    b_end = booking.end_time + datetime.timedelta(days=2)

                    if start_time > b_end or end_time < b_start:
                        v = item
                        break
                if v:
                    break

            if not v:
                return -5
            print(customer)
            print(v)
            print(d[0])
            print(start_time)
            print(end_time)
            print(customer)
            b = Booking.objects.create_booking(customer, v, d[0], start_time, end_time)
            print(b)
            b.save()
            print(b)
            return render(request, 'order_create.html')

    else:
        form = CreateBookingForm()
        return render(request, 'order_create.html', {'form' :form})