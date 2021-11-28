from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class LoginOrganiserRequiredMixin(AccessMixin):
    """Verify that the current user is and if he is an organiser authenticated."""
    def dispatch(self, request, *args, **kwargs):
        print(request.user.is_organisor)
        if not request.user.is_authenticated or not request.user.is_organisor:
            return redirect('leads:list_lead')
        return super().dispatch(request, *args, **kwargs)