from django.shortcuts import render
from .models import Jewelry, JewelryInstance, Stone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    text_head = 'На нашем сайте вы можете заказть и приобрести украшения ручной работы'
    name = 'Магия камней'
    jewelry = Jewelry.objects.all()
    num_jewelry = Jewelry.objects.all().count()
    rab1 = 'Только натуральные камни премиум качества'
    rab2 = 'Все украшения ручной работы'
    rab3 = 'Создание украшений по индивидуальному заказу'
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'text_head': text_head, 'name': name, 'num_jewelry': num_jewelry,
               'jewelry': jewelry, 'rab1': rab1, 'rab2': rab2, 'rab3': rab3, 'num_visits': num_visits}

    # передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)


class JewelryListView(generic.ListView):
    model = Jewelry
    context_object_name = 'jewelry'
    paginate_by = 3


class JewelryDetailView(generic.DetailView):
    model = Jewelry
    context_object_name = 'jewelry'


class StoneListView(generic.ListView):
    model = Stone
    paginate_by = 4


class StoneDetailView(generic.DetailView):
    model = Stone


class LoanerJewelryByUserListView(LoginRequiredMixin, generic.ListView):
    model = JewelryInstance
    template_name = 'catalog/jewelryinstance_list_customer_user.html'
    paginate_by = 10

    def get_queryset(self):
        return JewelryInstance.objects.filter(
            customer=self.request.user).filter(status__exact='4').order_by('due_back')


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
