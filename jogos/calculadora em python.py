x = 1
while x == 1:
 escolheoperacao = input("Qual a operacao?[s]omar,[m]ultiplicar,[su]btrair ou [d]ividir:")

 #fazendo a conta
 def soma(soma1,soma2):
  print("o resultado é:")
  print(soma1 + soma2)

 def subtracao(subtracao1,subtracao2):
  print("o resultado é:")
  print(subtracao1 - subtracao2)

 def multiplicacao(multiplicacao1,multiplicacao2):
  print("o resultado é:")
  print(multiplicacao1 * multiplicacao2)
 def dividir(dividir1,dividir2):
  print("o resultado é:")
  print(dividir1 / dividir2)
 #

 # verificando a operacao
 if escolheoperacao == "s":
  valorsoma1 = input("Qual o primeira parcela?:") 
  valorsoma2 = input("Qual o segunda parcela?:")
  soma(int(valorsoma1),int(valorsoma2))

 if escolheoperacao == "su":
  valorsubtracao1 = input("Qual o primeira parcela?:") 
  valorsubtracao2 = input("Qual o segunda parcela?:")
  subtracao(int(valorsubtracao1),int(valorsubtracao2))

 if escolheoperacao == "m":
  valormultiplicao1 = input("Qual o primeira parcela?:")
  valormultiplicao2 = input("Qual o segunda parcela?:")
  multiplicacao(int(valormultiplicao1),int(valormultiplicao2))
 
 if escolheoperacao == "d":
  valordividir1 = input("Qual a primeira parcela?:")
  valordividir2 = input("Qual o segunda parcela?:")
  dividir(int(valordividir1),int(valordividir2))
 #
