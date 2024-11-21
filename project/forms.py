from django import forms
from . models import Note

class NoteForm(forms.ModelForm):
	notes = forms.ModelChoiceField(queryset=Note.objects.all(), initial=0),

	class Meta:
		model = Note
		fields = ['subject', 'note', 'completed']