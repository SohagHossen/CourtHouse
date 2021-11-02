from django.shortcuts import render
from case.models import Status

def case(reguest):
    return render(reguest,'index.html')

def case_status(request):
            status_data = Status.objects.all()
            case_list =[]
            for x in status_data:
                case_id= x.case_id
                status = x.status
                temp={
                    "case_id" : case_id,
                    "status" :status,
                }
                case_list.append(temp)
            context = {
                'case_details':case_list,


            }

            return render(request, "status.html", context=context)
