from django.shortcuts import render
from .models import Jewelry, JewelryInstance, Stone
from django.views.generic import ListView, DetailView


def index(request):
    text_head = 'На нашем сайте вы можете заказть и приобрести украшения ручной работы'
    name = 'Магия камней'
    rab1 = 'Только натуральные камни премиум качества'
    rab2 = 'Все украшения ручной работы'
    rab3 = 'Создание украшений по индивидуальному заказу'

    context = {'text_head': text_head, 'name': name, 'rab1': rab1, 'rab2': rab2, 'rab3': rab3}

    # передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)


class JewelryListView(ListView):
    model = Jewelry
    context_object_name = 'jewelry'
    paginate_by = 3


class JewelryDetailView(DetailView):
    model = Jewelry
    context_object_name = 'jewelry'


class StoneListView(ListView):
    model = Stone
    paginate_by = 4


class StoneDetailView(DetailView):
    model = Stone

def about(request):
    text_head = 'Сведения о мазазине'
    name = 'ООО "Магия камней"'

    context = {'text_head': text_head, 'name': name}

    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Магия камней"'
    address = 'Москва, ул. Красная, д.15, к.105'
    tel = '495-223-55-55'
    email = 'magic_stone@mail.ru'
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
               'name': name, 'address': address,
               'tel': tel,
               'email': email}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/contact.html', context)
