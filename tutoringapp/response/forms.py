from response.models import Response
from tmsutil.forms import TmsModelForm

class ResponseForm(TmsModelForm):
    class Meta:
        model = Response
        exclude = ('created_by', 'last_updated',)
