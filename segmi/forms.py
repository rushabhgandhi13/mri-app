from django import forms

from segmi.models import lab_report

class ReportForm(forms.ModelForm):
	class Meta:
		model = lab_report
		fields = '__all__'

class LabReportForm(forms.ModelForm):
	
    class Meta:
        model = lab_report
        fields = ['lab','patient','doctor','report_img','report_summary']