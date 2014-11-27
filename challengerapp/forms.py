from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ChallengeForm(forms.Form):
	challenge_title = forms.CharField(
		label = 'Enter a title for your challenge:',
		max_length = 30,
		required = True, 
	)

	challenge_length = forms.IntegerField(
		label = 'Enter the number of days for the challenge:',
		required=True,
	)

	def __init__(self, *args, **kwargs):
		super(ChallengeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-exampleForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'makeChallenge'
		self.helper.add_input(Submit('submit', 'Submit'))