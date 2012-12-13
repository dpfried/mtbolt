from django.contrib import admin
from tasks.models import DescriptionTask, DescriptionQuestion
from mtbolt.actions import export_as_csv_action

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = 'Approve selected decription tasks'

def reject(modeladmin, request, queryset):
    queryset.update(approved=False)
reject.short_description = 'Reject selected decription tasks'

def use(modeladmin, request, queryset):
    queryset.update(use_in_object_tasks=True)
use.short_description = 'Use selected description questions in object tasks'

def do_not_use(modeladmin, request, queryset):
    queryset.update(use_in_object_tasks=False)
do_not_use.short_description = 'Do not use selected description questions in object tasks'

class DescriptionTaskAdmin(admin.ModelAdmin):
    fields = ('completion_code', 'approved')
    readonly_fields = ('completion_code',)
    search_fields = ('completion_code',)
    list_display = ('completion_code', 'approved')
    list_filter = ('approved', 'created', 'modified')
    actions = [approve, reject]

class DescriptionQuestionAdmin(admin.ModelAdmin):
    list_display = ('scene', 'entity', 'object_description', 'location_description', 'answer', 'use_in_object_tasks',)
    list_filter = ('created', 'modified', 'scene', 'task')

    actions = [use, do_not_use, export_as_csv_action('Export to CSV', fields=list_display)]

    def task_approved(self, obj):
        return '%s'%(obj.task.approved)
    task_approved.short_description = 'Approved'

admin.site.register(DescriptionTask, DescriptionTaskAdmin)
admin.site.register(DescriptionQuestion, DescriptionQuestionAdmin)
