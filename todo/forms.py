from django.contrib.auth.forms import UserCreationForm,User


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    def __init__(self,*args,**kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.help_text=None
            if name=="email":
                field.required=True
