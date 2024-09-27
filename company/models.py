from django.db import models

class Kompaniya(models.Model):
    KOMPANIYA_OLCHAMI = [
        ('kichik', 'Kichik'),
        ('orta', 'O\'rta'),
        ('katta', 'Katta'),
    ]

    nomi = models.CharField(max_length=200, verbose_name="Kompaniya nomi")
    tavsif = models.TextField(verbose_name="Kompaniya haqida qisqacha ma'lumot")
    joylashuv = models.CharField(max_length=200, verbose_name="Kompaniya joylashuvi")
    veb_sayt = models.URLField(verbose_name="Kompaniyaning veb-sahifasi")
    sanoat = models.CharField(max_length=100, verbose_name="Sanoat turi")
    olchami = models.CharField(max_length=10, choices=KOMPANIYA_OLCHAMI, verbose_name="Kompaniya o'lchami")
    tashkil_etilgan_sana = models.DateField(verbose_name="Kompaniya tashkil etilgan sana")

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Kompaniya"
        verbose_name_plural = "Kompaniyalar"
