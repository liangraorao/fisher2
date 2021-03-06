from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='长度在1-30个字符之间')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

