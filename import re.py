import re
from collections import Counter


with open('apache_logs.txt', 'r', encoding='utf-8') as file:
    log_data = file.read()

buscador_regex = re.compile(
    r"(Chrome|Firefox|Safari|Opera|Edg|MSIE|Trident|Brave|Vivaldi|SamsungBrowser)[/\s]?\d*\.?\d*",
    re.IGNORECASE
)
encontrar_buscador = buscador_regex.findall(log_data)


normalized_buscadores = [b.capitalize() for b in encontrar_buscador]


conteo_buscadores = Counter(normalized_buscadores)

print("Tipo de buscadores encontrados en los logs:")
for browser, count in conteo_buscadores.most_common():
    print(f"{browser}: {count} veces")