from django.shortcuts import render
from .models import Agent
from .forms import AgentForm


def index(request):
    return render(request, "index.html")


def agentinfo(request):
    form = AgentForm()

    if request.method == "POST":
        form = AgentForm(request.POST)
        if form.is_valid():
            a = Agent()
            a.first_name = form.cleaned_data["first_name"]
            a.last_name = form.cleaned_data["last_name"]
            a.education = form.cleaned_data["education"]
            a.company_name = form.cleaned_data["company_name"]
            a.specialization = form.cleaned_data["specialization"]
            a.agent_notes = form.cleaned_data["agent_notes"]
            a.mobileNumber = form.cleaned_data["mobileNumber"]
            a.phoneNumber = form.cleaned_data["phoneNumber"]
            a.emailID = form.cleaned_data["emailID"]
            a.save()

        else:
            form = AgentForm()

    ag = Agent.objects.all()
    return render(request, "agentinfo.html", {"agentinfo": ag, "form": form})
