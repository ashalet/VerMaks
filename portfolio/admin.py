from django.contrib import admin

# Register your models here.
from portfolio.models import Assets, Render, Work
#
#
# class RenderImageAdmin(admin.ModelAdmin):
#     pass
#
#
# class RenderImageInline(admin.StackedInline):
#     model = Render
#     max_num = 10
#     extra = 0
#
#
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [RenderImageInline,]
#
# admin.site.register(Render, RenderImageAdmin)
# admin.site.register(Render, ProductAdmin)



admin.site.register(Assets)
admin.site.register(Work)
admin.site.register(Render)
