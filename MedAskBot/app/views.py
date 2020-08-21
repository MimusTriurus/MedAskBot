from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from app.botScenaries.Scenario import Scenario

import json

def home( request ) :
    assert isinstance( request, HttpRequest )
    return render(
        request,
        'app/index.html'
    )

@csrf_exempt
def receive( request ) :
    sc = Scenario( )
    htmlData = sc.getHtmlData( request.POST[ 'step' ] )
    return HttpResponse( json.dumps( htmlData ), content_type="application/json" )
