from django.shortcuts import render
from Ncase.models import New_case
from police.models import Police
from Ncase import views
# Create your views here.

def police(reguest):
    return render(reguest,'police.html')

def police_view(request):
    police_data=Police.objects.all()
    police_list=[]
    for x in police_data:
        name = x.police_name
        id = x.police_id
        station = x.station_name
        post = x.post_name
        cases_list = []
        for case in x.case_id.all():
            case_id = case.case_id
            case_name = case.case_name
            temp = {
                "case_id": case_id,
                "case_name": case_name
            }
            cases_list.append(temp)
        print(cases_list)
        tem = {
            "police_name": name,
            "police_id": id,
            "police_station": station,
            "police_post": post,
            "police_cases": cases_list
        }
        police_list.append(tem)



    context={
        'police': police_list
    }

    return render(request,"police.html",context=context)