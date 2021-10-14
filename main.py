from __future__ import annotations
from random import shuffle

# Cargar prelista
with open("prelista.csv", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
lineas = [line.strip().split(",") for line in lineas]


cargos: dict[str, list[int]] = {}
for i, linea in enumerate(lineas):
    for cargo in linea:
        cargo_limpio = cargo.strip()
        if cargo_limpio not in cargos:
            cargos[cargo_limpio] = [i]
        cargos[cargo_limpio].append(i)

cargos_sin_ganador: dict[str, int] = {}
for _ in range(1_000_000):
    ya_escogidos = []
    cargos_a_escoger = list(cargos.keys())
    shuffle(cargos_a_escoger)
    for cargo in cargos_a_escoger:
        shuffle(cargos[cargo])
        for candidato in cargos[cargo]:
            if candidato not in ya_escogidos:
                ya_escogidos.append(candidato)
                break
        else:
            if cargo not in cargos_sin_ganador:
                cargos_sin_ganador[cargo] = 1
            else:
                cargos_sin_ganador[cargo] += 1

print("Se quedaron sin cargo:")
for cargo, veces in cargos_sin_ganador.items():
    print(f"{cargo}: {veces} veces.")
