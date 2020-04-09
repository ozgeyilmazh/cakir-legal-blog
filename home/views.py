from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Makale
from .forms import MakaleForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def hakkimizda_view(request):
    return render(request, 'kurumsal/hakkimizda.html')

def ekibimiz_view(request):
    return render(request, 'kurumsal/ekibimiz.html')

def bvmb_view(request):
    return render(request, 'kurumsal/bvmb.html')

def odemebilgileri_view(request):
    return render(request, 'kurumsal/odemebilgileri.html')

def sosyalsorumluluk_view(request):
    return render(request, 'kurumsal/sosyalsorumluluk.html')

def faaliyetalanlarimiz_view(request):
    return render(request, 'faaliyetalanlarimiz.html')

def bizeulasin_view(request):
    return render(request, 'iletisim/bizeulasin.html')

def kariyer_view(request):
    return render(request, 'iletisim/kariyer.html')

def bursbasvurusu_view(request):
    return render(request, 'iletisim/bursbasvurusu.html')

def vekaletbilgileri_view(request):
    return render(request, 'iletisim/vekaletbilgileri.html')

def makale_index(request):
    makale_list = Makale.objects.all()
    query = request.GET.get('q')
    if query:
        makale_list = makale_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(makale_list, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        makales = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        makales = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        makales = paginator.page(paginator.num_pages)

    return render(request, "makale.html", {'makales': makales})

def makale_detail(request, slug):
    makale = get_object_or_404(Makale, slug=slug)

    context = {
        'makale': makale,
    }
    return render(request, "makale_detail.html", context)