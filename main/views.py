from re import search

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .form import TalabaForm, MuallifForm, RecordForm, KutubxonachiForm
from .models import *
from django import forms
def home_view(request):
    return render(request, 'index.html')
def talabalar_view(request):
    form = TalabaForm
    if request.method == "POST":
        talaba_form = TalabaForm(request.POST)
        if talaba_form.is_valid():
            talaba_form.save()

        return redirect('talabalar')

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
        "form":form
    }

    return render(request, 'talabalar.html', context)

def mualliflar_view(request):
    mualliflar= Muallif.objects.all()
    form = MuallifForm
    if request.method == "POST":
        muallif_form = MuallifForm(request.POST)
        if muallif_form.is_valid():
            muallif_form.save()
        return redirect('Mualliflar')
    context = {
        'mualliflar':mualliflar,
        "form": form,
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
    context={
        'kitob': kitob
    }
    return render(request, 'kitob_detail.html',context )

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
def kitob_qoshish_view(request):
    if request.method == "POST":
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            annotatsiya=request.POST.get('annotatsiya'),
            sahifa=request.POST.get('sahifa'),
            janr=request.POST.get('janr'),
            muallif_id=request.POST.get('muallif_id')
        )
        return redirect("hamma_kitoblar")

    mualliflar = Muallif.objects.all()
    return render(request, 'kitob-qoshish.html', {"mualliflar": mualliflar})
def record_qoshish_view(request):
    form = RecordForm
    if request.method == "POST":
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            record_form.save()
        return redirect("/recordlar/")
    context= {
        "form":form
    }

    return render(request, 'record_qoshish.html', context)
def kutubxonachilar_view(request):
    kutubxonachilar = Kutubxonachi.objects.all()
    context={
        "kutubxonachilar":kutubxonachilar
    }
    return render(request, 'kutubxonachilar.html', context)
def kutubxonachi_qoshish_view(request):
    form = KutubxonachiForm
    if request.method == "POST":
        kutubxonachi_form = KutubxonachiForm(request.POST)
        kutubxonachi_form.save()
        return redirect("/kutubxonachilar/")
    context = {
        "form": form,
    }
    return render(request,"kutubxonachi_qoshish.html", context)

def talaba_update_view(request, pk):
    if request.method == "POST":
        talaba = Talaba.objects.filter(pk=pk)
        talaba.update(
            ism=request.POST.get("ism"),
            kurs=request.POST.get("kurs"),
            guruh=request.POST.get("guruh"),
            yosh=request.POST.get("yosh"),
            kitob_soni=request.POST.get("kitob_soni"),
        )
        return redirect("talabalar")
    talaba = get_object_or_404(Talaba, pk=pk)
    context = {
        "talaba":talaba,
    }
    return render(request,"talaba_update.html", context)
def kitob_update_view(request, pk):

    if request.method == "POST":
        kitob = Kitob.objects.filter(pk=pk)
        kitob.update(
            nom=request.POST.get("nom"),
            annotatsiya=request.POST.get("annotatsiya"),
            sahifa=request.POST.get("sahifa"),
            janr=request.POST.get("janr"),
            muallif=Muallif.objects.get(id=request.POST.get("muallif_id")),
        )
        return redirect("kitoblar")
    kitob = get_object_or_404(Kitob, pk=pk)
    mualliflar = Muallif.objects.exclude(id=kitob.muallif.id).order_by('ism')
    context = {
        "kitob":kitob,
        "mualliflar":mualliflar,
    }
    return render(request,"kitob_update.html", context)
def kutubxonachi_update_view(request, pk):
    if request.method == "POST":
        kutubxonachi = Kutubxonachi.objects.filter(pk=pk)
        kutubxonachi.update(
            ism=request.POST.get("ism"),
            ish_vaqti=request.POST.get("ish_vaqti"),

        )
        return redirect("kutubxonachilar")
    kutubxonachi = get_object_or_404(Kutubxonachi, pk=pk)
    context = {
        "kutubxonachi": kutubxonachi,
    }
    return render(request,"kutubxonach_update.html", context)
def mualliflar_update_view(request, pk):
    muallif= Muallif.objects.filter(pk=pk)
    form = MuallifForm
    if request.method == "POST":
        muallif_form = MuallifForm(muallif, request.POST)
        muallif_form.save()
        return redirect("muallif_malumotlari", muallif_id=pk)
    muallif = get_object_or_404(Muallif, pk=pk)
    context = {
        'muallif':muallif,
        'form':form,
    }
    return render(request, 'muallif_update.html', context)
def recordlar_update_view(request, pk):
    record= Record.objects.filter(pk=pk)
    if request.method == "POST":
        if request.POST.get('qaytarilgan_sana') == '':
            qaytarilgan_sana= None
        else:
            qaytarilgan_sana=request.POST.get('qaytarilgan_sana')
        record.update(
            qaytarilgan_sana=qaytarilgan_sana,
            qaytardi=request.POST.get('qaytardi') == 'on',
        )
        return redirect("/recordlar/")
    record = get_object_or_404(Record, pk=pk)
    context = {
        'record':record,
    }
    return render(request, 'record_update.html', context)