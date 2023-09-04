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

#depositar
def Depositar():
	print('\nQuanto você deseja depositar? \n')
	print(f'Dinheiro disponível para depósito:', colors.g + f'R$ {Dinheiro_disponivel[0]:.2f}' + colors.e)
	dep = float(input('Seu depósito: R$'))
	
	if dep > sum(Dinheiro_disponivel):
		print(colors.r + 'Dinheiro insuficiente' + colors.e)
		
	elif dep <= 0:
		print(colors.r + '\nImpossivel depositar 0 reais ou menos' + colors.e)
		
	else:
		print(colors.g + f'R$ {dep} reais depositado com sucesso!' + colors.e)
		Dinheiro_guardado[0] += dep
		Dinheiro_disponivel[0] -= dep
		Transacoes.append(('Depósito', dep))

#sacar
def Retirar():
	print(f'\nDinheiro disponível para saque:', colors.g + f'R$ {Dinheiro_guardado[0]:.2f}' + colors.e)
	ret = float(input('Quanto deseja retiirar? R$ '))
	
	if ret > sum(Dinheiro_guardado):
		print(colors.r + 'Quantia indisponível' + colors.e)
		
	elif ret <= 0:
		print(colors.r + '\nImpossivel retirar 0 reais ou menos' + colors.e)
		
	else:
		Dinheiro_disponivel[0] +=ret
		Dinheiro_guardado[0] -= ret
		Transacoes.append(('Retirada', ret))
		print(colors.g + 'Saque feito com sucesso' + colors.e)

#resgatar
def Resgatar():
	res = float(input('\nQuanto deseja resgatar? R$'))
	print('\nSeu dinheiro foi resgatado!')
	Dinheiro_disponivel[0] += res
	Transacoes.append(('Resgate', res))
	
#variáveis
line = '—'*18

#armazenar valores em listas
Dinheiro_guardado = [0.0]
Dinheiro_disponivel = [0.0]
Transacoes = []

#título personalizado
print('—'*48)
print(colors.y + 'SEJA BEM-VINDO(a) – DEPÓSITO E SAQUE DISPONÍVEIS' + colors.e)
print('—'*48)

#sistema principal
def Root():
	while True:
		print(colors.g + f'\nSaldo atual: R$ {Dinheiro_disponivel[0]:.2f}' + colors.e)
		print('\nMenu principal \n')
		print('[1] Depositar \n[2] Saque \n[3] Ver meu saldo \n[4] Sair \n\n[5] ajuda \n[6] Histórico')
		opc = input('\n>>> ')
		
		#estrutura condicional de ações
		if opc == '1':
			Depositar()
			
		elif opc == '2':
			Retirar()
			
		elif opc == '3':
			print(f'\nSeu saldo atual guardado é de', colors.g + f'R$ {Dinheiro_guardado[0]:.2f}' + colors.e)
			
		elif opc == '4':
			print('\nFinalizando...')
			time.sleep(3)
			LimparTerm()
			exit()
		
		#sistema para resgatar dinheiro
		elif opc == '5':
			print('\n [1] resgatar dinheiro \n [2] voltar \n')
			opc2 = input('>>> ')
			
			if opc2 == '1':
				Resgatar()
			
			if opc2 == '2':
				return Root()
				
		#sistema para histórico de transações
		elif opc == '6':
			 print(colors.y + '\nHistórico de transações:' + colors.e)
			 for i, transacao in enumerate(Transacoes, start=1):
			           tipo, valor = transacao
			           print(colors.c + f'{i}. Tipo: {tipo}, Valor: R${valor:.2f}' + colors.e)
		else:
			print(colors.r + '\nOpção inválida' + colors.e)

#faz com que a função Root seja executada junto ao script
if __name__ == "__main__":
	Root()
