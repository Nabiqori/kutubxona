from django.db import models
from django.db.models import SET_NULL


class Muallif(models.Model):
    JINS_CHOICES = (
        ('Erkak', "Erkak"),
        ('Ayol', 'Ayol')
    )
    ism = models.CharField(max_length=100)
    davlat = models.CharField(max_length=100)
    kitob_soni = models.PositiveSmallIntegerField(null=True, blank=True)
    t_sana = models.DateField()
    tirik = models.BooleanField(default=False)
    jins = models.CharField(max_length=10, choices=JINS_CHOICES)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Mualliflar'


class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    annotatsiya = models.TextField(blank=True, null=True)
    janr = models.CharField(max_length=255)
    sahifa = models.PositiveIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Kitoblar'


class Kutubxonachi(models.Model):
    ISH_VAQTI_CHOICES = (
        ('08:00-13:00', "08:00-13:00"),
        ('13:00-18:00', '13:00-18:00')
    )
    ism = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=15, choices=ISH_VAQTI_CHOICES)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Kutubxonachilar'


class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    kurs = models.PositiveSmallIntegerField(default=1)
    guruh = models.CharField(max_length=10)
    yosh = models.PositiveSmallIntegerField()
    kitob_soni = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Talabalar'


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=SET_NULL, null=True, blank=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=SET_NULL, null=True, blank=True)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytarilgan_sana = models.DateTimeField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __tr__(self):
        return self.talaba

    class Meta:
        verbose_name_plural = 'rekordlarlar'

