"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),
    path('talabalar/',talabalar_view, name="talabalar"),
    path('mualliflar/', mualliflar_view, name='Mualliflar'),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('mualliflar/<int:muallif_id>/',muallif_details_view, name="muallif_malumotlari"),
    path('mualliflartop3/',mualliftop3_details_view),
    path('kam_kitobli_mualliflar/',kitoblari_kam_mualliflar_view),
    path('recordlar/', recordlar_view),
    path('recordlar/<int:record_id>/',record_details_view),
    path('talabalar/<int:pk>/o\'chirish/',talaba_delete_view),
    path('talabalar/<int:pk>/tahrirlash/',talaba_update_view),
    path('kitoblar/<int:pk>/tahrirlash/',kitob_update_view),
    path('kutubxonachilar/<int:pk>/tahrirlash/',kutubxonachi_update_view),
    path('recordlar/<int:pk>/tahrirlash/',recordlar_update_view),
    path('mualliflar/<int:pk>/tahrirlash/',mualliflar_update_view),
    path('talabalar/<int:pk>/o\'chirish/confirm/',talaba_delete_confirm_view),
    path('kitoblar/', hamma_kitoblar, name='kitoblar'),
    path('kitob/<int:id>/', kitob_malumotlari, name='kitob_detail'),
    path('recordlar/', hamma_recordlar, name='hamma_recordlar'),
    path('tirik-mualliflar/', tirik_mualliflar, name='tirik_mualliflar'),
    path('eng-katta-kitoblar/', eng_katta_kitoblar, name='eng_katta_kitoblar'),
    path('eng-kop-mualliflar/', eng_kop_mualliflar, name='eng_kop_mualliflar'),
    path('eng-oxirgi-recordlar/', eng_oxirgi_recordlar, name='eng_oxirgi_recordlar'),
    path('tirik-muallif-kitoblari/', tirik_muallif_kitoblari, name='tirik_muallif_kitoblari'),
    path('badiiy-kitoblar/', badiiy_kitoblar, name='badiiy_kitoblar'),
    path('bitiruvchi-recordlar/', bitiruvchi_recordlar, name='bitiruvchi_recordlar'),
    path('kitob/<int:pk>/o\'chirish/',kitob_delete_view),
    path('kitob/<int:pk>/o\'chirish/confirm/',kitob_delete_confirm_view),
    path('kitob-qoshish/',kitob_qoshish_view),
    path('record-qoshish/',record_qoshish_view),
    path('kutubxonachi-qoshish/',kutubxonachi_qoshish_view),
    path('kutubxonachilar/', kutubxonachilar_view),
]
