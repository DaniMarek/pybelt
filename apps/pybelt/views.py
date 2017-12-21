from django.shortcuts import render, redirect

def index(request):
	return render(request, 'pybelt/index.html')

def welcome(request):
	return render(request, 'pybelt/welcome.html')

def comments(request):
	return render(request, 'pybelt/compliments.html') 

def register(request):
	errors = User.objects.validate(request.POST)
	if len(errors):
		for field, message in errors.iteritems():
			error(request, message, extra_tags=field)
		return redirect('/users/new')

	User.objects.create(
		fname=request.POST['fname'],
		lname=request.POST['lname'],
		email=request.POST['email'],
		password=request.POST['password'],
	)
	return redirect('/welcome')


def home(request):
	return redirect(reverse('casa'))