from uuid import uuid4

# Django Libraries
from django.db.models import Model, CharField, DateTimeField

class Example(Model):
    """
    Example object database model.
    """
    uuid         = CharField(max_length=128, default=str(uuid4()))
    created      = DateTimeField(auto_now_add=True)
    
    # Custom table metadata
    class Meta:
        db_table  = 'example'