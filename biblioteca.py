
# função que carrega arquivo csv
def carregar_csv(arquivo): 
    with open(arquivo, mode='r') as arquivo_csv: # abre o arquivo em modo read. o WITH fecha o arquivo quando termina a função.
        linhas = arquivo_csv.readlines() # cada linha do arquivo CSV é salvo na variavel 'linhas' em uma lista de strings
        print(linhas)
        header = linhas[0].strip().split(',') # salva a primeira linha do csv como o header, que sao as chaves do dic
        for linha in linhas[1:]: # itera sobre cada linha depois do header
            dados = linha.strip().split(',') # extrai a linha e salva em uma lista
            print(dados)
            livro = dict(zip(header, dados)) # cria um dicionario, combinando o header como chaves e os dados  como values
            print(livro)
            biblioteca.append(livro) # adiciona o dicionario na lista biblioteca. a biblioteca é uma lista de dicionarios, com 
            print(biblioteca)

# função para mostrar a biblioteca

def extrato_biblioteca(arquivo):
    print(f"\n{'Titulo':<40} {'Autor':<25}{'Categoria':<15}{'Valor':<10}{'Data de Cadastro'}")
    print('---------------------------------------------------------------------------------------------------------')
    for livro in arquivo:        
        print(f"{livro['Titulo']:<40} {livro['Autor']:<25} {livro['Categoria']:<15}{livro['Valor']:<10}{livro['Data de Cadastro']}")
    print('\n')

# pedir a data do usuário
def data_de_cadastro():
    run = True
    while run:
        try:
            dia_de_cadastro = int(input('Digite o dia com dois dígitos DD :'))
            while dia_de_cadastro > 31 or dia_de_cadastro <1:
                print('O dia tem que ser entre 1 e 31. Repita: ')
                dia_de_cadastro = int(input('Digite o dia com dois dígitos DD :'))

            mes_de_cadastro = int(input('Digite o mês com dois dígitos MM:'))
            while mes_de_cadastro > 12 or mes_de_cadastro <1:
                print('O mes tem que ser entre 1 e 12. Repita: ')
                mes_de_cadastro = int(input('Digite o mês com dois dígitos MM :'))

            ano_de_cadastro = int(input('Digite o ano com quatro dígitos AAAA:'))
            while ano_de_cadastro != 2023:
                print('O ano tem que ser 2023. Repita: ')
                ano_de_cadastro = int(input('Digite o ano com quatro dígitos AAAA :'))
            data_atual = str(dia_de_cadastro) +'-'+ str(mes_de_cadastro)+ '-' +str(ano_de_cadastro)
            print(data_atual)
            return data_atual
        except ValueError:
            print('Digite somente numeros.')

today = data_de_cadastro()



# Verificar se ja existe biblioteca existente. Se não, criar arquivo csv novo
biblioteca_existente = '0'
while biblioteca_existente == '0':
    print(f'\nAtenção!. Criar uma nova biblioteca vai apagar biblioteca existente. ')
    biblioteca_existente = input('\nJá existe uma biblioteca? 123- Sim, 456- Não: ')
    if biblioteca_existente == '123':
        # Comando para importar a biblioteca existente
        biblioteca = []
        csv_path = 'biblioteca.csv'
        carregar_csv(csv_path)
    elif biblioteca_existente == '456':        
        biblioteca = []
    else:
        print('\nDigite OPÇÃO VÁLIDA.')
        biblioteca_existente = '0'


# função para adicionar livro
def adicionar_livro(titulo, autor, categoria, valor, data):
    
    livro = { 'Titulo': titulo,'Autor': autor, 'Categoria': categoria, 'Valor': valor, 'Data de Cadastro':data}
    biblioteca.append(livro)
    salvar_csv('biblioteca.csv')

# função para remover livro pelo titulo
def remover_livro(titulo):
    titulo_lower = titulo.lower()
    for livro in biblioteca[:]: #itera sobre uma copia para não dar erro, pois se fosse pelo original, cada remoção muda o index, se tiver varios titulos iguais
        if livro['Titulo'].lower() == titulo.lower():
            biblioteca.remove(livro)
            print(f'{titulo} foi removido da biblioteca.')
            

# função para salvar arquivo csv
def salvar_csv(arquivo):
    with open(arquivo, mode='w', newline='') as arquivo_csv:
        header = ['Titulo', 'Autor', 'Categoria', 'Valor', 'Data de Cadastro']
        arquivo_csv.write(','.join(header) + '\n')
        for livro in biblioteca:
            values = [str(livro[key]) for key in header]
            arquivo_csv.write(','.join(values) + '\n')

                 
