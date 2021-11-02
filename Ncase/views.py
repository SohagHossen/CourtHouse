from django.contrib.auth.models import User
from django.shortcuts import render
from Ncase.models import New_case
from django.contrib import messages
def ncase(reguest):
     if reguest.method == 'POST':
            case_id = reguest.POST['case_id']
            case_name = reguest.POST['case_name']
            prose_name = reguest.POST['prose_name']
            def_name = reguest.POST['def_name']
            case_date = reguest.POST['case_date']
            new_case = New_case(case_id=case_id,case_name=case_name,prose_name=prose_name,def_name=def_name,case_date=case_date)
            new_case.save();
            messages.info(reguest, 'Your case is accepet')
            print("save the data ")


     return render(reguest, 'Ncase.html')
def case_view(request):
        case_data = New_case.objects.all()



        context ={
            'case_details':case_data
        }


        return render(request,"view.html",context=context)

def search_case(request):
    q=request.POST['q']
    case_data =New_case.objects.filter(case_id__int=q)
    for data in case_data :
        case_id =data.case_id
        case_name =data.case_name
        pro_name=data.prose_name
        def_name =data.def_name
        case_data=data.case_date
        context={
            'case_id ':case_id,
            'case_name':case_name,
            'pro_name':pro_name,
            'def_name':def_name,
            'case_date':case_data
        }
        return render(request, "view.html", context=context)
