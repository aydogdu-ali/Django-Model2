from django.db import models

from django.contrib.auth.models import User # DEFAULT OLARAK GELEN USER MODELİNİ İMPORT ETTİK. 

class Profile(models.Model):
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True,null=True, upload_to='profile')
    user= models.OneToOneField(User, on_delete=models.CASCADE) #her bir kullanıcının bir profili olabileceğini belirtmiş oluruz.
    #on_delete parametresi silme işleminde nasıl davranacağını belirtiriz. CASCADE parametresi verildiğinde siler ve db de yer tutmaz.

    def __str__(self):
        return self.user.username



class Address(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # BURADA USER İLE ADRESİ EŞLEŞTİRME İŞLEMİ YAPTIK. YANİ İLİŞKİLENDİRDİK. BİRDEN FAZLA ADRESİ OLABİLİR.

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    user= models.ManyToManyField(User) # ürünlerle kullanıcıları ilişkilendirdik.

    def __str__(self):
        return self.name