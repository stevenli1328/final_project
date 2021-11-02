from django.shortcuts import render
from django.http import HttpResponse



def payroll(request):
    #create new payroll form (for now just a list of employees)
    if request.method=='POST':
        pass
        #take given data from form
        #grab list of payroll objects associated with given employee
        #redirect to view page to see list of these objects
    else:
        pass
        #send form to template
    return render(request, 'payroll/payroll.html')

def other(request):
    return HttpResponse("Bad Page!")