import traceback

from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Post
from app.util import FirstThread

def save_data(title, content):
    Post.objects.create(title=title, content=content)
    FirstThread().start()

@api_view(['POST'])
def create_post(request):
    try:
        title = request.data.get('title')
        content = request.data.get('content')
        save_data(title, content)
        return Response(status=201)
    except Exception:
        print(traceback.format_exc())
        return Response(status=409)