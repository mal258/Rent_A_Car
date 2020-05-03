from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import pytz
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import *
from .manager import *

def sf_time():
    sf =  pytz.timezone("America/Los_Angeles")
    timezone.activate(sf)

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
                    print(booking)
                    b_start = booking.start_time - datetime.timedelta(days=2)
                    b_end = booking.end_time + datetime.timedelta(days=2)

                    if (start_time > b_end) or (end_time < b_start):
                        v = item
                        break
                if v:
                    break

            #v = item
            if not v:
                print("currently the vehicle is unavailable")
                return HttpResponseRedirect("/car/acar/")
            v_status = v.booking_status
            print(v_status)
            b = Booking.objects.create_booking(customer, v, d[0], start_time, end_time)
            if b == 1:
                print("Please book for less than 72 hours")
                return HttpResponseRedirect("/car/usersearch")
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
    customer = request.user
    sf_time()
    t_start = query.start_time
    now = timezone.localtime(timezone.now())
    print(now)
    td = t_start - now
    days, seconds = td.days, td.seconds
    hours = days * 24 + seconds // 3600
    print(hours)
    hours = hours*60
    if (hours < 60):
        print("deduct the amount")
    else:
        print("amount refunded")
    v = query.vehicle
    Car.objects.update_status(v)
    query.delete()
    return HttpResponseRedirect("/car/usersearch/")

def return_vehicle(request, id=None):
    query = get_object_or_404(Booking, id=id)
    sf_time()
    t_end = query.end_time
    now = timezone.localtime(timezone.now())
    if (now > t_end):
        td = now - t_end
        days, seconds = td.days, td.seconds
        hours = days * 24 + seconds // 3600
        late_charges = hours * 5
        print("late charge of %d amount is deducted from account", late_charges)
    v = query.vehicle
    Car.objects.update_status(v)
    query.delete()
    #return HttpResponseRedirect("/car/usersearch/")
    return render(request, 'User/return_car.html')

def update_booking(request, id=None):
    detail = get_object_or_404(Booking, id=id)
    form = CreateBookingForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update Order"
    }
    return render(request, 'order_create.html', context)

def customer_list(request):
    c_list = UserDetails.objects.all()
    print(c_list)

    query = request.GET.get('q')
    if query:
        c_list = c_list.filter(
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)
        )

    # pagination
    paginator = Paginator(c_list, 4)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    context = {
        'c_list': c_list,
    }
    print(c_list)
    return render(request, 'admin/admin_cust_view.html', context)

def cust_sub_term(request, id=None):
    query = get_object_or_404(UserDetails, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")

def cust_booking1 (request):
    detail = get_object_or_404(Booking,customer=request.user)
    context = {
        "detail": detail,
    }
    return render(request, 'User/bookingdetails.html', context)

def cust_booking (request):
    c_book = Booking.objects.filter(customer=request.user)
    query = request.GET.get('q')
    if query:
        c_book = c_book.filter(
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)
        )

    # pagination
    paginator = Paginator(c_book, 4)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    context = {
        'c_book': c_book,
    }
    #print(c_book)
    return render(request, 'User/mybooking.html', context)

