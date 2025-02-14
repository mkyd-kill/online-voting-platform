from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Election, Candidate, Vote
from .forms import VoteForm

@login_required
def vote(request, election_id):
    election = Election.objects.get(id=election_id)
    candidates = Candidate.objects.filter(election=election)

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            return redirect('results', election_id=election.id)
    else:
        form = VoteForm()
    return render(request, 'voting/vote.html', {'election': election, 'candidates': candidates, 'form': form})

def results(request, election_id):
    election = Election.objects.get(id=election_id)
    candidates = Candidate.objects.filter(election=election)
    votes = Vote.objects.filter(candidate__in=candidates)

    results_data = {}
    for candidate in candidates:
        results_data[candidate.name] = votes.filter(candidate=candidate).count()

    return render(request, 'voting/results.html', {'election': election, 'results_data': results_data})