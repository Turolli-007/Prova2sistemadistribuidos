import threading
import time


#Servidores Simulados 
principal = {
    "online" : True,
    "estoque" : 10
}

replica = {
    "online" : True,
    "estoque" : 10

}

#Controle de concorrencia 
MAXIMO_SIMULTANEO = 2

semaforo = threading.Semaphore (MAXIMO_SIMULTANEO)
trava = threading.Lock()

pedidos_confirmados = []

def processar_pedidos(numero):
    with semaforo:
        time.sleep(0.1)

        with trava :
            if principal["estoque"] > 0:
                principal ["estoque"] -= 1
                pedidos_confirmados.append(numero)

def sincronizar():
    replica ["estoque"] = principal ["estoque"]


def consultar_estoque():
    if principal["online"]:
        return(
            "PRINCIPAL",
            principal ["estoque"]
        )
    if replica ["online"]:
        return(
            "REPLICA",
            replica["estoque"]
        )
    return "INDISPONIVEL", None

print ("=== CENTRAL DE PEDIDOS ===")

print(
    "Limite simultaneo:",
    MAXIMO_SIMULTANEO
)

print(
    "Estoque Inicial:",
    principal ["estoque"]
)

trabalhadores = [
    threading.Thread(
        target=processar_pedidos,
        args=(numero,)
    )
    for numero in [101,102,103]
]
for trabalhador in trabalhadores:
    trabalhador.start()

for trabalhador in trabalhadores:
    trabalhador.join()

print(
    "Pedidos confirmados:",
    sorted(pedidos_confirmados)

)

print(
    "Estoque principal:",
    principal["estoque"]
)

print(
    "Replica antes:",
    replica["estoque"]
)

sincronizar()

print(
    "replica depois:",
    replica["estoque"]
)
#simulaçao de falha

principal["online"] = False

nome, estoque = consultar_estoque()

print(
    "Consultar apos falha:",
    nome,
    estoque
)
