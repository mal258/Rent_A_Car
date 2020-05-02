from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

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

def booking_detail(request, id=None):
    detail = get_object_or_404(Booking,id=id)
    context = {
        "detail": detail,
    }
    return render(request, 'User/bookingdetails.html', context)

#def create_booking(request, customer_id):
@login_required
@csrf_exempt
def create_booking2(request):
#    print(customer_id)
#    is_user(request, customer_id)

    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            customer = request.user
            customer.save()
            depot = form.cleaned_data['depot']
            vehicle_type = form.cleaned_data['vehicle_type']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            d = Location.objects.depots(depot)
            vehicle = Car.objects.cars(d[0], vehicle_type)
            print(vehicle)
            v = 0
            for item in vehicle:
                bookings = Booking.objects.bookings(depot=d[0], vehicle=item)
                if not bookings:
                    print("inside not booking")
                    v = item
                    break

                for booking in bookings:
                    b_start = booking.start_time - datetime.timedelta(days=2)
                    b_end = booking.end_time + datetime.timedelta(days=2)
#                    print(b_start)
#                    print(b_end)

                    if (start_time > b_end) or (end_time < b_start):
                        v = item
                        break
                if v:
                    break



            #v = item
            if not v:
                print("currently the vehicle is unavailable")
                return HttpResponseRedirect("/car/usersearch/")
            v_status = v.booking_status
            print(v_status)
            b = Booking.objects.create_booking(customer, v, d[0], start_time, end_time)
            print("this is b")
            print(b)
            b.save()
#            print(b)
            #return render(request, 'order_create.html')
            return HttpResponseRedirect(b.get_absolute_url())

    else:
        form = CreateBookingForm()
    return render(request, 'order_create.html', {'form' :form})

def delete_booking(request,id=None):
    query = get_object_or_404(Booking,id = id)
    t_start = query.start_time
    now = timezone.localtime(timezone.now())
    td = t_start - now
    days, seconds = td.days, td.seconds
    hours = days * 24 + seconds // 3600
    print(hours)
    hours = hours*60
    if (hours < 60):
        print("deduct the amount")
    query.delete()
    return HttpResponseRedirect("/car/usersearch/")

def return_vehicle(request, id=None):
    query = get_object_or_404(Booking, id=id)
    t_end = query.end_time
    now = timezone.localtime(timezone.now())
    if (now > t_end):
        td = now - t_end
        days, seconds = td.days, td.seconds
        hours = days * 24 + seconds // 3600
        late_charges = hours * 5
        print("late charge of %d amount is deducted from account", late_charges)
    return HttpResponseRedirect("/car/usersearch/")


