from re import search

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
def home_view(request):
    return render(request, 'index.html')
def talabalar_view(request):
    search = request.GET.get('search', '').strip()
    kurs = request.GET.get('kurs', 'all')
    guruh = request.GET.get('guruh', 'all')

    talabalar = Talaba.objects.all()

    if search:
        talabalar = talabalar.filter(ism__icontains=search)

    if guruh and guruh != 'all':
        talabalar = talabalar.filter(guruh=guruh)

    if kurs and kurs != 'all':
        talabalar = talabalar.filter(kurs=int(kurs))

    guruhlar = Talaba.objects.order_by('guruh').values_list('guruh', flat=True).distinct()
    kurslar = [1, 2, 3, 4]

    context = {
        'talabalar': talabalar,
        "search": search,
        "guruhlar": guruhlar,
        "kurs_query": kurs,
        "guruh_query": guruh,
        "kurslar": kurslar,
    }

    return render(request, 'talabalar.html', context)

def mualliflar_view(request):
    mualliflar= Muallif.objects.all()
    context = {
        'mualliflar':mualliflar,
    }
    return render(request, 'mualliflar.html', context)
def talaba_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        "talaba":talaba,

    }
    return render(request, 'talaba.html', context)
def muallif_details_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        "muallif":muallif,
    }
    return render(request, 'muallif.html', context)
def mualliftop3_details_view(request):
    mualliflar = Muallif.objects.order_by('t_sana')[:3]
    context = {
        "mualliflar": mualliflar,
    }
    return render(request, 'mualliflartop.html', context)
def kitoblari_kam_mualliflar_view(request):
    mualliflar = Muallif.objects.filter(kitob_soni__lt=10)
    context = {
        "mualliflar": mualliflar,
    }
    return render(request, 'kam_kitobli_mualliflar.html', context)
def recordlar_view(request):
    recordlar= Record.objects.all()
    context = {
        'recordlar':recordlar,
    }
    return render(request, 'recordlar.html', context)
def record_details_view(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        "record": record,
    }
    return render(request, 'record_details.html', context)
def talaba_delete_view(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk)
    talaba.delete()
    return redirect('talabalar')
def talaba_delete_confirm_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    context = {
        "talaba":talaba,
    }
    return render(request,'talaba_delete_confirm.html', context)
def hamma_kitoblar(request):
    search = request.GET.get('search', '').strip()
    janr_query = request.GET.get('janr', 'all')

    kitoblar = Kitob.objects.all()

    if search:
        kitoblar = kitoblar.filter(nom__icontains=search)

    if  janr_query != 'all':
        kitoblar = kitoblar.filter(janr=janr_query)

    janrlar = Kitob.objects.order_by('janr').values_list('janr', flat=True).distinct()

    context = {
        'kitoblar': kitoblar,
        "search": search,
        "janrlar": janrlar,
        "janr_query": janr_query,
    }

    return render(request, 'kitoblar.html', context)
def kitob_malumotlari(request, id):
    kitob = get_object_or_404(Kitob, id=id)
    return render(request, 'kitob_detail.html', {'kitob': kitob})

def hamma_recordlar(request):
    recordlar = Record.objects.all()
    return render(request, 'recordlar.html', {'recordlar': recordlar})

def tirik_mualliflar(request):
    mualliflar = Muallif.objects.filter(tirik=True)
    return render(request, 'mualliflar2.html', {'mualliflar': mualliflar})

def eng_katta_kitoblar(request):
    kitoblar = Kitob.objects.order_by('-sahifa')[:3]
    return render(request, 'kitoblar.html', {'kitoblar': kitoblar})

def eng_kop_mualliflar(request):
    mualliflar = Muallif.objects.order_by('-kitob_soni')[:3]
    return render(request, 'mualliflar.html', {'mualliflar': mualliflar})

def eng_oxirgi_recordlar(request):
    recordlar = Record.objects.order_by('-olingan_sana')[:3]
    return render(request, 'recordlar.html', {'recordlar': recordlar})

def tirik_muallif_kitoblari(request):
    kitoblar = Kitob.objects.filter(muallif__tirik=True)
    return render(request, 'kitoblar.html', {'kitoblar': kitoblar})

def badiiy_kitoblar(request):
    kitoblar = Kitob.objects.filter(janr='badiiy')
    return render(request, 'kitoblar.html', {'kitoblar': kitoblar})
def record_malumotlari(request, id):
    record = get_object_or_404(Record, id=id)
    return render(request, 'record_details.html', {'record': record})

def bitiruvchi_recordlar(request):
    recordlar = Record.objects.filter(talaba__kurs=4)
    return render(request, 'recordlar.html', {'recordlar': recordlar})
def kitob_delete_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    kitob.delete()
    return redirect('talabalar')
def kitob_delete_confirm_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    context = {
        "kitob":kitob,
    }
    return render(request, 'kitob_delete_confirm.html', context)