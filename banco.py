#sistema bancário

#bibliotecas
import os
import time

#cores ansi
class colors:
    c = '\033[1;36m'
    w = '\033[1;97m'
    y = '\033[1;33m'
    e = '\033[0m'
    g = '\033[92m'
    r = '\033[91m'

#funções
def LimparTerm():
    os.system('cls' if os.name == 'nt' else 'clear')

def Depositar():
	print('\nQuanto você deseja depositar? \n')
	dep = float(input('Seu depósito: R$'))
	
	if dep > sum(Dinheiro_disponivel):
		print(colors.r + 'Dinheiro insuficiente' + colors.e)
	else:
		print(colors.g + f'R${dep} reais depositado com sucesso!' + colors.e)
		Dinheiro_guardado[0] += dep
		Dinheiro_disponivel[0] -= dep
	
def Retirar():
	ret = float(input('Quanto deseja retiirar? R$'))
	
	if ret > sum(Dinheiro_guardado):
		print(colors.r + 'Dinheiro insuficiente' + colors.e)
	else:
		Dinheiro_disponivel[0] +=ret
		Dinheiro_guardado[0] -= ret
		print(colors.g + 'Retirado com sucesso' + colors.e)
	
def Resgatar():
	res = float(input('\nQuanto deseja resgatar? R$'))
	print('\nSeu dinheiro foi resgatado!')
	Dinheiro_disponivel[0] += res
	
Dinheiro_guardado = [0.0]
Dinheiro_disponivel = [0.0]

print(colors.y + 'Seja bem-vindo(a) ao seu banco' + colors.e)
#sistema
while True:
	print(colors.g + f'\nSaldo atual: R${Dinheiro_disponivel[0]:.2f}' + colors.e)
	print('\nEscolha uma opção \n')
	print('[1] Depositar \n[2] Retirar \n[3] Ver meu saldo \n[4] Sair \n[5] ajuda')
	opc = input('\n>>> ')
	
	#estrutura condicional de ações
	if opc == '1':
		Depositar()
		
	elif opc == '2':
		Retirar()
		
	elif opc == '3':
		print(f'\nSeu saldo atual guardado é R${Dinheiro_guardado[0]:.2f}')
		
	elif opc == '4':
		print('\nFinalizando...')
		time.sleep(3)
		LimparTerm()
		exit()
	
	elif opc == '5':
		print('\n [1] resgatar dinheiro \n [2] sair \n')
		opc2 = input('>>> ')
		
		if opc2 == '1':
			Resgatar()
		
		if opc2 == '2':
			print('\nFinalizando...')
			time.sleep(3)
			LimparTerm()
			exit()
	else:
		print(colors.r + 'Opção inválida' + colors.e)
