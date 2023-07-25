from django.shortcuts import render, redirect, get_object_or_404
from .models import Contract
from decimal import Decimal, InvalidOperation
from django.http import HttpResponse

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
    return render(request, 'contract_print.html', {'contract': contract})


def home(request):
    return render(request, 'home.html')

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