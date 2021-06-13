from import_export import resources
from .models import Biodata


class BiodataResource(resources.ModelResource):

    class Meta:
        model = Biodata
        import_id_fields = ('nik',)
