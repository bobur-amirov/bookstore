from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import RegisterForm, AccountEditForm
from account.models import Basket, Account
from book.models import Book
from comment.models import Like


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            messages.info(request, 'username yoki password xato!')
            return redirect('login_page')

    return render(request, 'account/login.html')


def logout_page(request):
    logout(request)
    return redirect('book_list')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'account/register.html', context)


def edit_account(request, username):
    account = get_object_or_404(Account, username=username)
    form = AccountEditForm(instance=account)
    if request.method == 'POST':
        form = AccountEditForm(request.POST, request.FILES, instance=account)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('basket_list')

    context = {
        'form': form,
    }

    return render(request, 'account/edit_account.html', context)



def basket(request, slug):
    user = request.user
    book = get_object_or_404(Book, slug=slug)
    try:
        basket = Basket.objects.get(user=user, book=book)
        if basket:
            return redirect('basket_list')
    except ObjectDoesNotExist:
        Basket(user=user, book=book, status=True).save()
        return redirect('basket_list')


def basket_list(request):
    user = request.user
    baskets = Basket.objects.filter(user=user)

    context = {
        'baskets': baskets
    }

    return render(request, 'account/basket_list.html', context)


def like_user_list(request):
    user = request.user
    likes = Like.objects.filter(user=user)

    context = {
        'likes': likes
    }

    return render(request, 'account/user_like_list.html', context)