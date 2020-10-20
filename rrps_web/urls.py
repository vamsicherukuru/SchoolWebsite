from django.urls import path
from . import views

app_name = 'rrps_web'

urlpatterns =[
    path('',views.HomePageView.as_view(),name='home'),
    path('about/',views.AboutPageView.as_view(),name='about'),
    path('six/',views.SixInputView.as_view(),name='sixthAdd'),
    path('seven/',views.SevenInputView.as_view(),name='sevenAdd'),
    path('eight/',views.EigthInputView.as_view(),name='eightAdd'),
    path('nine/',views.NineInputView.as_view(),name='nineAdd'),
    path('ten/',views.TenInputView.as_view(),name='tenthAdd'),
    path('admission/',views.AdmissionView.as_view(),name='admission_panel'),
    path('state/',views.SuccessView.as_view(),name='success'),
    path('standards/',views.ClassesListView.as_view(),name='classes_list'),
    path('sixaddlist/',views.SixListView.as_view(),name='six_adds_list'),
    path('sevenaddlist/',views.SevenListView.as_view(),name='seven_adds_list'),
    path('eightaddlist/',views.EightListView.as_view(),name='eight_adds_list'),
    path('announcements/',views.AnnouncementsListView.as_view(),name='announcements'),
    path('reviewadds/',views.ReviewApplicationsView.as_view(),name='review'),
    path('sixaddlist/<int:pk>/',views.SixAddDetailView.as_view(),name='six_details'),
    path('sevenaddlist/<int:pk>/',views.SevenAddDetailView.as_view(),name='seven_details'),
    path('eightaddlist/<int:pk>/',views.EightAddDetailView.as_view(),name='eight_details'),


]
