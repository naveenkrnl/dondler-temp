from django.contrib import admin
from .models import Subject,Unit,Topic,UnitParts,Related,TopicResources,UnitResources,SubjectResources
# Register your models here.


admin.site.register(Subject)
admin.site.register(UnitParts)
admin.site.register(Unit)
admin.site.register(Topic)
admin.site.register(TopicResources)
admin.site.register(Related)
# admin.site.register(TopicUser)

# admin.site.register(UnitUser)
admin.site.register(UnitResources)
# admin.site.register(SubjectUser)
admin.site.register(SubjectResources)
