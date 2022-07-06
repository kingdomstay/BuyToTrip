from django.contrib import admin

from search.models import Country, City, Airport, Hotel, Tour


@admin.register(Country)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Airport)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class PersonAdmin(admin.ModelAdmin):
    pass
