from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import WishlistSerializer
from .models import WishlistItem
from rest_framework.decorators import api_view
from .models import MoodEntry
from rest_framework.decorators import permission_classes
from .serializers import MoodSerializer

class WishlistAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    items = WishlistItem.objects.filter(user=request.user)
    return Response(WishlistSerializer(items, many=True).data)

  def post(self, request):
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_wishlist_item(request, pk):
  item = get_object_or_404(WishlistItem, pk=pk, user=request.user)
  item.delete()
  return Response(status=204)

# Create your views here.
class MoodAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    moods = MoodEntry.objects.filter(user=request.user).order_by('-date')
    return Response(MoodSerializer(moods, many=True).data)

  def post(self, request):
    serializer = MoodSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_habits(request):
    habits = Habit.objects.filter(user=request.user)
    return Response(HabitSerializer(habits, many=True).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_habit(request):
    serializer = HabitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class HabitAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = HabitLog.objects.filter(habit__user=request.user)
        return Response(HabitLogSerializer(logs, many=True).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return Response(TaskSerializer(tasks, many=True).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class TaskAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return Response(TaskSerializer(tasks, many=True).data)
