from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Profil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profil') # user.profil 
    bio = models.CharField(blank=True, max_length=250,null=True)
    city = models.CharField(blank=True, max_length=250,null=True)
    photo = models.ImageField(blank=True,null=True,upload_to='profil_photos/%Y/%m')
    
    class Meta:
        verbose_name = 'Profil'  # Modelin insan tarafından okunabilir adı
        verbose_name_plural = 'Profiller'  # Çoğul insan tarafından okunabilir adı
    
    
    def __str__(self):
        return f"{self.user.username}"
    
    
    def save(self,*args, **kwargs):
        ## IMAGE RESIZE
        super().save(*args,**kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            output_size = (600,600)
            img.thumbnail(output_size)
            img.save(self.photo.path)
            
    

class ProfilSituation(models.Model):
    user_profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sitiua_msg = models.CharField(max_length=240)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return str(self.user_profil)