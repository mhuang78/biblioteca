import csv
from datetime import datetime
  

# função que carrega arquivo csv
def carregar_csv(arquivo): 
    with open(arquivo, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for linha in reader:
            biblioteca.append(linha)

# função para mostrar a biblioteca

def extrato_biblioteca(arquivo):
    print(f"\n{'Titulo':<40} {'Autor':<25}{'Categoria':<15}{'Valor':<10}{'Data'}")
    print('---------------------------------------------------------------------------------------------------------')
    for livro in arquivo:        
        print(f"{livro['Titulo']:<40} {livro['Autor']:<25} {livro['Categoria']:<15}{livro['Valor']:<10}{livro['Data']}")
    print('\n')


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
    
    livro = { 'Titulo': titulo,'Autor': autor, 'Categoria': categoria, 'Valor': valor, 'Data':data}
    biblioteca.append(livro)
    salvar_csv('biblioteca.csv')

# função para remover livro pelo titulo
def remover_livro(titulo):
    for livro in biblioteca[:]: #itera sobre uma copia para não dar erro, pois se fosse pelo original, cada remoção muda o index, se tiver varios titulos iguais
        if livro['Titulo'] == titulo:
            biblioteca.remove(livro)
            print(f'{titulo} foi removido da biblioteca.')
            

# função para salvar arquivo csv
def salvar_csv(arquivo):
    with open(arquivo, mode='w', newline='') as csv_file:
        header = ['Titulo', 'Autor', 'Categoria', 'Valor','Data']
        writer = csv.DictWriter(csv_file, fieldnames=header)

        writer.writeheader()
        for livro in biblioteca:
            writer.writerow(livro)

                 
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
    selecionar=(input('1-CADASTRAR, 2-REMOVER, 3- ATUALIZAR, 4-BUSCAR, 5-EXTRATO, 6-TOTAL INVESTIDO, 7-ORDENAR, 8-FECHAR \n'))
    if selecionar=='8':
        print('Encerrando programa')

    elif selecionar =='1': # Cadastrar
        print('Digite os dados na seguinte ordem: titulo, autor, categoria, valor.')
        w= input("Titulo do livro: ").upper()
        x= input("Autor: ").upper()
        y= input ("Categoria: ").upper()
        z= input("Valor pago: ") 
        now = datetime.now()
        data = now.strftime('%d-%m-%Y')
        print(data)
        if w =='':
            print('\nFalta o título do livro. Voltando ao menu principal.')
        else:    
            adicionar_livro(w,x,y,z,data)        

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
