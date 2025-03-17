from services.espacos import get_all

def validate_nome(nome):
    if nome == "":
        return "O campo 'Nome' é obrigatório"
    
def validate_codigo(codigo, exclude_codigo=None):
    if codigo == "":
        return "O campo 'Código' é obrigatório"
    
    for espaco in get_all():
        if espaco["codigo"] == exclude_codigo:
            continue
        
        if espaco["codigo"] == codigo:
            return "Código já cadastrado"
    
