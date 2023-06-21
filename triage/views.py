from django.shortcuts import render
from .form import TriageForm
from .models import Triage
from .filters import TriageFilter
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
# Create your views here.


#checks if user is a station
def station_check(user):
    return user.groups.filter(name__in=['stations']).exists()

#checks if user is not a station

@login_required()
def home_view(request):
    name = request.user.get_full_name()
    return render(request, "index.html", {'name':name})

@login_required()
def add_triage(request):
    if station_check(request.user):

        context = {'isStation':True}

        # create object of form
        form = TriageForm(request.POST or None, request.FILES or None)

        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()

        context['form'] = form
        return render(request, "add_triage_form.html", context)

    else:
        raise PermissionDenied

@login_required()
def patients_list(request):

    patients_list= Triage.objects.all()
    patients_filter = TriageFilter(request.GET, queryset=patients_list)
    filter = TriageFilter()
    return render(request, "display_all_patients.html",{'patients_filter':patients_filter,'filter':filter})

@login_required()
def show_triage(request,pk):
    triage = get_object_or_404(Triage, id=pk)

    print(triage)
    return render(request, 'show_triage_details.html', {'triage': triage})

@login_required()
def search(request):
    if request.method == "POST":
        search = request.POST['search']
        querySet = Triage.objects.annotate(search_name=Concat('first_name', V(' '), 'last_name'))
        triages = querySet.filter(search_name__icontains=search)
        return render(request,'search.html',{'search':search,'triages':triages})

    else:
        return render(request, 'search.html',{})

def error_404(request, exception):
    return render(request, '404.html')