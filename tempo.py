segundos = int(input())
horas = segundos // 3600
minutos = segundos % 3600 // 60
resto = segundos % 60
print(f'{horas}h, {minutos}min, {resto}s')