participantes = int(input("Digite o numeros de participantes:"))
playstation = 0
xbox =0
nitendo = 0
votantes =0

while (votantes < participantes):
  voto = int(input("Digite 1- playstation ou 2-xbox ou 3- nitendo: "))
  if(voto == 1):
    playstation = playstation + 1
  elif(voto == 2):
    xbox = xbox + 1
  elif(voto == 3):
    nitendo = nitendo + 1
  votantes = votantes + 1

print("playtation teve", playstation,"votos")
print("xbox teve", xbox,"votos")
print("nitendo teve",nitendo,"votos")

if playstation > xbox and playstation> nitendo:
  print("Playstation foi o console escolhido com o total de: {}".format(playstation))

elif xbox > playstation and xbox> nitendo:
  print("xbox foi o console escolhido com o total de: {}".format(xbox)) 
else:
  print("nitendo foi o console escolhido com o total de: {}".format(nitendo)) 


