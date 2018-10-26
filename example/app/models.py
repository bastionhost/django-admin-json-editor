from django.db import models
from jsonfield import JSONField


class SchemaModel(models.Model):
    data = JSONField()

    def __unicode__(self):
        base_name = '[{}]-[{}]-'.format(self.data['title'], self.data['type'])
        if self.data['type'] == 'object':
            base_name += '-'.join(self.data['properties'].keys())
        elif self.data['type'] == 'array':
            base_name += '-'.join(self.data['items']['properties'].keys())
        return base_name


class JSONModel(models.Model):
    schema = models.ForeignKey(SchemaModel, default=1)
    data = JSONField(null=True, blank=True)
