from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from movies_app.models import Movie
from movies_app.models import Actor
from movies_auth.models import Profile

admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class ActorInline(admin.StackedInline):
    model = Actor.movies.through


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        ActorInline,
    ]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
