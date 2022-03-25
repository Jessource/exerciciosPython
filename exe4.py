
qtdViajantes = int (input('Informe a quantidade de viajantes: '))
if qtdViajantes <= 1:
  print ("Não existe paramentro de desconto para esse numero de viajantes: Desconto somente para acima de 2 viajantes")
else:
  valorBruto = float (input('Informe seu valor bruto do pacote: '))  
  categoria = input("informe sua categoria: ")

if categoria == "economica"and qtdViajantes == 2:
  desconto = valorBruto*0.02
  valorLiquido = valorBruto - desconto
  valorMedio = valorLiquido /2
  print("Valor Bruto: {} Valor liquido: {} Valor Médio: {}".format(valorBruto,valorLiquido,valorMedio))
elif categoria == "economica" and qtdViajantes == 3:
  desconto = valorBruto*0.03
  valorLiquido = valorBruto - desconto
  valorMedio = valorLiquido /3
  print("Valor Bruto: {} Valor liquido: {} Valor Médio: {}".format(valorBruto,valorLiquido,valorMedio))

elif categoria =="economica"and qtdViajantes >= 4:
  desconto = valorBruto*0.05
  valorLiquido = valorBruto - desconto
  valorMedio = valorLiquido /qtdViajantes
  print("Valor Bruto: {} Valor liquido: {} Valor Médio: {}".format(valorBruto,valorLiquido,valorMedio))

if categoria == "executiva"and qtdViajantes == 2:
  desconto = valorBruto*0.05
  valorLiquido = valorBruto - desconto
  valorMedio = valorLiquido /2
  print("Valor Bruto: {} Valor liquido: {} Valor Médio: {}".format(valorBruto,valorLiquido,valorMedio))
elif categoria == "executiva" and qtdViajantes == 3:
  desconto = valorBruto*0.07
  valorLiquido = valorBruto - desconto
  valorMedio = valorLiquido /3
  print("Valor Bruto: {} Valor liquido: {} Valor Médio: {}".format(valorBruto,valorLiquido,valorMedio))

elif categoria =="executiva"and qtdViajantes >= 4:
  desconto = valorBruto*0.08
  valorLiquido = valorBruto - desconto
  valorMedio = valorLiquido /qtdViajantes
  print("Valor Bruto: {} Valor liquido: {} Valor Médio: {}".format(valorBruto,valorLiquido,valorMedio))
   


  