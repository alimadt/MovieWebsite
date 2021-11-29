from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from movie.celery import app

@app.task
def send_activation_code(email, activation_code):
    activation_url = f'http://localhost:5000/v1/api/user/activate/{activation_code}'
    message = f"""
        Thank you for signing up.
        Please, activate your account.
        Activation link: {activation_url}
    """

    send_mail(
        'Activate your account',
        message,
        'myblogadmin@gmail.com',
        [email],
        fail_silently=False
    )


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    reset_password_url = 'http://localhost:5000'+'{}?token={}'.format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        "Password Reset",
        reset_password_url,
        "noreply@somehost.local",
        [reset_password_token.user.email],
        fail_silently=False
    )
