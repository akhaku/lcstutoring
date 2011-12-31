from django.forms import ValidationError
from tutors.models import Tutor
from tmsutil.constants import YEAR_CHOICES
from tmsutil.forms import TmsModelForm

class TutorForm(TmsModelForm):
    _year_choices = [val[0] for val in YEAR_CHOICES]
    exclude = ('added_on', 'active',)

    class Meta:
        model = Tutor

    def clean_first_name(self):
        name = self.cleaned_data.get('first_name')
        return name.title()

    def clean_last_name(self):
        name = self.cleaned_data.get('last_name')
        return name.title()

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        phone = phone.lstrip()
        phone = phone.rstrip()
        phone = phone.replace('+','')
        phone = phone.replace('(','')
        phone = phone.replace(')','')
        phone = phone.replace('-','')
        phone = phone.replace(' ','')
        phone = phone.lstrip('1')
        if len(phone) != 10:
            raise ValidationError("Please enter a valid phone number")
        return phone

    def clean_grad_year(self):
        val = int(self.cleaned_data.get('grad_year'))
        if val < 2010 or val > 2030:
            raise ValidationError("Must be a valid graduation year eg: 2014")
        return val

    def clean_tutoring_preference_from(self):
        pref_from = int(self.cleaned_data.get('tutoring_preference_from'))
        if not pref_from in self._year_choices:
            raise ValidationError("Value %s invalid" % pref_from)
        return pref_from

    def clean_tutoring_preference_to(self):
        pref_to = int(self.cleaned_data.get('tutoring_preference_to'))
        if not pref_to in self._year_choices:
            raise ValidationError("Value %s invalid" % pref_to)
        pref_from = self.cleaned_data.get('tutoring_preference_from')
        if pref_to < pref_from:
            raise ValidationError("Please enter a valid tutoring preference")
        return pref_to

    def clean(self):
        ret = super(TutorForm, self).clean()
        return ret
