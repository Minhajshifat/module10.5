from django.shortcuts import render
def home(request):
    a={'name':'rahim','id':21,'class':'firsts class','list':[1,2,3,4],'empty':"",
       
     "people":[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
],'info':"I Am Shifat",
'time':'10:30:00.000123+02:00',
       
       
       
       
       }
    return render(request,'home.html', a)