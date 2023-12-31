from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.models import Teacher
from classroom.form import ContactForm

# Create your views here.
def home_view(request):
    return render(request,'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    # .save()
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")

class TeacherListView(ListView):
    # mode_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY
    # model_detail.html
    model = Teacher
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    # Share model_form.html
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # Form --> Confirm Delete Button
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL?
    success_url = reverse_lazy("classroom:thank_you")

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)