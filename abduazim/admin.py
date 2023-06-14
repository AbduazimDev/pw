from django.contrib import admin
from .models import About, Comment, ClientLogo, Education, Experince, Portfolio, Skills, Category, Service, Blog


admin.site.register(Blog)

admin.site.register(About)
admin.site.register(Service)
admin.site.register(Comment)
admin.site.register(ClientLogo)
admin.site.register(Education)
admin.site.register(Experince)
admin.site.register(Portfolio)
admin.site.register(Skills)
admin.site.register(Category)
