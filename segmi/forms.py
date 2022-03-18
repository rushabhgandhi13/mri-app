from django import forms

from segmi.models import lab_report

class ReportForm(forms.ModelForm):
	class Meta:
		model = lab_report
		fields = '__all__'