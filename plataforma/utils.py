from django.contrib.messages import constants
from django.contrib import messages
from .models import Pacientes



def pacientes_is_valid(request, nome, sexo, idade, email, telefone):
    if len(nome.strip()) == 0 or len(sexo.strip()) == 0 or len(idade.strip()) == 0 or len(email.strip()) == 0 or len(telefone.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return False
    
    if not idade.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite uma idade válida')
        return False

    pacientes = Pacientes.objects.filter(email=email)

    if pacientes.exists():
        messages.add_message(request, constants.ERROR, 'Já existe um paciente com esse E-mail')
        return False
    
    return True