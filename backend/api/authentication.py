from rest_framework.authentication import TokenAuthentication, get_authorization_header
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework import exceptions
from rest_framework.settings import settings
from data.constants import constants
from utils.email import send_html_email
from api.models import citizen
from decouple import config


class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Token'

    def get_token_from_cookie(self, request):
        # Retrieve the token from the cookie
        token = request.COOKIES.get(settings.AUTH_COOKIE_NAME)
        if token:
            return token.encode('utf-8').split()
        return None

    def get_token(self, request):
        # First, try to get the token from the cookie
        token = self.get_token_from_cookie(request)
        if token:
            return token

        # If token is not found in the cookie, fall back to the header
        return get_authorization_header(request).split()

    def authenticate(self, request):
        auth = self.get_token(request)

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _(
                'Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        token = model.objects.select_related('user').get(key=key)
        if not token.user:
            raise exceptions.AuthenticationFailed(_('Unauthorized user'))
        if not token.user.is_verified:
            subject = f"{constants.APPLICATION_NAME} - Verify you email address"
            recipient_list = [token.user.email]
            res_citizen = citizen.Citizen.objects.filter(
                user=token.user).first()
            send_html_email(subject, "api/verification_email.html", {'application_name': constants.APPLICATION_NAME, 'citizen_name': res_citizen.f_name,
                            'verification_url': f"{config('API_BASE_URL')}/api/citizen/verify/{token.user.verification_token}"}, recipient_list)
            raise exceptions.AuthenticationFailed(
                _('You have not verified you email please verify you email from to you email address'))
        return super().authenticate_credentials(key)
