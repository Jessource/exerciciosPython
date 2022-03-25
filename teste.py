bpm =int( input('Informe seu número de batimentos: ') )
idade = int(input("Informe sua idade:"))
resposta = "Abaixo da faixa"

if (idade >= 2 and idade < 8):
  resposta = "Não existe paramentro para sua idade"
else:
  if idade <= 2 and (bpm >= 120 and bpm <= 140):
    resposta = "Dentro faixa adequada"
  elif idade <= 2 and bpm > 140 :
    resposta = "Acima faixa adequada"

  if idade >= 8 and (bpm >= 80 and bpm <= 100):
    resposta = "Dentro faixa adequada"
  elif idade >= 8 and bpm > 100:
    resposta = "Acima faixa adequada"

print(resposta)