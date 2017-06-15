from django.http import HttpResponse
from django.shortcuts import render

def list_projects(request):

    return render(request, 
                  'listeditor/project_list.html', 
                  { 'message' : 'Project List', 
                    'item_list' : [ ('GGStreamer', 'Live-stream app for video games'),
                                    ('HamsterGO', 'Track hamsters in real-time via Maps'),
                                    ('StartupGen', 'Generate (simple) ideas for startups')],
                  })

def list_tasks(request):

    pass
