from django.shortcuts import render,redirect
import pickle
import joblib
model2=joblib.load("C:/Users/savad/Desktop\strtup/savedmodel1/mod.joblib")
# with open("C:/Users/savad/Desktop/strtup/savedmodel1/model.pkl",'rb') as file:
#     model2=pickle.load(file)

def fun(Round):
    if Round=='has_roundA':
        d=1
    else:
        d=0
    return d
def func(Round):
    if Round=='has_roundB':
        d=1
    else:
        d=0
    return d
def funct(Round):
    if Round=='has_roundC':
        d=1
    else:
        d=0
    return d
def f(Round):
    if Round=='has_roundD':
        d=1
    else:
        d=0
    return d

def software(Company_Type):
    if Company_Type=='Software':
        d=1
    else:
        d=0
    return d
def web(Company_Type):
    if Company_Type=='web':
        d=1
    else:
        d=0
    return d
def mobile(Company_Type):
    if Company_Type=='mobile':
        d=1
    else:
        d=0
    return d
def enterprise(Company_Type):
    if Company_Type=='enterprise':
        d=1
    else:
        d=0
    return d
def advertising(Company_Type):
    if Company_Type=='advertising':
        d=1
    else:
        d=0
    return d
def games_video(Company_Type):
    if Company_Type=='games_video':
        d=1
    else:
        d=0
    return d
def semiconductor(Company_Type):
    if Company_Type=='semiconductor':
        d=1
    else:
        d=0
    return d    
def biotech(Company_Type):
    if Company_Type=='biotech':
        d=1
    else:
        d=0
    return d
def network_hosting(Company_Type):
    if Company_Type=='network_hosting':
        d=1
    else:
        d=0
    return d
def ecommerce(Company_Type):
    if Company_Type=='ecommerce':
        d=1
    else:
        d=0
    return d
def hardware(Company_Type):
    if Company_Type=='hardware':
        d=1
    else:
        d=0
    return d
def other_category(Company_Type):
    if Company_Type=='other_category':
        d=1
    else:
        d=0
    return d

def new(Has_VC):
    if Has_VC=='Yes':
        d=1
    else:
        d=0
    return d
def ne(Has_angel):
    if Has_angel=='Yes':
        d=1
    else:
        d=0
    return d
def news(Is_Top500):
    if Is_Top500=='Yes':
        d=1
    else:
        d=0
    return d









def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def prediction(request):
    if request.method=='POST':

        age_first_funding_year = request.POST['age_first_funding_year']
        age_last_funding_year = request.POST['age_last_funding_year']
        relationships = request.POST['relationships']
        funding_rounds = request.POST['funding_rounds']
        funding_total_usd = request.POST['funding_total_usd']
        milestones = request.POST['milestones']
        Has_VC = request.POST['Has_VC']
        Has_angel = request.POST['Has_angel']
        Round = request.POST['Round']
      
        avg_participants = request.POST['avg_participants']
        Is_Top500 = request.POST['Is_Top500']
        Company_Type = request.POST['Company_Type']
        list=[[age_first_funding_year, age_last_funding_year, relationships,
                                funding_rounds, funding_total_usd, milestones, new(Has_VC),
                                    ne(Has_angel),fun(Round),func(Round),funct(Round),f(Round),
                                avg_participants, news(Is_Top500), software(Company_Type), web(Company_Type), mobile(Company_Type),
                                     enterprise(Company_Type), advertising(Company_Type), games_video(Company_Type), semiconductor(Company_Type),
                                       biotech(Company_Type),network_hosting(Company_Type), ecommerce(Company_Type), 
                                       hardware(Company_Type), other_category(Company_Type)]]
        y_pred=model2.predict(list)
        if y_pred[0]==0:
            y_pred='not success'
        else:
            y_pred='success'
        return render(request,'result.html',{'result':y_pred})
    return render(request,'prediction.html')


def contact(request):
    return render(request,'contact.html')


# def forminfo(request):

    

    
    
    # return redirect('result',{'result':y_pred})
    





               
                  