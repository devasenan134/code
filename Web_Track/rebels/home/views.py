from django.shortcuts import render, HttpResponseRedirect

from .forms import FileForm
# Create your views here.

def index(request):

    if request.method == "GET":
        file_form = FileForm()
        return render(request, 'home/index.html', {
            'form': file_form
        })
    else:
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            #file1 = request.FILES['source_file']
            # return render(request, 'home/file.html', {
                # 'name': 'scores_pdf'
            # })
            return HttpResponseRedirect('home:index')

        return render(request, 'home/index.html', {
            'error': 'not_valid'
        })
