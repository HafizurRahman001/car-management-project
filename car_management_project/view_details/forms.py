from django import forms
from view_details.models import Comment,Purchase


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','comment']

        widgets = {
          'comment': forms.Textarea(attrs={'rows':4}),
        }


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude =['author','product']
        # fields = '__all__'