from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect
from .forms import StudentRegistraion, StudentAcadmics
from .models import Student_Info, Student_Acadmics
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# This is homepage
def home(request):
	return render(request, 'base.html')


# This is add new Student and show student
def add_student(request):
	if request.method == 'POST':
		show_form = StudentRegistraion(request.POST)
		if show_form.is_valid():
			show_form.save()
	else:
		show_form=StudentRegistraion()
	all_student = Student_Info.objects.all()
	return render(request, 'addstudent.html', {'form':show_form, 'all_student':all_student})

# This is Student Update 
def update_data(request, id):
	if request.method == 'POST':
		updates = Student_Info.objects.get(pk=id)
		show_form = StudentRegistraion(request.POST, instance=updates)
		if show_form.is_valid():
			show_form.save()
			return redirect('add_student')

	else:
		updates = Student_Info.objects.get(pk=id)
		show_form = StudentRegistraion(instance=updates)


	return render(request, 'update.html',{'form':show_form})


# This is Student Delete
def delete_data(request, id):
	if request.method=='POST':
		dele = Student_Info.objects.get(pk=id)
		dele.delete()
	return HttpResponseRedirect('/')
 

# Student Acadmics
def student_acadmics(request):
    all_academics = Student_Acadmics.objects.all()
    
    return render(request, 'Studenta.html', {'all_academics':all_academics})

def Student_Academics_update_data(request, id):
    if request.method == 'POST':
        updatesa = Student_Acadmics.objects.get(pk=id)
        up_form = StudentAcadmics(request.POST, instance=updatesa)
        if up_form.is_valid():
            up_form.save()
            return redirect('student_acadmics')

    else:
        updatesa = Student_Acadmics.objects.get(pk=id)
        up_form = StudentAcadmics(instance=updatesa)


    return render(request, 'Student_a_update.html',{'form':up_form})


# Authentication APIs
def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for erroeneous inputs
        # username should be under 10 charcters
        if len(username) >10:
            messages.error(request, "Username is too long.")
            return redirect('home')
        # Username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('home')
        # Password should match
        if pass1 != pass2:
            messages.error(request, "Password doesn't match.")
            return redirect('home')

        
        # Create the user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('add_student')

        else:
            messages.error(request, "Invalid Credentials, Please try again ")
            return redirect('home')

    return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
    return HttpResponse('handleLogout')

# search student
 
def search(request):
    query = request.GET['query']
   
    allStudentName = Student_Info.objects.filter(Name__icontains=query)
  
    params = {'allStudentName': allStudentName, 'query':query}
    return render(request, 'search.html', params)


# Change password of user

def change_password(request):
    if request.method == "POST":
        current = request.POST['cp']
        new = request.POST['np']
        confirm = request.POST['cnp']

        if new != confirm:
            messages.error(request, "Password doesn't match.")
        
        user = User.objects.get(id=request.user.id)
        check = user.check_password(current)
        if check==True:
            user.set_password(new)
            user.save()
            messages.success(request, "Password Changed Successfully !!!")
        else:
            messages.error(request, "Current Password doesn't match.")
    return render(request, 'change.html')