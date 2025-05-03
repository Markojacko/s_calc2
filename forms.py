from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, IPAddress, NumberRange, Optional

class SubnetForm(FlaskForm):
    ip_address = StringField('IP Address', validators=[DataRequired(), IPAddress(ipv4=True, ipv6=True, message="Invalid IP address.")])
    cidr_mask  = IntegerField('CIDR Mask', validators=[DataRequired(), NumberRange(min=0, max=128, message="Enter a mask between 0 and 128.")])
    split_mask = IntegerField('Split into (CIDR)', validators=[Optional(), NumberRange(min=0, max=128, message="Enter a mask between 0 and 128.")])
    cloud_provider = SelectField('Terraform Template For', choices=[('aws','AWS'),('azure','Azure'),('gcp','GCP')], default='aws')
    submit = SubmitField('Calculate')
