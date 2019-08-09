from django.shortcuts import render
import os
import csv
from app.settings import BASE_DIR

def inflation_view(request):
    template_name = 'inflation.html'

    path = os.path.join(BASE_DIR, 'inflation_russia.csv')
    inflation_list = []

    with open(path) as file:
        readed_file = csv.reader(file, delimiter=';')
        for line in readed_file:
            line_list = []
            for cell in line:
                if cell:
                    line_list.append(cell)
                else:
                    line_list.append('-')
            inflation_list.append(line_list)

    context = {
        'table_header': inflation_list[0],
        'table_body': inflation_list[1:]
    }

    return render(request, template_name,
                  context)