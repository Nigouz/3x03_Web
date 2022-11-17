from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import InputRequired, Length, ValidationError

class CourseForm(FlaskForm):
    search = StringField('search', validators=[InputRequired(),Length(max=100)])
    submit = SubmitField(label=("search"))

    def validate_search(self,search):
        excluded_chars = "*@?!'^+%&/()=}][{$#"
        for char in search:
            if char in excluded_chars:
                print("yes")
                #raise ValidationError(f"Character {char} not allowed")
                return False
        return True
                