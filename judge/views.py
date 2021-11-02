from django.shortcuts import render,redirect
from Ncase.models import New_case
from judge.models import Judge




def judge(reguest):
     return render(reguest,'judge.html')

def judge_view(request):
        judge_data = Judge.objects.all()
        judge_list = []
        for x in judge_data:
            name = x.judge_name
            id = x.judge_id
            court_name = x.Court_name
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
                "judge_name": name,
                "judge_id": id,
                "court_name": court_name,
                "judge_cases": cases_list
            }
            judge_list.append(tem)

        context = {
            'judge': judge_list
        }

        return render(request, "judge.html", context=context)