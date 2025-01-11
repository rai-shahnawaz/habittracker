from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, HabitViewSet, GoalViewSet, MilestoneViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'habits', HabitViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'milestones', MilestoneViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
