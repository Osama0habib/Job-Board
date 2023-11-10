from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializable import JobSerializable
from rest_framework import generics


@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all();
    data = JobSerializable(jobs ,many = True).data
    return Response({'data' : data})

@api_view(['GET'])
def job_details_api(request,id):
    job = Job.objects.get(id = id)
    data = JobSerializable(job).data
    return Response({'data' : data})

class Jobs(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializable

class JobDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializable
    lookup_field = 'id'
