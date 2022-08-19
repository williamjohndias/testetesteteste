#declaração de variáveis
x = 0

lista = []
x = len(lista)
#enquanto 1 for igual a 0 faça..
while True:
    #digitar um número inteiro e insere em x
    n = int(input('Digite um número: [ %s ]: ' % x))

    #se o número digitado for igual ou menor que 0 escreva..
    if x == 4:
      print('fim da lista')
      #para a aplicação
      break
    #senão
    else:
      #adiciona mais um item à lista e adiciona mais um valor a x
      lista.append(n)
      x += 1



print("MENU")
print("1 – Busca em tabela melhorado\n2 – Busca com sentinela\n3 – Pesquisa do Maior  OU  Menor elemento de uma tabela\n4 – Pesquisa do Maior E  Menor elemento de uma tabela\n5 – Determinação da Moda de uma tabela.")

print("Digite 0 para sair")

menu = int(input("escolha uma opção: "))

while True:
  if menu == 1:
    menu0 = int(input("Busca em tabela melhorado: "))
    continue
    
  elif menu == 2:
    menu1 = int(input("Busca com sentinela: "))
    break
    
  elif menu == 3:
    menu2 = int(input("1 = Maior\n2 = Menor\nEscolha: "))
    maiormenor()
    
  elif menu == 4:
    print('O maior valor é:', max(lista))
    print('O menor valor é:', min(lista))
    break
    
  elif menu == 5:
    moda = statistics.mode(listaItens)
    print("A moda é: ", moda)
    continue
    
def maiormenor():
  if menu2 == 1
  print('O maior valor é: ', max(lista))
    