# funçao para pesquisar livro segundo um criterio
def pesquisar_livros(header, criterio):
    livro_achado = []    
    for livro in biblioteca:
        if livro[header] == criterio:
            livro_achado.append(livro)    
    return livro_achado

# função para atualizar um livro
def atualizar_livro(titulo, novo_autor=None, nova_categoria=None, novo_valor=None):
    for livro in biblioteca:
        if livro['Titulo'] == titulo:
            if novo_autor is not None:
                livro['Autor'] = novo_autor
            if nova_categoria is not None:
                livro['Categoria'] = nova_categoria
            if novo_valor is not None:
                livro['Valor'] = novo_valor
            return True
    return False

# funçao para organizar e imprimir a biblioteca 
def organizar(ordenar):
    livros_organizados = sorted(biblioteca, key=lambda x: x[ordenar])
    return livros_organizados

# Programa rodando 
selecionar = '5'
while selecionar !='8':
    extrato_biblioteca(biblioteca)
    selecionar=input('1-CADASTRAR, 2-REMOVER, 3- ATUALIZAR, 4-BUSCAR, 5-EXTRATO, 6-TOTAL INVESTIDO, 7-ORDENAR, 8-FECHAR \n')
    if selecionar=='8':
        print('Encerrando programa')

    elif selecionar =='1': # Cadastrar
        print('Digite os dados na seguinte ordem: titulo, autor, categoria, valor.')
        w= input("Titulo do livro: ").upper()
        x= input("Autor: ").upper()
        y= input ("Categoria: ").upper()
        z= input("Valor pago: ") 
        if w =='':
            print('\nFalta o título do livro. Voltando ao menu principal.')
        else:    
            adicionar_livro(w,x,y,z,today)        

    elif selecionar == '2': # Remover
        remover = input('Digite o titulo do livro que quer remover: ')
        remover_livro(remover)

    elif selecionar == '3': # Atualizar
        w = input('Digite o titulo do livro que deseja atualizar. Se não precisar de correção nas outras áreas, deixe em branco.: ' ).upper()
        x = (input('Autor correto: ').upper() or None)
        y = (input('Categoria correta: ').upper() or None)
        z = (input('Valor correto: ') or None)
        atualizar_livro(w,x,y,z)
        if atualizar_livro(w,x,y,z):
            print(f'{w} atualizado.')
        else:
            print(f'{w} livro não encontrado.')

    elif selecionar == '4': # Buscar
        busca = input('Buscar por 1-titulo, 2-autor, 3-categoria: ')
        if busca == '1' or busca == '2' or busca == '3':
            if busca == '1':
                titulo = input('Digite o titulo: ').upper()
                if titulo != '':
                    busca_titulo = pesquisar_livros('Titulo', titulo)
                    print(f"\nTitulo de livros: {titulo}")
                    for livro in busca_titulo:
                        print(f"Autor: {livro['Autor']:<20} Categoria: {livro['Categoria']}")
                else:
                    print('Digite novamente')
            elif busca == '2':
                autor = input('Digite o autor: ').upper()
                if autor != '':
                    busca_autor = pesquisar_livros('Autor', autor)
                    print(f"\nLivros escritos por: {autor}")
                    for livro in busca_autor:
                        print(f"Livro: {livro['Titulo']:<20} Categoria: {livro['Categoria']}")
                else:
                    print('Digite novamente')
            elif busca == '3':
                categoria = input('Digite o categoria: ').upper()
                if categoria != '':
                    busca_categoria = pesquisar_livros('Categoria', categoria)
                    print(f"\nLivros na categoria: {categoria}")
                    for livro in busca_categoria:
                        print(f"Autor: {livro['Autor']:<20} Titulo: {livro['Titulo']}")
                else:
                    print('Digite novamente')
        else:
            print('Livro não encontrada ou inválida.')

    elif selecionar == '5': # Mostrar 
        extrato_biblioteca(biblioteca)

    elif selecionar == '6': # Valor da biblioteca

        for sub in biblioteca:
            sub['Valor'] = float(sub['Valor'])
        
        total = sum(sub['Valor'] for sub in biblioteca)
       
        print(f'\nTotal investido na biblioteca: R$ {total}.\n')
    elif selecionar == '7':
        ordem = input('Escreva como você quer ordenar a biblioteca. Escreva titulo, autor, ou categoria. ').capitalize()
        if ordem == 'Titulo' or ordem == 'Autor' or ordem == 'Categoria': 
            extrato_organizado = organizar(ordem)
            biblioteca = extrato_organizado
        else:
            print('Opção inválida. Voltando ao meu principal.')

    else:
        print('Selecione opção válida.')


salvar_csv('biblioteca.csv')        
extrato_biblioteca(biblioteca)
