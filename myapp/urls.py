from django.urls import path
from .import views
urlpatterns = [
    path('/',views.HomeView.as_view(),name='home'),
    path('',views.HomeView.as_view(),name='home'),
    path('paper/',views.PaperView.as_view(),name='paper'),
    path('notes/',views.NotesView.as_view(),name='notes'),
    path('syllabus/',views.SyllabusView.as_view(),name='syllabus'),
    path('timetable/',views.TimetableView.as_view(),name='timetable'),
]
