from django.http import JsonResponse

# Create your views here.
from django.views import View

from addcelery.task_1 import CourseTask


class Do(View):
    def get(self, request):
        print("start")
        # CourseTask.delay()
        CourseTask.apply_async(args=('name',), kwargs={'name': '书剑', 'age': 22, 'sex': '男'}, queue='work_queue')
        print("end")
        return JsonResponse({'result': 'ok'})
