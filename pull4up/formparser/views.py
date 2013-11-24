from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import FormUpload
from upload import FileParser

@login_required
def index(request):
    """
    The main view for the File Parser (requires an Authenticated User)
    """
    total = ' '
    if request.method == 'POST':
        if request.FILES:
            total = FileParser(request.FILES['upload_file'])
        else:
            total = 'Erro - Nenhum arquivo selecionado.'
    else:
        form = FormUpload()

    result = {'result' : total }
    return render_to_response('index.html', result, context_instance=RequestContext(request))