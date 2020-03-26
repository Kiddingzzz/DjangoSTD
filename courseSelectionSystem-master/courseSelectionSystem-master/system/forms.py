from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    attribute = (
        ('teacher', '教师'),
        ('student', '学生'),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    real_name = forms.CharField(label="真实姓名", max_length=128,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    id = forms.CharField(label="学号/工号", max_length=128,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    kind = forms.ChoiceField(label='用户类型', choices=attribute,)

class TeacherModifyForm(forms.Form):
    attribute = (
        ('teacher', '教师'),
    )
    username = forms.CharField(label="姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.CharField(label="性别", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zhengzhi = forms.CharField(label="政治面貌", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    joinTime = forms.CharField(label="参加工作时间", max_length=256,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    eduation = forms.CharField(label="受教育水平", max_length=256,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience = forms.CharField(label="工作经历", max_length=128,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    gonghaoid = forms.CharField(label="工号", max_length=128,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))