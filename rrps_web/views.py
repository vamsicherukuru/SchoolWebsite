from django.shortcuts import render
from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import (SixthClassAdmission,SevenClassAdmission,EightClassAdmission
                                    ,NinethClassAdmission,TenthClassAdmission,Announcement)
# Create your views here.

class HomePageView(TemplateView):

    template_name = 'home.html'

class AboutPageView(TemplateView):

    template_name = 'about.html'


class SixInputView(CreateView):

    context_object_name = 'six.html'
    model = SixthClassAdmission
    fields = '__all__'
    template_name = 'six.html'

class SevenInputView(CreateView):

    context_object_name = 'seven.html'
    model = SevenClassAdmission
    fields = '__all__'
    template_name = 'seven.html'

class EigthInputView(CreateView):

    context_object_name = 'eight.html'
    model = EightClassAdmission
    fields = '__all__'
    template_name = 'eight.html'
class NineInputView(CreateView):

    context_object_name = 'nine.html'
    model = NinethClassAdmission
    fields = '__all__'
    template_name = 'nine.html'
class TenInputView(CreateView):

    context_object_name= 'ten.html'
    model = TenthClassAdmission
    fields = '__all__'
    template_name = 'ten.html'
class AdmissionView(TemplateView):
    template_name ='admission_view_page.html'

class SuccessView(TemplateView):
    template_name = 'success_submit.html'
class ClassesListView(TemplateView):

    template_name = 'classes_list_page.html'


class SixListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'home.html'
    context_object_name = 'six_adds'
    model = SixthClassAdmission

    template_name = 'class_six_list.html'

class SevenListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'home.html'
    context_object_name = 'seven_adds'
    model = SevenClassAdmission

    template_name = 'class_seven_list.html'
class EightListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'home.html'
    context_object_name = 'eight_adds'
    model = EightClassAdmission

    template_name = 'class_eight_list.html'
class AnnouncementsListView(ListView):
    context_object_name='announcements'
    model = Announcement
    template_name='announcements_list.html'

class ReviewApplicationsView(TemplateView):
    template_name = 'Recent_applications_list.html'

class SixAddDetailView(DetailView):
    context_object_name = 'six_add_detail'
    model = SixthClassAdmission

    template_name = '6Add_detail_view.html'
class SevenAddDetailView(DetailView):
    context_object_name = 'seven_add_detail'
    model = SevenClassAdmission
    template_name = '7Add_detail_view.html'
class EightAddDetailView(DetailView):
    context_object_name = 'eight_add_detail'
    model = EightClassAdmission

    template_name = '8Add_detail_view.html'
