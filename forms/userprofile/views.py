from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Feedbackform
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Review
# Create your views here.
class feedbackform(View):
    def get(self,request):
        form = Feedbackform()
        return render(request, "userprofile/feedback.html", {"form":form})
    def post(self,request):
        form =Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thankyou")
        return render(request,"userprofile/feedback.html", {"form":form  })
        
 
# def thanku(request):
#     return render(request,'userprofile/thank_you.html')

class thanku(TemplateView):
    template_name = "userprofile/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Messgae"] = "somthing Here" 
        context["hello"] = "hello" 
        context["threee"] = "hi" 
        return context
    
class feedbacklistView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "userprofile/feedbacklist.html"