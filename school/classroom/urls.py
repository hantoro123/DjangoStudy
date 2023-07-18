from django.urls import path
from .views import HomeView, ThankYouView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView

app_name = 'classroom'
# domain.com/classroom
urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name="contact"),
    path('create_teacher/', TeacherCreateView.as_view(), name="create_teacher"),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher'),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
]
