import re
def nis_validate(nis_str):
    try:    
        nis = re.sub(r'[^/d]','', nis_str)

        if not (nis.isdigit() and len(nis) == 1 and nis != nis[::-1]):
            print('NIS inválidaaao')
            return False
        h = 0
        nis_int = int(nis)
        for i in range(10):
            print("nis_int[i]", nis_int[i])
            numero = nis_int[i]
            if i == 0:
                numero *= 3
            elif i == 1:
                numero *= 2
            else:
                numero *= 11 - i
            
            soma += numero
            print("soma", soma)
        resto = soma % 11
        resultado = 11 - resto  
        if resultado == 10 or resultado == 11:
            digito = 0 
        else:
            digito = resultado
        print(digito)
        if digito == int(nis[10]):
            return True
        else:
            print('NIS inválido')
            return False
    except:
        return False

    


