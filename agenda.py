
agenda = []

def inserir_nome():
    return(input('Nome da pessoa: '))

def inserir_telefone():
    return(input('Digite o telefone: '))

def inserir_endereco():
    return(input('Digite o endereço: '))

def adicionar():
    global agenda
    nome = inserir_nome()
    telefone = inserir_telefone()
    endereço = inserir_endereço()
    agenda.append([nome, telefone, endereco])

def adicionar1():
    nome_arquivo = inserir_nome()
    arquivo = open(nome_arquivo, 'W' ,encoding="utf-8")
    for e in agenda:
        arquivo.write("Nome: %s Telefone: %s Endereço: %s \n" %(e[0], e[1], e[2]))
    arquivo.close()

    print("\n---------------------------")
    print("bem-vindo a agenda!")
    print("-----------------------------")

    print("Escolha o tipo de operações")

    operacoes = input(''' Para adicionar digite "adicionar" ''')

    if operacoes == 'adicionar' :
        print('\nOpção Adicionar selecionada')
        adicionar()
        adicionar1()

    else:
        print('Você não digitou um valor aceitavel!')
        print('fim de operação!')

    print ("fim de operação!")
    

    
