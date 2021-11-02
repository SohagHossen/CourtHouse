from django.shortcuts import render
from Ncase.models import New_case
from lower.models import Lower
# Create your views here.

def lower(reguest):
    return render(reguest,'lower.html')

def lower_view(request):
        lower_data = Lower.objects.all()
        lower_list = []
        for x in lower_data:
            name = x.lower_name
            id = x.lower_id
            case_roll = x.case_roll
            phone=x.phone
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
                "lower_name": name,
                "lower_id": id,
                "case_roll": case_roll,
                "phone": phone,
                "lower_cases": cases_list
            }
            lower_list.append(tem)

        context = {
            'lower': lower_list
        }

        return render(request, "lower.html", context=context)
