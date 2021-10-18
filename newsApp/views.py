from django.shortcuts import render
# Create your views here.
def moviesInfo(request):
    my_dict={'head_msg':'Movies Information',
      'sub_msg1':'Sonali slowly getting cured',
      'sub_msg2':'Bahubali-3 is just planning',
      'sub_msg3':'Mazu has good looks',
      'photo':'images/lion.jpg'}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsInfo(request):
    my_dict={'head_msg':'Sports Information',
      'sub_msg1':'Manya done hokey season ',
      'sub_msg2':'she good at playing sports',
      'sub_msg3':'school Team  won and got 8 goals yesterday'}
    return render(request,'newsApp/news.html',context=my_dict)

def politicsInfo(request):
    my_dict={'head_msg':'Politics Information',
      'sub_msg1':'Rupee value rising against dollar',
      'sub_msg2':'current US president is Biden',
      'sub_msg3':'he is the oldest president in the history'}
    return render(request,'newsApp/news.html',context=my_dict)

def index(request):
    return render(request,'newsApp/index.html')
