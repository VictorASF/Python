import datetime

hora = datetime.time(9, 30, 25)
print(hora)
soma = datetime.timedelta(minutes=35)

hora = hora.replace(hour=15)
print('{}#{}#{}'.format(hora.hour, hora.minute, hora.second))
print(hora.strftime('%H#%M#%S'))
