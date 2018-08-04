from django.shortcuts import render_to_response,HttpResponse

def search_form(request):
    return render_to_response('polls/index.html')
	
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
