from .models import Post, PostTag, PostComment, Portfolio, User, WorkExperience, VolunteerExperience
from django import forms
from djrichtextfield.widgets import RichTextWidget


class SignUpForm(forms.ModelForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                               'class': 'form-control',
                                                                               'required': True, 'type': 'text',
                                                                               'style': 'height:50px;'}))
    email = forms.EmailField(label='username',
                    widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control',
                                                  'required': True, 'type': 'email', 'style': 'height:50px;'}))
    first_name = forms.CharField(label='first_name',
                    widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control',
                                                  'required': True, 'type': 'text', 'style': 'height:50px;'}))
    last_name = forms.CharField(label='last_name',
                    widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control',
                                                  'required': True, 'type': 'text', 'style': 'height:50px;'}))
    password = forms.CharField(label='password',
                               widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control',
                                                             'required': True, 'type': 'password',
                                                             'style': 'height:50px;'}))
    confirm_password = forms.CharField(label='confirm_password',
                               widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control',
                                                             'required': True, 'type': 'password',
                                                             'style': 'height:50px;'}))

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            'confirm_password',
        )


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='username',
                    widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control',
                                                  'required': True, 'type': 'text', 'style': 'height:50px;'}))
    password = forms.CharField(label='password',
                    widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control',
                                                  'required': True, 'type': 'password', 'style': 'height:50px;'}))

    class Meta:
        model = User
        fields = ['username','password',]


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('name', 'email', 'body')


class ConfessionForm(forms.ModelForm):
    title = forms.CharField(label='title',
                               widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control',
                                                             'required': True, 'type': 'text',
                                                             'style': 'height:50px;'}))
    content = forms.CharField(label='content',
                               widget=forms.Textarea(attrs={'placeholder': 'Content', 'class': 'form-control',
                                                             'required': True, 'type': 'text', 'rows': 20}))


    class Meta:
        model = Post
        fields = ('title', 'content', 'post_image', 'tag')


class PortfolioForm(forms.ModelForm):
    title = forms.CharField(label='title',
                            widget=forms.TextInput(attrs={'placeholder': 'Position', 'class': 'form-control',
                                                          'required': True, 'type': 'text',
                                                          'style': 'height:50px;'}))
    biography = forms.CharField(label='biography',
                              widget=forms.Textarea(attrs={'placeholder': 'Biography', 'class': 'form-control',
                                                           'required': True, 'type': 'text'}))
    phone_number = forms.CharField(label='phone_number',
                            widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control',
                                                          'required': True, 'type': 'text',
                                                          'style': 'height:50px;'}))
    address = forms.CharField(label='address',
                                   widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control',
                                                                 'required': True, 'type': 'text',
                                                                 'style': 'height:50px;'}))
    class Meta:
        model = Portfolio
        fields = (
            "title",
            "biography",
            "phone_number",
            "address",
            "portfolio_image"
        )


class WorkExperienceForm(forms.ModelForm):
    description = forms.CharField(label='description',
                                widget=forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control',
                                                             'required': True, 'type': 'text'}))
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'accordian-date-picker'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'accordian-date-picker'}))

    class Meta:
        model = WorkExperience
        fields = (
            "description",
            "start_date",
            "end_date"
        )


class VolunteerExperienceForm(forms.ModelForm):
    description = forms.CharField(label='description',
                                  widget=forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control',
                                                               'required': True, 'type': 'text'}))
    start_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'accordian-date-picker'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'accordian-date-picker'}))

    class Meta:
        model = VolunteerExperience
        fields = (
            "description",
            "start_date",
            "end_date"
        )
