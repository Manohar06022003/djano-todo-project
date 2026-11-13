# from asyncio import tasks
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from .models import todo_User , Task
from .forms import signupform as todo_forms
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def login_view(request):
    if request.method == 'POST':
        email =request.POST.get('email')
        password = request.POST.get('password')

        user =authenticate(request, email=email, password = password)


        if user is not None:
            login(request, user)
            # return render(request, 'interface.html',{'user': user})
            return redirect('dashboard_views')
        else :

            error_message = "Invalid email or password.please try again."

            return render (request, 'login.html' ,{'error_message' : error_message})
    return render(request, 'login.html')
        
            
    return render(request, 'login.html')

def signup_view(request):

    if  request.method =='POST':
        form = todo_forms(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect ( 'login')
    else:
        form=todo_forms()
        
    return render(request, 'signup.html' ,{'form':form})

@login_required
def dashboard_view(request):

    tasks = Task.objects.filter(user=request.user)
    task_count=tasks.count()
    task_completed= tasks.filter(completed=True).count()
    task_pending = tasks.filter(completed=False).count()
    

    return render(request, 'interface.html',{'tasks': tasks,'task_count':task_count,
                                             'task_completed':task_completed,'task_pending':task_pending} )

def add_task_view(request):

    if request.method =='POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(user = request.user,title=title , description =description)
        task.save()
        

        if request.POST.get('action') == 'add_another' :
            return redirect('add_task')

        else:
            return redirect('dashboard_views')
    
    else:
        return render(request, 'add_task.html')

def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method =='POST':
        task.title= request.POST.get('title')
        task.description = request.POST.get('description')
        task.user=request.user
        # task.completed = request .POST.get('completed') =='off'
        task.save()

        return redirect('dashboard_views')
    return render(request, 'edit_task.html',{'task' :task})

def delete_task_view(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('dashboard_views')

@login_required
@require_POST
def toggle_task_completion_view(request, task_id):

    task = get_object_or_404(Task, id=task_id , user = request.user)
    task.completed =not task.completed
    task.save(update_fields=['completed'])
    next_page = request.POST.get('next')

    if next_page == 'completed_tasks':
        return redirect('completed_tasks')
    elif next_page == 'pending_tasks':
        return redirect('pending_tasks')
    return redirect('dashboard_views')

@login_required
def completed_task_view(request):
    completed_tasks = Task.objects.filter(user = request.user , completed = True)
    return render(request, 'completed_task.html',{'completed_tasks':completed_tasks,'completed_task_count':completed_tasks.count()})

@login_required
def pending_task_view(request):
    pending_tasks = Task.objects.filter(user = request.user , completed=False)
    return render(request,'pending_task.html',{'pending_tasks':pending_tasks,'pending_task_count': pending_tasks.count()})






