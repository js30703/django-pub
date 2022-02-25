from typing import Tuple
from django.db import models
from multiselectfield import MultiSelectField
from app.base.models import BaseModel


class ICF001(BaseModel):
    ga_id = models.CharField("ga_id", max_length=50, null=True, blank=True)
    q1 = models.CharField("Nama lengkap calon pasien", max_length=50)
    q2 = models.CharField("Nomor HP/ Whatsapp calon pasien", max_length=50)
    q7 = models.CharField("Email calon pasien", max_length=50)
    q3 = models.CharField("Alamat domisili calon pasien", max_length=50)
    q4 = models.CharField("Pekerjaan calon pasien", max_length=50)
    q5 = models.CharField("Tempat dan tanggal lahir calon pasien", max_length=50)
    Q6_CHOICES = (
    ('Rekomendasi Teman/Keluarga/Kenalan', 'Rekomendasi Teman/Keluarga/Kenalan'),
    ('Google', 'Google'),
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('lainnya', 'lainnya'),
    )
    q6 = MultiSelectField("Dari manakah Anda tahu Indental Clinic? (Mohon pilih salah satu)", choices=Q6_CHOICES ,max_length=50)
    q6_other = models.CharField("Jika Anda memilih 'lainnya', tolong tuliskan jawaban Anda di bawah", max_length=50,  blank=True, null=True)
    
    
    class Meta:
        verbose_name = "Form_N01"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.q1}"

class IFC001_2(BaseModel):
    
    origin = models.OneToOneField("survey.ICF001", verbose_name="1페이지", on_delete=models.CASCADE)
    q1 = models.CharField("Pada tanggal berapa dan hari apa Anda berencana melakukan perawatan/ konsultasi ke Indental Clinic?", max_length=250)
    Q2_CHOICES = (
    ('Konsultasi', 'Konsultasi'),
    ('Kontrol ortodonti', 'Kontrol ortodonti'),
    ('Tambai gigi', 'Tambai gigi'),
    ('Scaling', 'Scaling'),
    ('Lainnya', 'Lainnya'),
    )
    BOOL_CHOICES = ((True, 'IYA'), (False, 'TIDAK'))
    q2 = models.CharField("Perawatan apa yang rencananya hendak Anda lakukan di Indental Clinic?",choices=Q2_CHOICES ,max_length=50)
    q2_other = models.CharField("Jika Anda memilih 'lainnya', tolong tuliskan jawaban Anda di bawah", max_length=50, blank=True, null=True)
    q3 = models.TextField("Mohon berikan penjelasan singkat tentang keluhan yang Anda alami. Misalnya: Gigi bagian mana yang terasa sakit? Bagaimana keluhan sakitnya? Apakah terasa nyeri atau ngilu ketika makan?", help_text="yes=true, no=false")
    q4 = models.BooleanField("Apakah Anda mengalami demam >38° C dalam kurun waktu 14 hari terakhir?", default=False, choices=BOOL_CHOICES)
    q5 = models.BooleanField("Apakah Anda mengalami batuk/ pilek/ nyeri tenggorokan dalam kurun waktu 14 hari terakhir?", default=False, choices=BOOL_CHOICES)
    q6 = models.BooleanField("Apakah Anda mengalami sesak napas dalam kurun waktu 14 hari terakhir?", default=False, choices=BOOL_CHOICES)
    q7 = models.BooleanField("Apakah anda mengalami anosmia ( indera penciuman berkurang) dalam kurun 14 hari terakhir? ", default=False, choices=BOOL_CHOICES)
    q8 = models.BooleanField("Apakah anda mengalami diare / mual / muntah / nyeri perut dalam kurun 14 hari terakhir? ", default=False, choices=BOOL_CHOICES)
    q9 = models.BooleanField("Apakah Anda bekerja atau mengunjungi fasilitas kesehatan yang berhubungan dengan kasus pasien konfirmasi COVID-19?", default=False, choices=BOOL_CHOICES)
    q10 = models.BooleanField("Apakah Anda bekerja atau menghadiri perkumpulan massal/tempat ibadah/arisan/pesta/pasar atau tempat jasa (bandara, bank, dll)?", default=False, choices=BOOL_CHOICES)
    q11 = models.BooleanField("Apakah keluarga Anda (1 rumah) bekerja atau bepergian ke tempat dengan kasus positif/berisiko?", default=False, choices=BOOL_CHOICES)
    q12 = models.BooleanField("Apakah lingkungan sekitar Anda didapatkan kasus konfirmasi COVID-19 (tempat tinggal atau tempat kerja)?", default=False, choices=BOOL_CHOICES)
    q13 = models.BooleanField("Apakah Anda pernah melakukan tes COVID-19 sebelumnya?", default=False, choices=BOOL_CHOICES)
    q14 = models.DateField("Jika ya, kapan Anda melakukan tes tersebut?", auto_now=False, auto_now_add=False, null=True)
    
    q15 = models.BooleanField("Jika ya, apa hasil dari rapid test COVID-19 Anda?", default=False, choices=((True, 'Reaktif'), (False, 'Non-reaktif')))
    q16 = models.BooleanField("Jika ya, apa hasil dari tes swab COVID-19 Anda?", default=False, choices=((True, 'Positif'), (False, 'Negatif')))
    
    Q17_CHOICES = (
    ('A1', 'Mengisi formulir ini dengan lengkap dan sebenar-benarnya, paling lambat satu hari sebelum pasien datang ke Indental Clinic'),
    ('A2', 'Memakai masker selama berada di area Indental Clinic'),
    ('A3', 'Ketika tiba dan sebelum melakukan perawatan di Indental Clinic, pasien dimohon untuk mencuci tangan (sesuai panduan WHO) di wastafel yang tersedia di klinik'),
    ('A4', 'Bagi para pengantar, dimohon untuk menunggu di ruang tunggu dan tidak masuk ke ruang perawatan (kecuali untuk pasien anak-anak)'),
    ('A6', 'Sebelum memulai prosedur perawatan, pasien diharapkan untuk berkumur dengan betadine yang telah disediakan di dental unit selama 20-30 detik'),
    )
    q17 = MultiSelectField("Demi keselamatan dan kesehatan bersama, saya bersedia melakukan hal-hal di bawah ini ketika saya melakukan perawatan di Indental Clinic (mohon untuk memberi tanda centang)", 
    min_choices=5,
    choices=Q17_CHOICES ,
    max_length=50)


    class Meta:
        verbose_name = "Form_N02"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.origin}"



