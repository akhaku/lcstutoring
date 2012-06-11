from django.forms import ValidationError
from match.models import Match
from tmsutil.forms import TmsModelForm
from tmsutil.constants import DAY_CHOICES
from tmsutil.timewidget import SelectTimeWidget

class MatchForm(TmsModelForm):
    
    _day_choices = [val[0] for val in DAY_CHOICES]
    class Meta:
        model = Match
        fields = ('time', 'day', 'note', 'location')
        widgets = {'time': SelectTimeWidget(minute_step=15, second_step=60,
            show_seconds=False) }

#     def clean_time(self):
#         return self.cleaned_data.get('time')

    def clean_day(self):
        day = int(self.cleaned_data.get('day'))
        if not day in self._day_choices:
            raise ValidationError("Value %s invalid" % day)
        return day

    def clean(self):
        ret = super(MatchForm, self).clean()
        print "DASDAD"
        print self.cleaned_data
        return ret
