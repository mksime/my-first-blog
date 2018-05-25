from django import forms
from .models import Post
from tinymce import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
