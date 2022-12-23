from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image

# Create your views here.


def scan(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"scan.html",{"obj":obj})
    else:
          form=ImageForm()
          img=Image.objects.all()
    return render(request,"scan.html",{"img":img,"form":form})





# class ScanView(FormView):
    #form_class = ScanForm
  #  template_name = 'scan.html'
    #success_url = '/scan'

  #  def post(self, request: HttpRequest, *args: str, **kwargs: str):
       # image = request.FILES.get('image')
        #return super().post(request, *args, **kwargs)
