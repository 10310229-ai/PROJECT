from django.db import models
from django.contrib.auth.models import User

class AboutImageStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about_image = models.ImageField(upload_to='ABOUT_IMAGE/')
    upload_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

    class Meta:
        ordering =['-upload_at']



class AboutVideoStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about_video = models.FileField(upload_to='ABOUT_VIDEO/')
    upload_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['-upload_at']

class ServiceStore(models.Model):
    text = models.TextField(max_length=1000)
    upload_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['-upload_at']


class NewsImageStore(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    news_image = models.ImageField(upload_to='NEWS_IMAGES')
    title = models.CharField(max_length=1000)
    show_in_recent = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    class Meta:
        ordering = ['-upload_at']


class NewsVideoStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    news_video = models.FileField(upload_to='NEWS_VIDEOS/')
    title = models.CharField(max_length=1000)
    show_in_recent = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    class Meta:
        ordering = ['-upload_at']



# SLIDE STORAGE INFORMATION
class SlideStore(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    slide_image = models.ImageField(upload_to='SLIDE IMAGE')
    upload_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['-upload_at']

# DOCUMENT INFORMATION
class DocumentStore(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    document_upload = models.FileField(upload_to='document/')
    upload_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.user
    class Meta:
        ordering = ['-upload_at']


# TOURIST INFORMATION
class TouristImageStore(models.Model):
    tourist_image = models.ImageField(upload_to='TOURIST IMAGE/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['-upload_at']


class TouristVideoStore(models.Model):
    tourist_video = models.FileField(upload_to='TOURIST VIDEO/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['-upload_at']