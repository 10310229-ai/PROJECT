from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AboutVideoStore,AboutImageStore
from .models import ServiceStore
from .models import NewsImageStore,NewsVideoStore
from .models import SlideStore
from .models import TouristImageStore,TouristVideoStore
from .models import DocumentStore


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

# ABOUT INFORMATION
class AboutImageForm(forms.ModelForm):
    class Meta:
        model = AboutImageStore
        fields = ['about_image','title']

class AboutVideoForm(forms.ModelForm):
    class Meta:
        model = AboutVideoStore
        fields = ['about_video','title']

class AboutVideoRename(forms.ModelForm):
    class Meta:
        model = AboutVideoStore
        fields = ['title']

class AboutImageRename(forms.ModelForm):
    class Meta:
        model = AboutImageStore
        fields = ['title']

# SERVICE INFORMATION
class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceStore
        fields = ['text']

class ServiceRename(forms.ModelForm):
    class Meta:
        model = ServiceStore
        fields = ['text']

# NEWS INFORMATION
class NewsImageForm(forms.ModelForm):
    class Meta:
        model = NewsImageStore
        fields = ['news_image','title']

class NewsVideoForm(forms.ModelForm):
    class Meta:
        model = NewsVideoStore
        fields = ['news_video','title']

class NewsVideoRename(forms.ModelForm):
    class Meta:
        model = NewsVideoStore
        fields = ['title']

class NewsImageRename(forms.ModelForm):
    class Meta:
        model = NewsImageStore
        fields = ['title']



# SLIDE FORM INFORMATION
class SlideForm(forms.ModelForm):
    class Meta:
        model = SlideStore
        fields = ['slide_image','title']

class SlideRename(forms.ModelForm):
    class Meta:
        model = SlideStore
        fields = ['title']


# TOURIST INFORMATION
class TouristImageForm(forms.ModelForm):
    class Meta:
        model = TouristImageStore
        fields = ['tourist_image','title']

class TouristVideoForm(forms.ModelForm):
    class Meta:
        model = TouristVideoStore
        fields = ['tourist_video','title']

class TouristVideoRename(forms.ModelForm):
    class Meta:
        model = TouristVideoStore
        fields = ['title']

class TouristImageRename(forms.ModelForm):
    class Meta:
        model = TouristImageStore
        fields = ['title']


#DOCUMENT
class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentStore
        fields = ['document_upload','title']

class DocumentRename(forms.ModelForm):
    model = DocumentStore
    fields = ['title']