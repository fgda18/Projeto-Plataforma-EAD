
#Menu Projeto 3.1

#Menu

#bibliotecas
import os
import time
import requests 
from datetime import datetime
#Funções

def cadastro():
        os.system("cls")
        cabeçalho ("CADASTRO DE NOVO USUÁRIO")
        dados_login = verificar_cpf()
        if  dados_login['logado']:
            cpf = dados_login['cpf']
            nome = verificar_nome()
            dt_nasc = verificar_data_de_nascimento()
            email = verificar_email()
            cep = verificar_cep()
            endereco_aluno = consultar_cep(cep)

            if isinstance(endereco_aluno, dict):
                aluno[cpf] = {
                    'Nome': nome,
                    'Data de Nascimento': dt_nasc,
                    'Email': email,
                    'Endereço': endereco_aluno
                }
            else:
                print(f'\033[0;31mErro ao Buscar endereço:\033[0m {endereco_aluno}')
                
            input ('\033[1;36maperte qualquer tecla para voltar\033[0m')
            os.system("cls")
            input("Voltando à tela inicial! Seu cadastro no Instituto Antônio Carlos foi realizado com sucesso!")
            loading('Logando','CARLINHOS')
            login(dados_login['cpf'])
        
        else:
            input("CPF já cadastrado, aperte qualquer tecla para continuar")
            os.system("cls")
            login(dados_login['cpf'])


def login(Login):
        os.system("cls")
        print ('\033[33maperte "ENTER" duas vezes para cancelar e voltar à tela inicial\033[0m')
        cpf = Login
        if cpf in aluno:
            while True:
                #print ('\033[33maperte "ENTER" duas vezes para cancelar e voltar ao menu\033[0m')
                os.system("cls")
                resposta2 = Tela_inicial(['Dados da matrícula','Alterar dados da matrícula','Excluir matrícula', 'Acessar cursos', 'Voltar à tela inicial'])
                #DADOS DA MATRÍCULA
                if resposta2 == 1:
                    os.system("cls")
                    cabeçalho('DADOS DA MATRÍCULA')
                    exibir_dados(cpf)
                    input('\033[1;36maperte qualquer tecla para voltar\033[0m')

                #ALTERAR OS DADOS DA MATRÍCULA
                if resposta2 == 2:
                    os.system('cls')
                    cabeçalho('ALTERAR DADOS DA MATRÍCULA')
                    alterar_dados(cpf)
                    input('\033[1;36maperte qualquer tecla para voltar\033[0m')

                #EXCLUSAO DA MATRICULA
                if resposta2 == 3:
                    os.system('cls')
                    cabeçalho('EXCLUSÃO DA MATRÍCULA')
                    excluir_matricula(cpf)
                    input('\033[1;36maperte qualquer tecla para voltar\033[0m')

                #ACESSAR CURSOS
                if resposta2 == 4:
                    while True:
                        os.system("cls")
                        cabeçalho("OPÇÕES DE CURSOS")
                        print('''\033[1;36m1\033[0m - Medicina
\033[1;36m2\033[0m - Análise e desenvolvimento de dados(ADS)
\033[1;36m3\033[0m - Direito
\033[1;36m4\033[0m - Administração
\033[1;36m5\033[0m - Odontologia
\033[1;36m6\033[0m - Psicologia
\033[1;36m7\033[0m - Voltar''')
                        escolha = int(input('VISUALIZAR CURSO (ID)>> '))
                        if escolha < 1 and escolha > 7:
                            input('ID de curso inválido!')
                        elif escolha == 1:
                            os.system("cls")
                            medicina()
                            input ('\033[1;36maperte qualquer tecla para voltar\033[0m')
                        elif escolha == 2:
                            os.system("cls")
                            ads()
                            input ('\033[1;36maperte qualquer tecla para voltar\033[0m')
                        elif escolha == 3:
                            os.system("cls")
                            direito()
                            input ('\033[1;36maperte qualquer tecla para voltar\033[0m')
                        elif escolha == 4:
                            os.system("cls")
                            administracao()
                            input ('\033[1;36maperte qualquer tecla para voltar\033[0m')
                        elif escolha == 5:
                            os.system("cls")
                            odontologia()
                            input ('\033[1;36maperte qualquer tecla para voltar\033[0m')
                        elif escolha == 6:
                            os.system("cls")
                            psicologia()    
                            input ('\033[1;36maperte qualquer tecla para voltar\033[0m')
                        elif escolha == 7:
                            os.system("cls")
                            loading("Voltando", '\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m')
                            break


                #VOLTAR A TELA INICIAL
                if resposta2 == 5:
                    os.system("cls")
                    loading("Voltando à tela inicial", '\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m')
                    break
        else:
            print("\033[0;31mCPF não encontrado no sistema.\033[0m Insira um CPF cadastrado ou realize seu cadastro.")
            confirmar = input("Digite \033[1;32m'S'\033[0m para cadastrar um novo usuário ou qualquer outra tecla para voltar ao menu: ").strip().upper()
            
            if confirmar == 'S':
                cadastro()

