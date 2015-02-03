from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms


# workaround for bug#1 - to enable MyUser adding in Admin site
# based on http://stackoverflow.com/questions/16953302/django-custom-user-model-in-admin-relation-auth-user-does-not-exist
class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            MyUser._default_manager.get(username=username)
        except MyUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = MyUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('avatar',)}),
    )


admin.site.register(MyUser, MyUserAdmin)