from django.db import models


class Student(models.Model):
    first_name= models.CharField(max_length=30)# chardfield data tipidir.max_length= parametresi zorunludur.
    last_name = models.CharField(max_length=40)
    number = models.PositiveIntegerField(blank=True) # pozitif ve 32767 ye kadar gider.
    about = models.TextField(blank=True) # blank=True olursa boş bırakılabilir.
    email= models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="Student") # Student tablosuna ait ımageler "upload_to=Student" parametresi ile media klasörünün altında Student adlı bir klasör oluşur ve student toplasında yüklenen tüm ımageler burada tutulur.
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.number} {self.first_name} {self.last_name}"
        # bunu admin panelinde modelimizde verilerin istediğimiz gibi adlandırılmasını sağlar.

    class Meta:
        ordering = ("-number",) # büyükten küçüğe sıralar.
        verbose_name = "Öğrenci" # tabloda tekil isimleri ifade ederiz.
        verbose_name_plural ="Öğrenciler" #tabloda çoğul kısmı ifade ederiz.
         