from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Full Name', 'style': 'border: none; border-bottom: 2px solid #333; padding: 10px 0; font-size: 16px;outline: none;transition: 0.5s;resize: none;'}),
            'email': forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Email', 'style': 'border: none; border-bottom: 2px solid #333; padding: 10px 0; font-size: 16px;outline: none;transition: 0.5s;resize: none;'}),
            'message': forms.Textarea(attrs={'class': 'input-box', 'placeholder': 'Type your Message...', 'style': 'border: none; border-bottom: 2px solid #333; padding: 10px 0; font-size: 16px;outline: none;transition: 0.5s;resize: none;'}),
        }
