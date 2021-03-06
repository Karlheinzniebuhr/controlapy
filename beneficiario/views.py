from django.utils import timezone
from .models import Beneficiario
from .models import Nangareko
from .models import Pytyvo
from .models import IPS
from .models import SET
from .models import SFP
from .models import MJ
from .models import Jubilado
from .models import Tekopora
from django.shortcuts import render, get_object_or_404
from .forms import BeneficiarioForm
from django.shortcuts import redirect


def list(request, cedula):
    beneficiarios = Beneficiario.objects.filter(cedula=cedula).order_by('cedula')
    return render(request, 'beneficiario/list.html', {'beneficiarios': beneficiarios})

def detail(request, cedula):
    nangareko = get_object_or_404(Nangareko, cedula=cedula)
    pytyvo = get_object_or_404(Pytyvo, cedula=cedula)
    return render(request, 'beneficiario/detail.html', {'nangareko': nangareko, 'pytyvo': pytyvo})

#def detail(request, cedula):
#    if request.method == "POST":
#        form = BeneficiarioForm(request.POST)
#        if form.is_valid():
#            print(form)
#            cedula = form.cedula
#            print (cedula)
#            beneficiario = get_object_or_404(Beneficiario, cedula=cedula)
#            print (beneficiario)
#            return redirect('beneficiario/detail.html', {'beneficiario': beneficiario})
#
#            return render(request, 'beneficiario/beneficiario_detail.html', {'beneficiario': beneficiario})
#    else:
#        form = BeneficiarioForm()
#    return render(request, 'beneficiario/buscar.html', {'form': form})


def buscar(request):
    if request.method == "POST":
        cedula = request.POST.get("cedula","")
        print(cedula)
        try:
            nangareko = Nangareko.objects.get(cedula=cedula)
        except Nangareko.DoesNotExist:
            nangareko = None
        try:
            pytyvo = Pytyvo.objects.get(cedula=cedula)
        except Pytyvo.DoesNotExist:
            pytyvo = None
        try:
            ips = IPS.objects.get(cedula=cedula)
        except IPS.DoesNotExist:
            ips = None
        try:
            set = SET.objects.get(cedula=cedula)
        except SET.DoesNotExist:
            set = None
        try:
            sfp = SFP.objects.get(cedula=cedula)
        except SFP.DoesNotExist:
            sfp = None
        try:
            mj = MJ.objects.get(cedula=cedula)
        except MJ.DoesNotExist:
            mj = None
        try:
            tekopora = Tekopora.objects.get(cedula=cedula)
        except Tekopora.DoesNotExist:
            tekopora = None
        try:
            jubilado = Jubilado.objects.get(cedula=cedula)
        except Jubilado.DoesNotExist:
            jubilado = None
        return render(request, 'beneficiario/detail.html', 
            {
                'nangareko': nangareko, 
                'pytyvo': pytyvo,
                'ips': ips, 
                'set': set,
                'sfp': sfp,
                'mj': mj,
                'tekopora': tekopora,
                'jubilado': jubilado
            })

#            return redirect('beneficiario/detail/', {'cedula': cedula})
#
#            return render(request, 'beneficiario/beneficiario_detail.html', {'beneficiario': beneficiario})
    else:
        form = BeneficiarioForm()
    return render(request, 'beneficiario/buscar.html', {'form': form})