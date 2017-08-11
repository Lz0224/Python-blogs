#coding=utf-8
from myapp.models import Book,Author
from django import forms

TOPIC_CHOICES = (
    ('leve1','好评'),
    ('leve2','中评'),
    ('leve3','差评'),
)

class RemarkForm(forms.Form):
    subject = forms.CharField(max_length = 100,label = '标题' )
    mail = forms.EmailField(label = '邮件')
    topic = forms.ChoiceField(choices = TOPIC_CHOICES, label = '评价')
    message = forms.CharField(label = '内容',widget = forms.Textarea)
    cc_myself = forms.BooleanField(required = False,label = '订阅')

class BookForm(forms.ModelForm):
    class Meta:              #元类
        model = Book
        fields = ('title','publication_date','publisher')
        labels = {
            'title':'书名',
        }
