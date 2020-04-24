from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q
from django.http import HttpResponse
from .models import *
from .forms import *

def is_user(request, customer_id):
    current_customer = UserDetails.objects.get(id=customer_id)
    if not request.user == current_customer:
        return HttpResponse(404)


def create_booking(request, customer_id):
    is_user(request, customer_id)
    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():

            customer = request.user
            customer.save()

            depot = form.cleaned_data['depot']
            vehicle_type = form.cleaned_data['vehicle_type']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            # return depot

            d = Depot.objects.depots(depot)
            vehicle = Vehicle.objects.vehicles(d[0], vehicle_type)


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

            b = Booking.objects.create_booking(customer, v, d[0], start_time, end_time)
            b.save()
            print(b)
            return render(request, 'booking_created.html')

    else:
        form = CreateBookingForm()
        return render(request, 'create_booking.html', {'form' :form})