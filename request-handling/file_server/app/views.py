from _datetime import datetime
import os
from app.settings import FILES_PATH
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    context = {
        'files': [],
        'date': date
    }
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files_list = os.listdir(FILES_PATH)

    for file in files_list:
        file_path = os.path.join(FILES_PATH, file)
        file_metadata = os.stat(file_path)
        # print(f'ТУТ!!!!!! : {file_metadata}')

        time_create_file = datetime.fromtimestamp(file_metadata.st_ctime)
        time_change_file = datetime.fromtimestamp(file_metadata.st_mtime)

        file_info = {
            'name': file,
            'ctime': time_create_file,
            'mtime': time_change_file
        }

        if date:
            if file_info['ctime'].date() == datetime.strptime(date, '%Y-%m-%d').date():
                context['files'].append(file_info)
        else:
            context['files'].append(file_info)

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = os.path.join(FILES_PATH,name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            file_contents = file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_contents}
    )