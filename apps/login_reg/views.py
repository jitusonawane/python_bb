from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import User, Item, Wish
from django.contrib import messages

def logincheck(session):
    if 'user_id' not in session:
        return False
    return True    

def index(request):
    if logincheck(request.session):
        return redirect('/friends')
    else:
        return render(request, 'login_reg/index.html')

def register(request):
    errors  = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():            
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        print "here"
        rg = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = rg.id   
        return redirect('/friends')


def login(request):    
    errors  = User.objects.login_valiator(request.POST)
    if len(errors):              
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:        
        lg =  User.objects.get(email = request.POST['email'])
        request.session['user_id'] = lg.id
        return redirect('/friends')


def logout(request):
    del request.session['user_id']
    return redirect('/')
  

def friends(request):    
    if logincheck(request.session):
        
        # context ={
        #     'mainUser' : User.objects.get(id = request.session['id']),
        #     'all_users': User.objects.exclude(id = request.session['id']),
        #     'friends': User.objects.get(id = request.session['id']).friends.all()
        # }

        user=request.session['user_id']
        context={
            'items': Item.objects.exclude(wishers__wisher_id=user),
            'wishes': Wish.objects.filter(wisher_id=user),
            'all': Wish.objects.all()
        }
        return render(request, 'login_reg/friends.html')
    else:
        return redirect('/')
    

# def profile(request,frId):
#     if logincheck(request.session):
#         check = User.objects.checkUser(frId)
#         if check[0]:            
#             friend = User.objects.get(id=frId)
#             context = {
#                 'user': friend
#             }
#             return render(request,'login_reg/show.html',context)
#         else:
#             messages.error(request,check[1])
#             return redirect('/friends')
#     else:
#         return redirect('/')
        

# def add_friend(request,usId):
#     if logincheck(request.session):
#         if int(usId) != request.session['id']:
#             check = User.objects.checkUser(usId)
#             if check[0]:
#                 User.objects.get(id = request.session['id']).friends.add(User.objects.get(id=usId))
#             else:
#                 messages.error(request,check[1])
#         else:
#             messages.error(request,"You can't add yourself as a friend.")
#         return redirect('/friends')
#     else:
#         return redirect('/')

# def remove_friend(request,frId):
    # if logincheck(request.session):    
    #     if int(frId) != request.session['id']:            
    #         check = User.objects.checkUser(frId)
    #         if check[0]:
    #             User.objects.get(id =request.session['id']).friends.remove(User.objects.get(id=frId))
    #         else:
    #             messages.error(request, check[1])
    #     else:
    #         messages.error(request,"You can't delete yourslef as friend ")
    #     return redirect('/friends')
    # else:
    #     return redirect('/')
            
def add_item(request):
    if logincheck(request.session):
        if request.method == 'POST':
            wish=request.POST['wish_name']
            if len(wish)>3:
                items=Item.objects.create(title=wish, user_id=request.session['user_id'])
                Wish.objects.create(wish_id=items.id, wisher_id=request.session['user_id'])
                return redirect('/friends')
            else:
                    messages.add_message(request,messages.ERROR,'Iteam must be at least 3 characters')
                    return redirect('/add')
                

        return render(request,'login_reg/add.html')

def add_wish(request, wish_id):
    if logincheck(request.session):
        Wish.objects.create(wish_id=wish_id, wisher_id=request.session['user_id'])
    return redirect('/friends')

def remove_wish(request, wish_id):
    if logincheck(request.session):
      Wish.objects.get(wish_id=wish_id, wisher_id=request.session['user_id']).delete()
    return redirect('/friends')

def item(request, item_id):
    if logincheck(request.session):        
        context={
            'item': Item.objects.get(id=item_id),
            'wish': Wish.objects.filter(wish_id=item_id)
        }
    return render(request, 'login_reg/item.html', context)

def delete(request, item_id):
    if logincheck(request.session):
     Item.objects.get(id=item_id, user_id=request.session['user_id']).delete()
    return redirect('/friends')
