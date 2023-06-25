from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='Email')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']
        conteudo = f'Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}'
        mail = EmailMessage(
        subject='E-mail enviado pelo sistema Django',
        body=conteudo,
        from_email='contato@seudominio.com.br',
        to=['contato@seudominio.com.br', ],
        headers={'Reply.To':email},
        )
        mail.send()