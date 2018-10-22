from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse,HttpResponse
from django.core import serializers

from portfolio.models import *
from portfolio.forms import *

###############
# 本体
###############
class Portfolio(TemplateView):
    template_name = "portfolio.html"

    def get(self, request, *args, **kwargs):
        context = super(Portfolio, self).get_context_data(**kwargs)

        context['form'] = PortfolioForm()

        itemHeaders = get_list_or_404(MenuItemHeader)
        context['itemHeaders'] = itemHeaders

        items = get_list_or_404(MenuItem)
        context['items'] = items

        return render(self.request, self.template_name, context)

def loginPortfolio(request):
    password = request.POST.get('password')
    users = get_list_or_404(User, password=password)
    
    return render(request, "portfolio.html", {'result' : 'success'})

###############
# ポートフォリオ
###############
class Portfolio_Page(TemplateView):
    template_name = "portfolio_page.html"

    def get(self, request, *args, **kwargs):
        context = super(Portfolio_Page, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)        

class Portfolio_Page_Sub(TemplateView):
    template_name = "portfolio_page_sub.html"

    def get(self, request, *args, **kwargs):
        context = super(Portfolio_Page_Sub, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)        

##############
# カレンダー
##############
class Calender(TemplateView):
    template_name = "calender.html"

    def get(self, request, *args, **kwargs):

        context = super(Calender, self).get_context_data(**kwargs)

        context['form'] = CalenderForm()

        return render(self.request, self.template_name, context)

def getSchedule(request):
    import datetime
    import calendar

    year = request.GET.get('year')
    month = request.GET.get('month')

    today = datetime.date.today()
    if year is None:
        year = today.year
    if month is None:
        month = today.month

    _, lastday = calendar.monthrange(year,month)

    querySet = Schedule.objects.filter(start_date__lte=datetime.date(year,month,lastday), end_date__gte=datetime.date(year,month,1))
    if len(querySet) == 0:
        return HttpResponse(status=204)
    else:
        data = serializers.serialize('json', querySet)
        return HttpResponse(data, content_type="application/json")
 

def saveSchedule(request):
    pk = request.POST.get('pk')

    obj = Schedule(
        start_date=request.POST.get('startDate'),
        end_date=request.POST.get('endDate'),
        content=request.POST.get('content')
    )
    if len(pk) == 0:
        pass
    else:
        obj.pk = request.POST.get('pk')

    obj.save()
    
    return JsonResponse({})

def deleteSchedule(request):
    pk = request.POST.get('pk')
    Schedule(pk=pk).delete()

    return JsonResponse({})

class Calender_Sub(TemplateView):
    template_name = "calender_sub.html"

    def get(self, request, *args, **kwargs):
        context = super(Calender_Sub, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)           

###########
# Excel作成ツール
###########
class ExCreater(TemplateView):
    template_name = "excreater.html"

    def get(self, request, *args, **kwargs):
        context = super(ExCreater, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)

##########
# 自己紹介
##########
class About(TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        context = super(About, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)

class About_Sub(TemplateView):
    template_name = "about_sub.html"

    def get(self, request, *args, **kwargs):
        context = super(About_Sub, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)        

##########
# スキル
##########
class Skills(TemplateView):
    template_name = "skills.html"

    def get(self, request, *args, **kwargs):
        context = super(Skills, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)    

class Skills_Sub(TemplateView):
    template_name = "skills_sub.html"

    def get(self, request, *args, **kwargs):
        context = super(Skills_Sub, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)         

##########
# ツール
##########
class Tools(TemplateView):
    template_name = "tools.html"

    def get(self, request, *args, **kwargs):
        context = super(Tools, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)    
           