# Prova2sistemadistribuidos

# Evidência 1

<img width="470" height="174" alt="image" src="https://github.com/user-attachments/assets/3716bc21-05ae-4b9a-801e-61669fe8f8cd" />

Problema A 

#Controle de concorrencia 
MAXIMO_SIMULTANEO = 2 - foi alterado de numero 3 para 2 

<img width="480" height="178" alt="image" src="https://github.com/user-attachments/assets/92687f04-cdda-4cbf-a766-5c4d15101246" />


# Replicação e Consistência 

Problema B 

def sincronizar():
    replica ["estoque"] = principal ["estoque"] - foi alterado de replica para principal 
    
<img width="461" height="174" alt="image" src="https://github.com/user-attachments/assets/c0b8f5f5-a085-4e5b-b970-c52f0efba4c3" />

# Tolerância a Falhas

Problema C 

if replica ["online"]: - foi alterado de principal para replica 

<img width="477" height="163" alt="image" src="https://github.com/user-attachments/assets/a2f6163b-21b2-455c-b88b-147005cde417" />

# Questões 
1-  O semáforo limita a quantidade de threads que podem ser executado simultaneamente e evitando sobrecarga 

2- E necessário caso o servidor principal caia entra a replica para o substituir mesmo estando desatualizada 

3-  Significa que caso tenha falhas o código ira continuar sendo executado, ela foi mostrada nesse codigo a traves da replica mesmo estando errado ele continua sendo executado   

4 -  Serve para que somente 1 threads pode ser modificado por vez assim evitando que ocorra erro de estoque 

5- depois porque tem que atualizar o valor de estoque 
1 Os pedidos são processados no servidor principal.
2 O estoque é alterado conforme os pedidos realizados 
3 Após essa atualização, a sincronização envia o novo valor para a réplica.
