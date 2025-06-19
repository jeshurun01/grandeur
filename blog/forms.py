from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["full_name", "email", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                'class': "mt-1 block w-full rounded-md bg-white border-gray-300 shadow-sm focus:border-indigo-300 focus:ring-indigo-200 p-2",
                'placeholder': "Enter Your full Name..."
            }),
            "email": forms.EmailInput(attrs={
                'class': "mt-1 block w-full rounded-md bg-white border-gray-300 shadow-sm focus:border-indigo-300 focus:ring-indigo-200 p-2",
                'placeholder': "Enter Your Email..."
            }),
            "message": forms.Textarea(attrs={
                'class': "mt-1 block w-full rounded-md bg-white border-gray-300 shadow-sm focus:border-indigo-300 focus:ring-indigo-200 p-2",
                'placeholder': "Enter Your Message...",
                'rows': 4
            }),
        }
