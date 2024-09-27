from django.db import models

from elonlar.models import Elonlar
from user.models import Userlar

class Ariza(models.Model):
    ARIZA_HOLATI = [
        ('ko\'rib_chiqilmoqda', 'Ko\'rib chiqilmoqda'),
        ('rad_etildi', 'Rad etildi'),
        ('qabul_qilindi', 'Qabul qilindi'),
    ]

    user = models.ForeignKey(Userlar, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    job = models.ForeignKey(Elonlar, on_delete=models.CASCADE, verbose_name="Ish e'loni")
    cover_letter = models.TextField(verbose_name="Motivatsiya xati")
    status = models.CharField(max_length=20, choices=ARIZA_HOLATI, default='ko\'rib_chiqilmoqda', verbose_name="Ariza holati")
    date_applied = models.DateTimeField(auto_now_add=True, verbose_name="Ariza topshirilgan sana")

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"

    class Meta:
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"
