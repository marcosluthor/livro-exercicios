pip install pyautogui#remover elemento da lista
#mostrar elementos  e mostrar ultimo elemento
#incluir elemento na lista
listar=str(input("qual nome quer incluir na lista ?"))
animais=str(input('Qual tipo de animal voce gosta? '))
nomes=['Ana','Carlos','Jamile','Fernando','Maria','Paulo']
nomes.append(listar)
nomes.remove('Carlos')
print('ana tambem gosta de {}.'.format(animais))
print('Já {} não gosta de {}, assim como {}.'.format(nomes[2],animais,nomes[3]))
print(nomes)
print(nomes[0:3])
print (nomes[1:4])
print(nomes[-1])