from django.contrib import admin

from django_admin_json_editor import JSONEditorWidget

from .models import JSONModel, SchemaModel


def get_schema(id):
    return SchemaModel.objects.get(id=id).data


@admin.register(JSONModel)
class JSONModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'schema', 'data')
    search_fields = ('data',)
    list_filter = ('schema',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['schema', ]
        else:
            return []

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            schema_id = obj.schema.id
            schema = get_schema(schema_id)
        else:
            schema = {}
        widget = JSONEditorWidget(schema, False, True)
        form = super(JSONModelAdmin, self).get_form(request, obj, widgets={'data': widget}, **kwargs)
        return form


@admin.register(SchemaModel)
class SchemaModelAdmin(admin.ModelAdmin):
    search_fields = ('data',)
