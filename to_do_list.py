from time import sleep

def mostrar_lista(lista):
    print()
    print('--- Lista de tarefas ---')
    for indice, valor in enumerate(lista):
        print(f'{indice+1}°: {valor}')
    print()

def desfazer(lista, refazer_lista):
    if not lista:
        print('\nNada para se desfazer.')
        return
    last_item = lista.pop()
    refazer_lista.append(last_item)

def refazer(lista, refazer_lista):
    if not refazer_lista:
        print('\nNada para se refazer.')
        return
    last_item = refazer_lista.pop()
    lista.append(last_item)

def separar_linhas():
    print('-'*45)


if __name__ == '__main__':
    lista = []
    refazer_lista = []


    while True:
        separar_linhas()
        sleep(1.5)
        opcao_lista = input(
"""\nEscolha uma das seguinte opções:
\n[1] Adicionar tarefa na lista;
[2] Desfazer tarefa adicionado anteriormente;
[3] Refazer tarefa anterior da lista;
[4] Mostrar lista;
[x] Sair.
\nQual opção desejas? """)

        while opcao_lista not in '1234x':
            print('\n[ERROR] Digite uma resposta válida.')
            separar_linhas()
            sleep(1.5)
            opcao_lista = input(
"""\nEscolha uma das seguinte opções:
\n[1] Adicionar tarefa na lista;
[2] Desfazer tarefa adicionado anteriormente;
[3] Refazer tarefa anterior da lista;
[4] Mostrar lista;
[x] Sair.
\nQual opção desejas? """)

        else:
            if opcao_lista == '1':
                item = input('\nDigite a tarefa: ')
                lista.append(item)

            elif opcao_lista == '2':
                desfazer(lista, refazer_lista)

            elif opcao_lista == '3':
                refazer(lista, refazer_lista)

            elif opcao_lista == '4':
                mostrar_lista(lista)

            elif opcao_lista == 'x':
                break

separar_linhas()
print('Encerrando..')
sleep(3)
print('\nObrigado por utilizar esse sistema, volte sempre.')
separar_linhas()

