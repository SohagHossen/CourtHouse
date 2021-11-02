from django.shortcuts import render
from court.models import Court

# Create your views here.
def court_view(reguest):
    return render(reguest,'test.html')

def court_data(request):
        data = Court.objects.all()
        court_list = []
        for x in data:
            name = x.court_name
            address = x.address
            room_number = x.room_number
            timedate = x.datetime
            cases_list = []
            judge_list = []
            for case in x.case_id.all():
                case_id = case.case_id
                case_name = case.case_name
                temp = {
                    "case_id": case_id,
                    "case_name": case_name,
                }
                cases_list.append(temp)
                print(cases_list)
            for y in x.judge_id.all():
                judge_id = y.judge_id
                judge_name = y.judge_name
                temp1 = {
                    "judge_id": judge_id,
                    "judge_name": judge_name,
                }
                judge_list.append(temp1)
                print(judge_list)
            tem = {
                "court_name": name,
                "address": address,
                "room_number": room_number,
                "timedate": timedate,
                "cases_id ": cases_list,
                "judge_data": judge_list,
            }
            court_list.append(tem)
            print(court_list)

        context = {
            'court_details ': court_list
        }
        return render(request, "Court_Test.html", context=context)
