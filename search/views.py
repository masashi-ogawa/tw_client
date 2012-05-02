# Create your views here.
from django.http import HttpResponse

import twitter
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def search(request):
    user_name = request.POST.get("user_name", "python")

    api = twitter.Api()
#    statuses = api.GetPublicTimeline()
    statuses = api.GetUserTimeline(user_name)

    timelines = []
    for s in statuses:
        print s
        print 1
        if s.text[0] != '@':
            data = {}
            data["name"] = s.user.screen_name
            data["tweet"] = s.text
            data["created_at"] = s.created_at
            timelines.append(data)

    ctxt = RequestContext(request,{
            "search_value": user_name,
            "timelines": timelines,
            })
    return render_to_response('search.html', ctxt)
