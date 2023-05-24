from rest_framework.authentication import TokenAuthentication, get_authorization_header
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework import exceptions


class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Token'

    def get_token_from_cookie(self, request):
        # Retrieve the token from the cookie
        token = request.COOKIES.get('auth')
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
