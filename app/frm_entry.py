from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
   nilai_1=StringField("Nilai 1", validators=[DataRequired()])
   nilai_2=StringField("Nilai 2", validators=[DataRequired()])
   operatornya=SelectField(choices=[('',"Pilih Operator"),('*','x'),('+','+'),('-','-'),('/','/')])
   submit=SubmitField("Proses")

class EditForm(FlaskForm):
   nilai_1=StringField("Nilai 1", validators=[DataRequired()])
   nilai_2=StringField("Nilai 2", validators=[DataRequired()])
   operatornya=SelectField(choices=[('*','x'),('+','+'),('-','-'),('/','/')])
   submit=SubmitField("Proses")   




