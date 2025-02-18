from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Election, Candidate, Vote
from .forms import VoteForm

@login_required
def elections(request):
    return render(request, "voting/elections.html")

@login_required
def vote(request, election_id):
    election = Election.objects.filter(id=election_id).first()

    if not election:
        return render(request, 'voting/error.html', {'message': 'Election Not Found'})

    # check if user has already voted
    if Vote.objects.filter(user=request.user, candidate__election=election).exists():
        return render(request, 'voting/already_voted.html')

    if request.method == 'POST':
        form = VoteForm(request.POST, election=election)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            return redirect('results', election_id=election.id)
    else:
        form = VoteForm(election=election)

    return render(request, 'voting/vote.html', {'election': election, 'form': form})

def results(request, election_id):
    election = Election.objects.get(id=election_id)
    candidates = Candidate.objects.filter(election=election)
    votes = Vote.objects.filter(candidate__in=candidates)

    results_data = {}
    for candidate in candidates:
        results_data[candidate.name] = votes.filter(candidate=candidate).count()

    return render(request, 'voting/results.html', {'election': election, 'results_data': results_data})