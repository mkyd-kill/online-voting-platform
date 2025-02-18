from django import forms
from .models import Vote, Candidate

class VoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        election = kwargs.pop('election', None)
        super().__init__(*args, **kwargs)

        if election is not None:
            self.fields['candidate'].queryset = Candidate.objects.filter(election=election)
        else:
            self.fields['candidate'].queryset = Candidate.objects.none()
        
    class Meta:
        model = Vote
        fields = ['candidate']