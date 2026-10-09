from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import CustomUserCreationForm, CustomUserUpdateForm


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш каталог'
        message = 'Добро пожаловать в наш учебный проект! Вы успешно зарегистрировались на демонстрационном сайте. Все функции носят ознакомительный характер. Спасибо за участие в тестировании!'
        from_email = 'maxbatsmanov@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    def form_invalid(self, form):
        print("ОШИБКИ ФОРМЫ:", form.errors)
        return super().form_invalid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserUpdateForm
    template_name = "users/profile_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        return self.request.user