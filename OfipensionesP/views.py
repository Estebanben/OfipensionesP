from django .http  import HttpResponse

def home(request):
    return HttpResponse ("Hello world! Django views")
def healthCheck(request):
    return HttpResponse ('ok')