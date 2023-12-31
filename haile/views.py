from django.shortcuts import render, redirect, get_object_or_404
from .models import Contract, Delier, Deal, Petroleum, Transport
from decimal import Decimal, InvalidOperation
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


def contract_form(request):
    if request.method == 'POST':
        form_data = request.POST.dict()
        form_data.pop('csrfmiddlewaretoken', None)
        contract = Contract(**form_data)
        contract.save()
        return redirect('contract_preview', contract_id=contract.id)

    return render(request, 'contract_form.html')


def contract_preview(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    return render(request, 'contract_preview.html', {'contract': contract})

def contract_print(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    contract.print_count += 1
    contract.save()
    return render(request, 'contract_print.html', {'contract': contract})


def home(request):
    return render(request, 'home.html')

def delier_form(request):
    if request.method == 'POST':
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken', None)
        delier = Delier(**data)
        delier.save()
        return redirect('delier_preview', delier_id=delier.id)
    return render(request, 'delier_form.html')

def delier_preview(request, delier_id):
    delier = get_object_or_404(Delier,  pk=delier_id)
    return render(request, 'delier_preview.html', {'delier': delier})

def delier_print(request, delier_id):
    delier = get_object_or_404(Delier, pk=delier_id)
    return render(request, 'delier_print.html', {'delier': delier})


def deal_form(request):
    if request.method == 'POST':
        com = request.POST.dict()
        com.pop('csrfmiddlewaretoken', None)
        deal = Deal(**com)
        deal.save()
        return redirect('deal_preview', deal_id=deal.id)
    return render(request, 'deal_form.html')

def deal_preview(request, deal_id):
    deal = get_object_or_404(Deal,  pk=deal_id)
    return render(request, 'deal_preview.html', {'deal': deal})

def deal_print(request, deal_id):
    deal = get_object_or_404(Deal, pk=deal_id)
    return render(request, 'deal_print.html', {'deal': deal})


def your_view(request):
    if request.method == 'POST':
        input_value = request.POST.get('amount_litter', '')

        # Remove commas and validate the input value
        value_without_commas = input_value.replace(",", "")

        try:
            # Convert the value to a decimal
            decimal_value = Decimal(value_without_commas)

            # Now you can use 'decimal_value' in your Django model or perform other operations
            # For example:
            # your_model_instance.amount_litter = decimal_value
            # your_model_instance.save()

        except InvalidOperation:
            # Handle the exception in case the conversion fails
            return HttpResponse("Invalid decimal value. Please provide a valid decimal number.", status=400)
        


def petroleum_form(request):
    if request.method == 'POST':
        petroleum = request.POST.dict()
        petroleum.pop('csrfmiddlewaretoken', None)
        petroleum = Petroleum(**petroleum)
        petroleum.save()
        return redirect('petroleum_preview', petroleum_id=petroleum.id)
    return render(request, 'petroleum_form.html')

def petroleum_preview(request, petroleum_id):
    petroleum = get_object_or_404(Petroleum,  pk=petroleum_id)
    return render(request, 'petroleum_preview.html', {'petroleum': petroleum})

def petroleum_print(request, petroleum_id):
    petroleum = get_object_or_404(Petroleum, pk=petroleum_id)
    return render(request, 'petroleum_print.html', {'petroleum': petroleum})




def transport_form(request):
    if request.method == 'POST':
        transport = request.POST.dict()
        transport.pop('csrfmiddlewaretoken', None)
        transport = Transport(**transport)
        transport.save()
        return redirect('transport_preview', transport_id=transport.id)
    return render(request, 'transport_form.html')

def transport_preview(request, transport_id):
    transport = get_object_or_404(Transport,  pk=transport_id)
    return render(request, 'transport_preview.html', {'transport': transport})




def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL, default to an empty string if not provided

    contracts = Contract.objects.all()  # Start with all contracts

    if query:
        # If a query is provided, filter contracts based on companyname or signed_date
        contracts = contracts.filter(
            Q(companyname__icontains=query) | Q(buyerrepre_signe_date__icontains=query)
        )

    paginator = Paginator(contracts, 10)  # Show 10 results per page
    page = request.GET.get('page')
    contracts = paginator.get_page(page)

    return render(request, 'search.html', {'contracts': contracts, 'query': query})