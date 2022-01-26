from django.shortcuts import render
from .models import City, Subscription
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, FormView
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EditSubscriptionForm
from django.contrib.auth.decorators import login_required
import requests
from .tasks import send


def get_weather_data(city_name):
    r = requests.get(
        'https://api.weatherbit.io/v2.0/current?city={0}&country={1}&key='.format(city_name, 'RU'))
    r_status = r.status_code
    print(r_status)
    send('westftorum@gmail.com')
    if r_status == 200:
        r_json = r.json()
        hum = r_json['data'][0]['rh']
        temp = r_json['data'][0]['temp']
        return hum, temp

# Create your views here.


class SubscriptionView(LoginRequiredMixin, TemplateView):
    template_name = 'subscriptions.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subs'] = Subscription.objects.filter(
            user=self.request.user).all()
        return context


class CityView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cities'] = City.objects.all()
        context['subscriber'] = Subscription.objects.filter(
            user=self.request.user).exists()
        return context


class SubsDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'subs_detail.html'

    def get_context_data(self, pk, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['city'] = City.objects.get(id=pk)
        try:
            hum, temp = get_weather_data(context['city'].name)
            context['city'].temperature = int(temp)
            context['city'].humidity = int(hum)
            context['city'].save()
        except TypeError:
            pass
        context['subscribe_status'] = Subscription.objects.filter(
            user=self.request.user, city=context['city']).exists()
        if context['subscribe_status'] == True:
            context['subscription'] = Subscription.objects.filter(
                user=self.request.user, city=context['city']).get()
        return context


@login_required
def subscribe(request, option, id):
    try:
        subscr = Subscription.objects.filter(
            user=request.user, city=id).exists()

        if int(option) == 0 and subscr == True:
            Subscription.objects.get(user=request.user,
                                     city=id).delete()
        else:
            new_sub = Subscription(
                user=request.user, city=City.objects.get(id=id))
            new_sub.save()
        return HttpResponseRedirect(reverse('subs_detail', args=[str(id)]))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('subs_detail', args=[str(id)]))


@login_required
def EditSubscription(request, id):
    user = request.user.id
    subscription = Subscription.objects.get(user__id=user, city__id=id)
    city = City.objects.get(id=id)
    if request.method == 'POST':
        form = EditSubscriptionForm(request.POST)
        if form.is_valid():
            print(3)
            subscription.period = form.cleaned_data.get('period')
            subscription.save()
            return HttpResponseRedirect(reverse('subs_detail', args=[str(id)]))
    else:
        form = EditSubscriptionForm()

    context = {
        'form': form,
        'city': city,
    }

    return render(request, 'subs_edit.html', context)
