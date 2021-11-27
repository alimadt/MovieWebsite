from django.core.mail import send_mail


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


def send_welcome_email(email):
    message = f'You were successfully registered at MyBlog! Thanks for the interest in our site!'
    send_mail(
        'Registration at MyBlog',
        message,
        'myblogadmin@gmail.com',
        [email],
        fail_silently=False
        )