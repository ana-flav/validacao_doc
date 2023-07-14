
def cpf_validate(cpf):
    ''' Função para validar CPF, usando o algoritmo de validação de CPF em que os dois últimos dígitos são dígitos verificadores.'''
    
    try:
        cpf = re.sub(r'[^\d]', '', cpf)

        if not (cpf.isdigit() and len(cpf) == 11 and cpf != cpf[::-1]):
            print('CPF inválido')
            return False

        # Checar primeiro dígito verificador
        soma = 0
        numero = 0;
        for i in range(9):
            numero = int(cpf[i])    
            valor = numero * (10 - i)
            soma += valor
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto

        # Checar segundo dígito verificador
        soma = 0
        numero = 0;
        for i in range(10):
            numero = int(cpf[i])
            valor = numero * (11 - i)
            soma += valor
        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto
        if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
            return True
        else:
            print('CPF inválido')
            return False

    except:
        print('Erro na validação do CPF')
        return False


        

  
        
   
 #TODO: Verificar FUNÇÃO PARA VALIDAR NIS

