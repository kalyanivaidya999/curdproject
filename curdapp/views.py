from django.shortcuts import render, redirect

from curdapp.models import datasheet


# Create your views here.
def home(request):
    ds = datasheet.objects.all()
    return render(request, "store/home.html", {'ds': ds})


def add_data(request):
    if request.method == "POST":
        emp1 = request.POST.get('callid')
        name1 = request.POST.get('callname')
        Email1 = request.POST.get('callemail')
        Salary1 = request.POST.get('callsalary')

        # create an object for model
        d = datasheet()
        d.emp_id = emp1
        d.name = name1
        d.email = Email1
        d.salary = Salary1
        d.save()
        return redirect("/home")
    return render(request, "store/add.html")


def del_data(request,emp_id):
    d=datasheet.objects.get(pk=emp_id)
    d.delete()
    return redirect('/home')

def edit_data(request,emp_id):
    dtl = datasheet.objects.get(pk=emp_id)
    return render(request, "store/update.html",{'dtl':dtl})


def do_edit_data(request, emp_id):
    # Retrieve the existing data object
    dtl = datasheet.objects.get(pk=emp_id)

    if request.method == "POST":
        emp2 = request.POST.get('callid')
        name2 = request.POST.get('callname')
        Email2 = request.POST.get('callemail')
        Salary2 = request.POST.get('callsalary')

        dtl.emp_id = emp2
        dtl.name = name2
        dtl.email = Email2
        dtl.salary = Salary2
        dtl.save()

        return redirect('/home')

    return render(request, "store/update.html", {'dtl': dtl})