# from django import forms

# class PersonalityQtnForm(forms.Form):
#     def __init__(self, questions, *args, **kwargs):
#         super(PersonalityQtnForm, self).__init__(*args, **kwargs)

#         for idx, question in enumerate(questions):
#             self.fields[f"question_{idx}"] = forms.ChoiceField(
#                 label=question,
#                 choices=[("yes", "YES"),("No","no")],
#                 widget=forms.RadioSelect(),
#             )
