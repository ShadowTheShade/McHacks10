from django import forms

class QuestionCheckForm(forms.Form):
    question_id = forms.IntegerField(required=True)
    option = forms.IntegerField(required=False)