def validar_cpf_duplicado(cpf):
    try:
        if aluno[cpf]:
            
            return True
    
    except KeyError as e:
        return False


#FUNÇÃO DE CEP
def consultar_cep(cep):
    #URL da API dos correios para consultar cep
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if 'erro' in dados:
            return '\033[0;31mCEP não encontrado.\033[0m'
        
        return dados
    
    except requests.exceptions.RequestException as e:
        return f"\033[0;31mOcorreu um erro: {e}\033[0m"

#FUNÇÃO LEIA INTEIRO
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[0m')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n
        
#FUNÇÃO LEIA REAL
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real válido.\033[0m')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

#FUNÇÃO LINHA
def linha(tam=50):
    return '-' *tam

#FUNÇÃO DE CABEÇALHO
def cabeçalho(txt):
    print (linha())
    print (txt.center(50))
    print (linha())

#FUNÇÃO DE MENU DOS DOCENTES
def Tela_inicial (lista):
    cabeçalho("\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m")
    c =1
    for item in lista:
        print (f'\033[1;36m{c}\033[0m - {item}')
        c += 1
    print (linha())
    opc = leiaInt('Sua opção: ')
    return opc

#FUNÇÃO DE MENU DOS PROFESSORES
def menu_usuario (lista):
    cabeçalho("\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m")
    c =1
    for item in lista:
        print (f'\033[0;33m{c}\033[m - {item}')
        c += 1
    print (linha())
    opc = leiaInt('Sua opção: ')
    return opc


def loading (string1, string2):
    c=1
    while c<3:
        cabeçalho(string2)
        print(string1, '.')
        time.sleep(0.33)
        os.system("cls")
        cabeçalho(string2)
        print(string1, '..')
        time.sleep(0.33)
        os.system("cls")
        cabeçalho(string2)
        print(string1, '...')
        time.sleep(0.33)
        os.system("cls")
        c=c+1

def consultar_cep(cep):
    #URL da API dos correios para consultar cep
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if 'erro' in dados:
            return '\033[0;31mCEP não encontrado.\033[0m'
        
        endereco = {
            'rua': dados.get('logradouro'),
            'bairro': dados.get('bairro'),
            'cidade': dados.get('localidade'),
            'estado': dados.get('uf')
        }

        print('\033[4;32mEndereço encontrado:\033[0m ')
        for chave, valor in endereco.items():
            print(f'{chave.capitalize()}: {valor}')
        
        numero = leiaInt('Número: ')
        complemento = input('Complemento (opcional): ')

        endereco['numero'] = numero
        endereco['complemento'] = complemento if complemento else None           

        return endereco
    
    except requests.exceptions.RequestException as e:
        return f"\033[0;31mOcorreu um erro: {e}\033[0m"
    
    
def verificar_nome():
    while True:
        try:
            vnome = input("Digite o seu nome completo: ").upper()
            if not all(c.isalpha() or c.isspace() for c in vnome):
                raise ValueError("\033[0;31mNome Inválido\033[0m. Deve conter apenas letras e espaços.")
            if len(vnome.strip()) == 0:
                raise ValueError("\033[0;31mNome Inválido\033[0m. Não pode estar vazio.")
            partes_nome = vnome.split()
            if len(partes_nome) < 2:
                raise ValueError("\033[0;31mNome Inválido\033[0m. Deve conter pelo menos um nome e um sobrenome.")
            return vnome
        except ValueError as e:
            print(f"Erro: {e}")
            print("\033[0;36mTente novamente\033[0m.")

def verificar_cep():
    while True:
        try:
            vcep = input("Digite o seu CEP (somente números): ")
            if len(vcep) != 8:
                raise ValueError("\033[0;31mCEP Inválido\033[0m. Deve conter 8 dígitos.")
            if not vcep.isdigit():
                raise ValueError("\033[0;31mCEP Inválido\033[0m. Deve conter apenas números.")
            return vcep
        except ValueError as e:
            print(f"Erro: {e}")
            print("\033[0;36mTente novamente\033[0m.")

def verificar_cpf(): #função pra validar o formata do CPF
    while True:
        try:
            chave = input('CPF \033[0;33m(000.000.000-XX)\033[0m: ')
            if len(chave) != 14:
                raise ValueError(f'\033[0;31mFormato inválido!!\033[0m Por favor, use \033[0;33m(000.000.000-XX)\033[0m.')   
            if not chave[0].isdigit() or not chave[1].isdigit() or not chave[2].isdigit() or not chave[4].isdigit() or not chave[5].isdigit() or not chave[6].isdigit() or not chave[8].isdigit() or not chave[9].isdigit() or not chave[10].isdigit() or not chave[12].isdigit() or not chave[13].isdigit():
                raise ValueError("\033[0;31mCPF Inválido\033[0m. Deve conter apenas números.")
            if len(chave) == 14 and chave[3] == '.' and chave[7] == '.' and chave [11] == '-':
                if validar_cpf_duplicado(chave):
                    return {'logado': False, 'cpf': chave}
                
                return {'logado': True, 'cpf': chave}
            
        except ValueError as e:
            print(f"Erro: {e}")
            print("\033[0;36mTente novamente\033[0m.")

def verificar_data_de_nascimento(): #função pra validar o formato da data de nascimento
    while True:
        try:
            dtnasc = input("Digite a sua data de nascimento \033[0;33m(DD/MM/AAAA)\033[0m: ")
            dia, mes, ano = dtnasc.split('/')
            
        
            if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                raise ValueError("\033[0;31mData de Nascimento Inválida\033[0m. Deve conter apenas números.")
            
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            
        
            if not (1 <= dia <= 31):
                raise ValueError("\033[0;31mDia Inválido\033[0m. (1-31)")
            if not (1 <= mes <= 12):
                raise ValueError("\033[0;31mMês Inválido\033[0m. (1-12)")
            
            
            if not (1900 <= ano <= 2024):
                raise ValueError("\033[0;31mAno Inválido\033[0m. Deve estar entre 1900 e 2024.")
            
            
            calcular = datetime(ano, mes, dia)
            
        
            idade = (datetime.now() - calcular).days // 365
            if idade < 18:
                raise ValueError("\033[0;31mMenor de Idade\033[0m. Deve ter pelo menos 18 anos.")
            
            if idade >= 18:
                return dtnasc
        except ValueError as e:
            print(f"Erro: {e}")
            print("\033[0;36mTente novamente\033[0m.")
        except Exception as e:
            print("\033[0;31mErro Desconhecido\033[0m. Certifique-se de usar o formato DD/MM/AAAA.")
            print(f"Detalhes do erro: {e}")
            print("\033[0;36mTente novamente\033[0m.")

def exibir_dados(cpf):
    if cpf in aluno:
        dados = aluno[cpf] 
        print("\nDados da Matrícula:")
        for chave, valor in dados.items():
            if isinstance(valor, dict):
                print(f"{chave}:")
                for subchave, subvalor in valor.items():
                    print(f"  {subchave.capitalize()}: {subvalor}")
            else:
                print(f"{chave}: {valor}")
    else:
        print("\033[0;31mCPF não encontrado no sistema.\033[0m Insira um CPF cadastrado ou realize seu cadastro.")
        confirmar = input("Digite \033[1;32m'S'\033[0m para cadastrar um novo usuário ou qualquer outra tecla para voltar ao menu: ").strip().upper()
        
        if confirmar == 'S':
            cadastro()
        else:
            os.system("cls")
            loading("Voltando ao menu","\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m")

def alterar_dados(cpf):
    if cpf in aluno:
        print("\nDados atuais:")
        for chave, valor in aluno[cpf].items():
            if isinstance(valor, dict):
                print(f"{chave}:")
                for subchave, subvalor in valor.items():
                    print(f"  {subchave.capitalize()}: {subvalor}")
            else:
                print(f"{chave}: {valor}")

        print("\nQual dado deseja alterar?")
        opcoes = list(aluno[cpf].keys())  
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")

        escolha = leiaInt("\nDigite o número da opção desejada: ")

        
        if 1 <= escolha <= len(opcoes):
            chave_selecionada = opcoes[escolha - 1]

            
            if not isinstance(aluno[cpf][chave_selecionada], dict):
                novo_valor = input(f"Digite o novo valor para \033[0;33m{chave_selecionada}\033[0m: ")
                aluno[cpf][chave_selecionada] = novo_valor
                print(f"\033[4;32m{chave_selecionada} alterado com sucesso!\033[0m")

            
            else:
                print(f"Alterando dados de \033[0;33m{chave_selecionada}\033[0m:")
                subopcoes = list(aluno[cpf][chave_selecionada].keys())
                for i, subopcao in enumerate(subopcoes, start=1):
                    print(f"{i} - {subopcao.capitalize()}")

                subescolha = leiaInt("\nDigite o número do dado do endereço que deseja alterar: ")
                if 1 <= subescolha <= len(subopcoes):
                    subchave_selecionada = subopcoes[subescolha - 1]
                    novo_valor = input(f"Digite o novo valor para \033[0;33m{subchave_selecionada.capitalize()}\033[0m: ")
                    aluno[cpf][chave_selecionada][subchave_selecionada] = novo_valor
                    print(f"\033[4;32m{subchave_selecionada.capitalize()} alterado com sucesso!\033[0m")
                else:
                    print("\033[0;31mOpção inválida para o endereço.\033[0m")
        else:
            print("\033[0;31mOpção inválida.\033[0m")
    else:
        print("\033[0;31mCPF não encontrado no sistema.\033[0m Insira um CPF cadastrado ou realize seu cadastro.")
        confirmar = input("Digite \033[1;32m'S'\033[0m para cadastrar um novo usuário ou qualquer outra tecla para voltar ao menu: ").strip().upper()
        
        if confirmar == 'S':
            cadastro()
        else:
            os.system("cls")
            loading("Voltando ao menu","\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m")

def verificar_email():
    while True:
        try:
            temail = input("Digite o seu e-mail: ")
            if "@" not in temail or "." not in temail.split("@")[1]:
                raise ValueError("\033[0;31mE-mail Inválido\033[0m.")
            if len(temail.strip()) == 0:
                raise ValueError("\033[0;31mE-mail Inválido\033[0m. Não pode estar vazio.")
            return temail
        except ValueError as e:
            print(f"Erro: {e}")
            print("\033[0;36mTente novamente\033[0m.")


def excluir_matricula(cpf):
    if cpf in aluno:
        print("\nDados da matrícula encontrados:")
        for chave, valor in aluno[cpf].items():
            if isinstance(valor, dict):
                print(f"{chave}:")
                for subchave, subvalor in valor.items():
                    print(f"  {subchave.capitalize()}: {subvalor}")
            else:
                print(f"{chave}: {valor}")
        
        print("\n\033[1;33mTem certeza de que deseja excluir esta matrícula?\033[0m")
        confirmar = input("Digite \033[1;32m'S'\033[0m para confirmar ou qualquer outra tecla para \033[31mcancelar\033[0m: ").strip().upper()
        
        if confirmar == 'S':
            del aluno[cpf]
            print("\n\033[4;32mMatrícula excluída com sucesso!\033[0m")
        else:
            print("\n\033[0;31mOperação cancelada.\033[0m")
    else:
        print("\033[0;31mCPF não encontrado no sistema.\033[0m Insira um CPF cadastrado ou realize seu cadastro.")
        confirmar = input("Digite \033[1;32m'S'\033[0m para cadastrar um novo usuário ou qualquer outra tecla para voltar ao menu: ").strip().upper()
        
        if confirmar == 'S':
            cadastro()
        else:
            os.system("cls")
            loading("Voltando ao menu","\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m")

def medicina():
    print('''
\033[34m___________________________________________________\033[0m
          
    CURSO: MEDICINA
    DURAÇÃO: 6 anos
    ÁREA: Saúde
    Aulas:
    1. Anatomia Humana
    2. Fisiologia
    3. Farmacologia
    4. Patologia
    5. Clínica Médica
    6. Cirurgia Geral
\033[34m___________________________________________________\033[0m
    ''')

def ads():
    print('''
\033[34m___________________________________________________\033[0m
          
    CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
    DURAÇÃO: 3 anos
    ÁREA: Tecnologia
    Aulas:
    1. Algoritmos e Programação
    2. Estrutura de Dados
    3. Desenvolvimento Web
    4. Banco de Dados
    5. Engenharia de Software
    6. Redes de Computadores
\033[34m___________________________________________________\033[0m
    ''')

def direito():
    print('''
\033[34m___________________________________________________\033[0m
          
    CURSO: DIREITO
    DURAÇÃO: 5 anos
    ÁREA: Ciências Humanas
    Aulas:
    1. Direito Constitucional
    2. Direito Penal
    3. Direito Civil
    4. Direito Empresarial
    5. Direito Trabalhista
    6. Direito Internacional
\033[34m___________________________________________________\033[0m
    ''')

def administracao():
    print('''
\033[34m___________________________________________________\033[0m
          
    CURSO: ADMINISTRAÇÃO
    DURAÇÃO: 4 anos
    ÁREA: Ciências Sociais
    Aulas:
    1. Introdução à Administração
    2. Marketing
    3. Gestão de Pessoas
    4. Contabilidade
    5. Finanças Empresariais
    6. Planejamento Estratégico
\033[34m___________________________________________________\033[0m
    ''')

def odontologia():
    print('''
\033[34m___________________________________________________\033[0m
          
    CURSO: ODONTOLOGIA
    DURAÇÃO: 5 anos
    ÁREA: Saúde
    Aulas:
    1. Anatomia Dentária
    2. Periodontia
    3. Endodontia
    4. Prótese Dentária
    5. Radiologia Odontológica
    6. Cirurgia Buco-maxilo-facial
\033[34m___________________________________________________\033[0m
    ''')

def psicologia():
    print('''
\033[34m___________________________________________________\033[0m
          
    CURSO: PSICOLOGIA
    DURAÇÃO: 5 anos
    ÁREA: Ciências Humanas
    Aulas:
    1. Teorias da Personalidade
    2. Psicologia do Desenvolvimento
    3. Psicopatologia
    4. Psicologia Social
    5. Neuropsicologia
    6. Psicoterapia
\033[34m___________________________________________________\033[0m
    ''')



#LISTAS E DICIONÁRIOS
aluno = {'499.523.228-10': {'Nome': 'FELIPE GOMES', 'Data de Nascimento': '11/03/2006', 'Email': 'fgda14gomes@gmail.com', 'Endereço': {'rua': 'Caminho do Pinheirinho', 'bairro': 'Jardim Amazonas', 'cidade': 'Itaquaquecetuba', 'estado': 'SP', 'numero': 25, 'complemento': None}}, '445.616.928-19': {'Nome': 'VICTOR SASAKI', 'Data de Nascimento': '11/04/2005', 'Email': 'vcsasaki@gmail.com', 'Endereço': {'rua': 'Rua São Diego', 'bairro': 'Jardim Califórnia', 'cidade': 'Jacareí', 'estado': 'SP', 'numero': 601, 'complemento': 'ap73A'}}}
cursos = {
'1':medicina, 
'2':ads,
'3':direito, 
'4':administracao, 
'5':odontologia, 
'6':psicologia}


#CORES
verde = '\033[4;32m'
vermelho = '\033[0;31m'
ciano = '\033[4;36m'
amarelo = '\033[1;33m'
amarelosub = '\033[4;33m'
reset = '\033[0m'


# MENU TELA INICIAL

os.system("cls")
while True:
    os.system("cls")
    resposta1 = Tela_inicial(['Novo usuário', 'Usuário já existente', 'Sair do programa'])
    
#NOVO USUÁRIO
    if resposta1 == 1:
        cadastro()

#USUÁRIO JÁ EXISTENTE
    if resposta1 == 2:
        os.system('cls')
        login(input("Informe o CPF cadastrado: "))

#SAIR DO APLICATIVO
    if resposta1 == 3:
        os.system("cls")
        loading("Saindo do programa", '\033[4;34mINSTITUTO ANTÔNIO CARLOS\033[0m')
        break    