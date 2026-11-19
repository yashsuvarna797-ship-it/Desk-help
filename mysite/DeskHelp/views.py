from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import forms
from django.contrib.auth.views import LoginView, PasswordResetDoneView, PasswordResetConfirmView,PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic.edit import FormView, UpdateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

def home_view(request):
    if request.user.is_authenticated:
        ticket_list = models.Ticket.objects.filter(owner=request.user)

        return render(request,
                    "DeskHelp/index.html",
                    {'ticket_list':ticket_list})
    else:
        return  render(request,
                    "DeskHelp/index.html")

def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
        else:
            return HttpResponse("Invalid")
        return redirect('login')
    else:
        form = forms.SignUpForm()
        return render(request, 'DeskHelp/registration/signup.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'DeskHelp/registration/login.html'
    next_page = reverse_lazy('home')

class MyPasswordChangeView(PasswordChangeView): 
    form_class = forms.MyPasswordChangeForm
    template_name = 'DeskHelp/registration/password_change_form.html'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'DeskHelp/registration/password_change_done.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'DeskHelp/registration/password_reset_form.html'
    form_class = forms.MyPasswordResetForm
    success_url = reverse_lazy('password_reset_done')   

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'DeskHelp/registration/password_reset_done.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = forms.MyResetPasswordForm
    template_name = 'DeskHelp/registration/password_reset_confirm.html' 
    success_url = reverse_lazy('login')

class CreateTicketView(LoginRequiredMixin,FormView):
    form_class = forms.TicketForm
    template_name = 'DeskHelp/ticket/create_ticket_form.html' 
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.owner = self.request.user
        ticket.save()

        return super().form_valid(form)

@login_required
def display_tickets_view(request):
    ticket_list = models.Ticket.objects.filter(owner=request.user)
    ticket_count = ticket_list.count()
    ticket_resolve = ticket_list.filter(status="RESOLVED").count()
    ticket_open = ticket_list.filter(status="OPEN").count()


    status = request.GET.get('status')
    time = request.GET.get('time')

    if status:
        ticket_list = ticket_list.filter(status=status)
        ticket_count = ticket_list.count()
        ticket_resolve = ticket_list.filter(status="RESOLVED").count()
        ticket_open = ticket_list.filter(status="OPEN").count()

    if time == 'latest':
        ticket_list = ticket_list.order_by('-datetime')

    if time == 'oldest':
        ticket_list = ticket_list.order_by('datetime')



    return render(request, 
                'DeskHelp/ticket/display_tickets.html', 
                {'ticket_list':ticket_list,
                 'ticket_count':ticket_count,
                 'ticket_resolve':ticket_resolve,
                 'ticket_open':ticket_open})

@login_required
def display_ticket_info_view(request, pk):
    ticket = get_object_or_404(models.Ticket, id=pk)
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)

        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.owner = request.user
            form.ticket = ticket
            form.save()
            return redirect('display_ticket_info', pk=pk)
    else:
        comment_form_new = forms.CommentForm()
    comments_list = models.Comment.objects.filter(ticket=ticket)

    return render(request, 
                'DeskHelp/ticket/display_ticket_info.html',
                {'ticket':ticket,
                'comments_list':comments_list,
                'comment_form':comment_form_new})

@login_required
def delete_ticket_view(request, pk):
    ticket = models.Ticket.objects.filter(id=pk).first().delete()
    return redirect('display_tickets')

class UpdateTicketView(UpdateView):
    model = models.Ticket
    fields = ['title', 'description', 'category']
    template_name = 'DeskHelp/ticket/update_ticket_form.html' 
    success_url = reverse_lazy('display_tickets')

    def get_queryset(self):
        return models.Ticket.objects.filter(owner=self.request.user)  

@login_required
def profile_view(request):
    if request.method == "POST":
        pass
    else:
        user = request.user
        return render(request, 'DeskHelp/profile.html', {'user': user})  