class ICF002(BaseModel):
    name = models.CharField("Nama", max_length=20)
    phone = models.CharField("Phone", max_length=20)
    SERVICE_LIST = (
    ('KO', 'Konsultasi (Mulai dari Rp 200.000)'),
    ('KA', 'Kawat Gigi (Mulai dari Rp 10.00.000)'),
    ('SC', 'Scaling Gigi (Mulai dari Rp 300.000)'),
    ('PE', 'Pemutihan Gigi (Mulai dari Rp 1.750.000)'),
    ('BE', 'Bedah Mulut (Mulai dari Rp 400.000)'),
    ('PE', 'Pembersihan Gigi (Mulai dari Rp 250.000)'),
    ('CA', 'Cabut Gigi (Mulai dari Rp 300.000)'),
    ('PE', 'Pemasangan Crown Gigi (Mulai dari Rp 2.500.000)'),
    ('GI', 'Gigi Palsu (Mulai dari Rp 1.000.000)'),
    ('VE', 'Veneer Gigi (Mulai dari Rp 800.000)'),
    ('TA', 'Tambal Gigi (Mulai dari Rp 350.000)'),
    ('IM', 'Implan Gigi (Mulai dari Rp 16.000.000)'),
    )
    service = models.CharField("Layanan",choices=SERVICE_LIST,max_length=5)
    date = models.DateField("date", auto_now=False, auto_now_add=False)
    time = models.TimeField("time", auto_now=False, auto_now_add=False)
    
    

    class Meta:
        verbose_name = "ICF002"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"

