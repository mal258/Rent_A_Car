from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q
import datetime
from .models import Car, Order, PrivateMsg, Location, UserDetails,StartSubscribe
from .forms import CarForm, OrderForm, MessageForm, LocationForm, UserDetail, StartSubcription,DeleteUser
from .tables import PersonTable
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django.shortcuts import render
from .models import UserDetails
from .tables import PersonTable
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    models,
)

User = get_user_model()


def home(request):
    context = {
        "title" : "Rent a Car"
    }
    return render(request,'home.html', context)

def car_list(request):
    car = Car.objects.all()
    print(car)

    query = request.GET.get('q')
    if query:
        car = car.filter(
                     Q(car_name__icontains=query) |
                     Q(company_name__icontains = query) |
                     Q(num_of_seats__icontains=query) |
                     Q(cost_per_day__icontains=query)
                            )

    # pagination
    paginator = Paginator(car, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        car = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car = paginator.page(paginator.num_pages)
    context = {
        'car': car,
    }
    return render(request, 'car_list.html', context)

def car_detail(request, id=None):
    detail = get_object_or_404(Car,id=id)
    context = {
        "detail": detail
    }
    return render(request, 'car_detail.html', context)

def car_created(request):
    form = CarForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/")
    context = {
        "form" : form,
        "title": "Create Car"
    }
    return render(request, 'car_create.html', context)

def car_update(request, id=None):
    detail = get_object_or_404(Car, id=id)
    form = CarForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update Car"
    }
    return render(request, 'car_create.html', context)

#shreyus
def location(request):
    form = LocationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/location")
    context = {
        "form": form,
        "title": "Add Location"
    }
    return render(request, 'addLocation.html', context)

def location_list(request):
    loc = Location.objects.order_by('-id')
    car = Car.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        car = car.filter(
            Q(loc_name__icontains=query) |
            Q(address__icontains=query) |
            Q(vehicle_cap__icontains=query)
        )

    # pagination
    paginator = Paginator(loc, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        loc = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        loc = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        loc = paginator.page(paginator.num_pages)
    context = {
        'loc': loc,
    }
    print(context)
    return render(request, 'location.html', context)

def loc_edit(request,id=None):
    return render(request, 'location.html')

def loc_delete(request,id=None):
    query = get_object_or_404(Location,id = id)
    query.delete()

    location = Location.objects.all()
    context = {
        'location': location,
    }
    return render(request, 'admin_index.html', context)

def loc_detail(request,context):
    return render(request, 'admin_index.html', context)


def car_delete(request,id=None):
    query = get_object_or_404(Car,id = id)
    query.delete()

    car = Car.objects.all()
    context = {
        'car': car,
    }
    return render(request, 'admin_index.html', context)
#customer details

def customer_created(request):
    form = UserDetail(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/car/newcar/")

    context = {
        "form": form,
        "title": "Primary Details"
    }
    return render(request, 'customer_details.html', context)

# Subscription begin

def start_subscription(request):
    form = StartSubcription(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/car/newcar/")

    context = {
        "form": form,
        "title": "start subscription"
    }
    return render(request, 'connected_services.html', context)

# def end_subscription(request):
#     query = get_object_or_404(StartSubscribe, first_name=request.user)
#     query.delete()
#
#     subs = StartSubscribe.objects.all()
#     context = {
#         'delete_subs ': subs,
#     }
#     return render(request, 'connected_services.html', context)




#order

def order_list(request):
    order = Order.objects.all()

    query = request.GET.get('q')
    if query:
        order = order.filter(
            Q(movie_name__icontains=query)|
            Q(employee_name__icontains=query)
        )

    # pagination
    paginator = Paginator(order, 4)  # Show 15 contacts per page
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
        'order': order,
    }
    print(order)
    return render(request, 'order_list.html', context)

def order_detail(request, id=None):
    detail = get_object_or_404(Order,id=id)
    context = {
        "detail": detail,
    }
    return render(request, 'order_detail.html', context)

def order_created(request):
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

def order_update(request, id=None):
    detail = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update Order"
    }
    return render(request, 'order_create.html', context)

def order_delete(request,id=None):
    query = get_object_or_404(Order,id = id)
    query.delete()
    return HttpResponseRedirect("/listOrder/")

def newcar(request):
    new = Car.objects.order_by('-id')
    #seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(car_name__icontains=query) |
            Q(car_type__icontains=query) |
            Q(num_of_seats__icontains=query) |
            Q(cost_per_day__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)

def like_update(request, id=None):
    new = Car.objects.order_by('-id')
    like_count = get_object_or_404(Car, id=id)
    like_count.like+=1
    like_count.save()
    context = {
        'car': new,
    }
    return render(request,'new_car.html',context)

def popular_car(request):
    new = Car.objects.order_by('-like')
    # seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(car_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(num_of_seats__icontains=query) |
            Q(cost_per_day__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)



def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/car")
    context = {
        "form": form,
        "title": "Contact With Us",
    }
    return render(request,'contact.html', context)

#-----------------Admin Section-----------------

def admin_car_list(request):
    car = Car.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        car = car.filter(
            Q(car_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(num_of_seats__icontains=query) |
            Q(cost_per_day__icontains=query)
        )

    # pagination
    paginator = Paginator(car, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        car = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car = paginator.page(paginator.num_pages)
    context = {
        'car': car,
    }
    print(context)
    return render(request, 'admin_index.html', context)

def admin_msg(request):
    msg = PrivateMsg.objects.order_by('-id')
    context={
        "car": msg,
    }
    return render(request, 'admin_msg.html', context)

def admin_pge(request):
    return render(request, 'admin/admin_home.html')


def msg_delete(request,id=None):
    query = get_object_or_404(PrivateMsg, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")





class PersonListView(ListView):
    model = Post = UserDetails
    template_name = 'user_summary.html'

    def get_queryset(self):
        user = get_object_or_404(UserDetails, username=self.kwargs.get('first_name'))
        return UserDetails.objects.filter(author=user)

    def get_username_field(self):
        user = get_object_or_404(UserDetails, username=self.kwargs.get('username'))
        return UserDetails.objects.filter(user=user)

def PersonListView(request):
    #expiry_date = UserDetails.objects.get("start_date")
    #print(expiry_date)
    user_list = UserDetails.objects.filter(first_name=request.user)
    sub_list = StartSubscribe.objects.filter(first_name=request.user)

    e = StartSubscribe.objects.get(id=2)
    e.start_date += datetime.timedelta(days=180)
    e.save()
    print(sub_list)
    print(StartSubscribe.objects.filter("start_date"))
    return render(request, 'user_summary.html', {'obj1': user_list,'obj2': sub_list})


def end_subscription(request):

    user = User.objects.get(username=request.user)
    logout(request)
    user.delete()
    context = {
        "deleted_msg": "Account has been deleted",
    }
    return render(request, 'delete_subscription.html', context) and HttpResponseRedirect('/logout/')


def extend_subscription(request):
    #expiry_date = UserDetails.objects.get("start_date")
    #print(expiry_date)
    user_list = UserDetails.objects.filter(first_name=request.user)
    sub_list = StartSubscribe.objects.filter(first_name=request.user)
    k = StartSubscribe.objects.get(id=2)

    k.start_date += datetime.timedelta(days=5)
    k.save()
    return render(request, 'renew_subscription.html', {'obj8': user_list,'obj9': sub_list})