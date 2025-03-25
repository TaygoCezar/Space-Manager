# def validar_datas(datah_inicio: str, datah_fim: str) -> bool:  
#     """ Verifica se a data e hora de fim é maior do que 30 minutos da data e hora do inicio. 
    
#     Args: 
#         datah_inicio (str): data e hora de inicio no formato YYYY-MM-DD hh:mm
#         datah_fim (str): data e hora de fim no formato YYYY-MM-DD hh:mm
    
#     """
#     data_inicio, horario_inicio = datah_inicio.split() 
#     ano_inicio, mes_inicio, dia_inicio = map(int, data_inicio.split("-")) 
#     hora_inicio, minuto_inicio = map(int, horario_inicio.split(":"))

#     data_fim, horario_fim = datah_fim.split() 
#     ano_fim, mes_fim, dia_fim = map(int, data_fim.split("-")) 
#     hora_fim, minuto_fim = map(int, horario_fim.split(":")) 
    
#     if(ano_fim > ano_inicio and minuto_fim >= 30 + minuto_inicio): 
#         return True 
#     if(mes_fim > mes_inicio and minuto_fim >= 30 + minuto_inicio): 
#         return True
#     if(dia_fim > dia_inicio and minuto_fim >= 30 + minuto_inicio): 
#         return True
#     if(hora_fim > hora_inicio and minuto_fim >= 30 + minuto_inicio): 
#         return True

