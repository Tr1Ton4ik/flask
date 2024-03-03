from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    team_leader = IntegerField("Team Leader ID")
    work_size = IntegerField('Work Size')
    collaborators = TextAreaField('Collaborators')
    is_finished = BooleanField('Is Job Finished')
    add = SubmitField('Add')
