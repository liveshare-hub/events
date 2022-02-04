from django.db import models
from django.core.files import File

import uuid, qrcode
from io import BytesIO
from PIL import Image, ImageDraw

from accounts.models import PesertaEvent


class BuatEvent(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    tgl_event = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tgl_event} - {self.judul}'


class DaftarEvent(models.Model):
    peserta = models.ForeignKey(PesertaEvent, on_delete=models.CASCADE)
    event = models.ForeignKey(BuatEvent, on_delete=models.CASCADE)
    url_uuid = models.UUIDField(default=uuid.uuid4())
    myqrcode = models.ImageField(upload_to='qrcode/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.peserta.nama} - {self.event.judul}'

    def save(self, *args, **kwargs):
        
        qr = qrcode.QRCode(
            version=20,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=30,
            border=4,
        )
        qr.add_data(f'http://localhost:8000/activation/{self.url_uuid}')
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        canvas = Image.new('RGB', (300,300), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_img)
        fname = f'{self.peserta.user.username} - {self.event.judul}.PNG'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.myqrcode.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
