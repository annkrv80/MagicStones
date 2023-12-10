from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('jewelry/', views.JewelryListView.as_view(), name='jewelry-list'),
    path('jewelry/<int:pk>/', views.JewelryDetailView.as_view(), name='jewelry-detail'),
    path('stone/', views.StoneListView.as_view(), name='stone-list'),
    path('stone/<int:pk>', views.StoneDetailView.as_view(), name='stone-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]