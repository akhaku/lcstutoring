from django.forms import ValidationError
from tutees.models import Tutee
from tmsutil.constants import YEAR_CHOICES
from tmsutil.forms import TmsModelForm

class TuteeForm(TmsModelForm):
    _gender_choices = ['male', 'female']
    _year_choices = [val[0] for val in YEAR_CHOICES]

    class Meta:
        model = Tutee
        exclude = ('added_on', 'active',)

    def clean_cell_phone_number(self):
        phone = self.cleaned_data.get('cell_phone_number')
        if not phone:
            return phone
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
        return "%s-%s-%s" % (phone[0:3], phone[3:6], phone[6:10])

    def clean_home_phone_number(self):
        phone = self.cleaned_data.get('home_phone_number')
        if not phone:
            return phone
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
        return "%s-%s-%s" % (phone[0:3], phone[3:6], phone[6:10])

    def clean_parent_first_name(self):
        name = self.cleaned_data.get('parent_first_name')
        return name.title()

    def clean_parent_last_name(self):
        name = self.cleaned_data.get('parent_last_name')
        return name.title()

    def clean_child_first_name(self):
        name = self.cleaned_data.get('child_first_name')
        return name.title()

    def clean_child_last_name(self):
        name = self.cleaned_data.get('child_last_name')
        return name.title()

    def clean_gender(self):
        gender = str(self.cleaned_data.get('gender'))
        if not gender in self._gender_choices:
            raise ValidationError("Value %s invalid" % gender)
        return gender

    def clean_grade(self):
        grade = int(self.cleaned_data.get('grade'))
        if not grade in self._year_choices:
            raise ValidationError("Value %s invalid" % grade)
        return grade

    def clean(self):
        ret = super(TuteeForm, self).clean()
        if not self.cleaned_data.get('home_phone_number') and \
                not self.cleaned_data.get('cell_phone_number'):
            raise ValidationError("Please enter at least one valid phone number")
        return ret
