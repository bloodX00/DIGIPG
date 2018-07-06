from random import randint as r
from time import sleep as slp
import sl4a
droid = sl4a.Android()

print('o======({}{}'.format('='*24, '>'))
print('                                 DIGIPG')
print('                                       <{}{}'.format('='*24, ')======o'))
print('\n'*4, 'digite help')

def create_character():
    nome = input('digite o nome do personagem ').capitalize()
    idade = int(input('digite a idade do personagem '))
    origem = input('digite a origem do personagem ').capitalize()
    classe = input('digite a classe do seu personagem ').capitalize()
    raça = input('digite a raça do seu personagem ').capitalize()
    HP = int(input('pontos de vida: '))
    MP = int(input('pontos de mana: '))
    defesa = int(input('ponto de defesa atual: '))
    destreza = int(input('destreza atual '))
    força = int(input('digite a força do personagem '))
    dano = int(input('digite o dano mínimo do seu personagem '))
    luta = int(input('digite os pontos de luta '))
    camuflar = int(input('digite os pontos de camuflagem '))
    agilidade = int(input('digite os pontos de agilidade '))
    lvl = int(input('digite o lvl atual do seu personagem '))
    gold = int(input('digite a grana atual do seu pesonagem '))
    try:
        p1 = open('sdcard/DIGIPG/{}.txt'.format(nome), 'a')
        p1.write('''nome: {}        idade: {}\n
        origem: {}        classe: {}        \n
        raça: {}\n
        --------------------------------------------------
        --------------------------------------------------\n
        
        vida: {}        mana: {}        defesa: {}\n
        \n
        destreza: {}    força: {}        dano: {}\n
        \n
        luta: {}        camuflar: {}    agilidade: {}\n
        \n
        \n
        LVL: {}
        Gold: {}'''.format(nome, idade, origem, classe, raça, HP, MP, defesa, destreza, força, dano, luta, camuflar, agilidade, lvl, gold))
        p1.close()
        print('personagem criado com sucesso!')
    except:
        print('ocorreu um erro.')
        print('''provavelmente pasta DIGIPG não existe no sdcard.\n
        por favor, crie a pasta DIGIPG no sdcard''')

def helpie():
    print('"roll"....................modo de rolagem de dados')
    print('''    dados suportados;\n
                    D2, D4, D6, D8, D12, D16, D20, D30, D100''')
    print('"exit"....................sair do programa')
    print('"soma"....................somar os resultados')
    print('"sub".....................subtrair HP e MP')
    print('"create -persona".........criação de personagem')
    print('        antes crie uma pasta chamada DIGIPG no sdcard.')

def loadice():
    droid.dialogCreateSpinnerProgress('  Rolando o dado', 'Aguarde...')
    droid.dialogShow()
    slp(2)
    droid.dialogDismiss()

def roll(d):
    loadice()
    res = r(1, d)
    print('resultado do dado D{} :: {}'.format(d, res))
    if res == 1:
        print('\033[1;31mERRO CRITICO\033[m')
    elif res == d:
        print('\033[1;34mACERTO CRITICO\033[m')


while True:
    comando = input('\033[1;31mo\033[m==\033[1;33m€=====>\033[m ')
    res = 0

    if comando == 'soma':
        print('digite 999 para finalizar a soma')
        rec = 0
        while True:
            v = int(input('\033[1;31m======E\033[m '))
            rec = rec + v
            if v == 999:
                break
        print('a soma total foi de {}'.format(rec - 999))
                        #não repara na gambiarra ^
    elif comando == 'sub':
        v1 = int(input('atributo: '))
        v2 = int(input('subtração: '))
        ata = v1 - v2
        print('resultado: ', ata)
    elif comando == 'exit':
        exit()
    elif comando == 'help':
        helpie()
    elif comando == 'create -persona':
        create_character()
    elif comando == 'roll':
        dado = int(input('qual dado deseja rolar? D'))
        if not dado == 2 and not dado == 4 and not dado == 6 and not dado == 8 and not dado == 12 and not dado == 16 and not dado == 20 and not dado == 30 and not dado == 100:
            print('ERRO: Dado não suportado.')
            print('use apenas os dados: D2, D4, D6, D8, D12, D16, D20, D30, D100')
        else:
            roll(dado)
    else:
        print('Comando não conhecido.')
