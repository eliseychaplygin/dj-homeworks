from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    form = CalcForm(request.GET)

    if form.is_valid():
        common_result = form.cleaned_data['initial_fee'] + form.cleaned_data['initial_fee'] * (form.cleaned_data['rate'] / 100)
        result = common_result / form.cleaned_data['months_count']
        context = {
            'form': form,
            'common_result': common_result,
            'result': result
        }
        return render(request, template, context)
    else:
        context = {
            'form': form
        }
        return render(request, template, context)
