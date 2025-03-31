import bisect

limites = [25, 50, 75, 100]
intervalo_valores = ["[0, 25]", "(25, 50]", "(50, 75]", "(75, 100]"]

inserir_valor =  float(input())

indice = bisect.bisect_right(limites, inserir_valor)

if 0 <= inserir_valor <= 100:
    print(f"Intervalo {intervalo_valores[indice]}")
else:
    print("Fora de intervalo")