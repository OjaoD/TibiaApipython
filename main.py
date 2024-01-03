import requests


resposta = requests.get("https://dev.tibiadata.com/v4/guild/Blood Moon Society")
resposta = resposta.json()

print(f"players online:{resposta['guild']['players_online']}\nplayers offline:{resposta['guild']['players_offline']}")
print(f"Membros total:{resposta['guild']['members_total']}")

#name = input("Insira o nome de um membro para buscar:")
minlevel = int(input("Level minimo:"))
reqVocacao = input("(Elder Druid, Elite Knight, Master Sorcerer)Vocacao:")

for membros in resposta['guild']['members']:
    if int(membros['level']) >= minlevel:
        if membros['vocation'] == reqVocacao:
            print(f"Nome:{membros['name']}, level:{membros['level']}, Vocacao:{membros['vocation']}, Status:{membros['status']}")



#with open('data.json', 'w') as fp:
#    json.dump(resposta, fp)