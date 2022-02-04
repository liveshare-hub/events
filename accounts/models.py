from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UnitKerja(models.Model):
    kode = models.CharField(max_length=3)
    nama_kantor = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.kode} - {self.nama_kantor}'

class Jabatan(models.Model):
    kode = models.CharField(max_length=3)
    nama_jabatan = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.kode} - {self.nama_jabatan}'

class PesertaEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitKerja, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.nama}'
