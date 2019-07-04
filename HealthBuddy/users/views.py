from .models import Type
from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.views.generic import View
from .forms import UserForm, StffPatientRegForm, StudPatientRegForm
from django.views.generic import TemplateView
from Patient.models import Patient
from students.models import students


class Home(TemplateView):
    template_name = "users/base_home.html"

class Calc(TemplateView):
    template_name = "users/health_calc.html"

class Contact(TemplateView):
    template_name = "users/contact_us.html"

class Profile(TemplateView):
    template_name = "users/Profile.html"

#only for patient's registrations
class UserFormView(View):
    form_class = UserForm
    template_name = 'users/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            isStudent = form.cleaned_data['isStudent']
            
            if password1!=password2:
                return render(request, self.template_name, {'form': form})
            

            if request.user.is_authenticated:
                logout(request)

            #create user
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            #create type
            types = Type(
                user = user,
                types = 'pat',
            )
            types.save()
            user = authenticate(username=username, password=password2)
              
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if isStudent:
                        return redirect('/register/stud_patient')
                    else:
                        return redirect('/register/stff_patient/')
        return render(request, self.template_name, {'form': form})

class StffPatientRegFormView(View):
    form_class = StffPatientRegForm
    template_name = 'users/stff_pat_reg_form.html'

    def get(self, request):
        if not request.user.is_authenticated:
            error_message = 'you are not autnenticated!'
            return render(request, 'users/registration_form.html', {'error_message': error_message})
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.is_dependent = False
            p.designation = 'Student'
            s = students.objects.get(roll=p.rollNo)


        #can fill rest of the data with student search
            p.save()
            return render(request, 'users/patient_profile', {'patient': p})
        return render(request, self.template_name, {'form': form})

class StudPatientRegFormView(View):
    form_class = StudPatientRegForm
    template_name = 'users/stud_pat_reg_form.html'

    def get(self, request):
        if not request.user.is_authenticated:
            error_message = 'you are not autnenticated!'
            return render(request, 'users/registration_form.html', {'error_message': error_message})
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            s = students.objects.get(roll=p.rollNo)
            p.bloodGroup = s.blood_group
            p.ccUsername = s.username
            p.program = s.program
            p.department = s.dept
            p.hall = s.hall
            p.room = s.room
            p.gender = s.gender
            if s.hometown:
                p.hometown = s.hometown
            p.save()

            return render(request, 'users/patient_profile')
        return render(request, self.template_name, {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'users/base_home.html', {'error_message': 'logged out!'})

def login_user(request):
    baseHome = 'users/base_home.html'
    if request.user.is_authenticated:
        return render(request, baseHome, {'error_message': 'You are already logged in!'})
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, baseHome, {'error_message': 'Logged in!'})
                # if user.type.types == 'phr':
                #     return render(request, 'users/phr_index.html', {})
                # if user.type.types == 'rec':
                #     return render(request, 'users/rec_index.html', {})
                # if user.type.types == 'doc':
                #     return render(request, 'users/doc_index.html', {})
                # if user.type.types == 'pat':
                #     return render(request, 'users/pat_index.html', {})
            else:
                return render(request, baseHome, {'error_message': 'Your account has been disabled'})
        else:
            return render(request, baseHome, {'error_message': 'Invalid login'})
    return render(request, baseHome)
