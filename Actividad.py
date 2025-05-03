import json

with open('Json_Actividad/cuartos_champions.json', 'r', encoding='utf-8') as file:
    partidos = json.load(file)

total_rojas = sum(partido["tarjetas_rojas"]["local"] + partido["tarjetas_rojas"]["visitante"] for partido in partidos)
print("Cantidad total de tarjetas rojas:", total_rojas)

clasificados = [partido["clasificado"] for partido in partidos]
print("Equipos clasificados a semifinales:")
for equipo in clasificados:
    print("-", equipo)
