some notes of views.py

else:
            User.objects.create_user(username=un, email=e, password=pwd1, is_staff=False)   #from here a user will create or he or she will signup from here & ...
            user = authenticate(user=un, password=pwd1)             #...as soon as the user signups, user automatically login too with the help of this line.
            login(request, user)            #'user' is a variable 'User' is an object.

def Account(request):
    if request.user.is_authenticated:   #this line is used, when a user which is already login and tries to go... 
                                        #...to login page again by pasting customer/account/ in url.
        return redirect('home')     #redirect k parameters m jo bhi pass hota hai wo kisi na kisi url se link hota hai.

#anytime you make a new table or new model on admin site, you have to run two commands.
#1. makemigrations
#2. migrate

notes of customer/views.py
def Home(request):
    cat = Category.objects.all()
    dish = Dish.objects.filter(avail = True)
    if request.user.is_anonymous:
#anonymous tells us ki koi aisa user toh cart nhi dekh rha jo login nhi hai