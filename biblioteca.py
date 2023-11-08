import csv
  

# função que carrega arquivo csv
def carregar_csv(filename): 
    with open(filename, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            biblioteca.append(row)


# Verificar se ja existe biblioteca existente. Se não, criar arquivo csv novo
biblioteca_existente = 0
while biblioteca_existente == 0:
    biblioteca_existente = int(input('Já existe uma biblioteca criada anteriormente? 1- Sim, 2- Não: '))
    if biblioteca_existente == 1:
        # Comando para importar a biblioteca existente
        biblioteca = []
        csv_file_path = 'C:/Users/marco/projeto_restaurante/biblioteca.csv'
        carregar_csv(csv_file_path)
    elif biblioteca_existente == 2:
        biblioteca = []
    else:
        print('Digite OPÇÃO VÁLIDA.')


# função para adicionar livro
def adicionar_livro(titulo, autor, categoria, valor):
    livro = { 'Titulo': titulo,'Autor': autor, 'Categoria': categoria, 'Valor': valor}
    biblioteca.append(livro)

# função para salvar arquivo csv
def salvar_csv(filename):
    with open(filename, mode='w', newline='') as csv_file:
        dados = ['Titulo', 'Autor', 'Categoria', 'Valor']
        writer = csv.DictWriter(csv_file, fieldnames=dados)

        writer.writeheader()
        for livro in biblioteca:
            writer.writerow(livro)



                 
# funçao para pesquisar livro segundo um criterio
def pesquisar_livros(criteria, value):
    livro_achado = []
    
    for livro in biblioteca:
        if livro[criteria] == value:
            livro_achado.append(livro)
    
    return livro_achado

# função para atualizar um livro
def update_book_by_title(title, new_autor=None, new_categoria=None, new_valor=None):
    for livro in biblioteca:
        if livro['Titulo'] == title:
            if new_autor is not None:
                livro['Autor'] = new_autor
            if new_categoria is not None:
                livro['Categoria'] = new_categoria
            if new_valor is not None:
                livro['Valor'] = new_valor
            return True
    return False

# funçao para organizar e imprimir a biblioteca 
def sort_books_by_category(category):
    sorted_books = sorted(biblioteca, key=lambda x: x[category])
    return sorted_books

# Sample usage of the sort function
# Sort books by author
#sorted_by_author = sort_books_by_category('Author')
#print("Books Sorted by Author:")
#for book in sorted_by_author:
#    print(f"{book['Title']} by {book['Author']} ({book['Year Written']})")

# Sort books by title
#sorted_by_title = sort_books_by_category('Title')
#print("\nBooks Sorted by Title:")
#for book in sorted_by_title:
#    print(f"{book['Title']} by {book['Author']} ({book['Year Written']})")

# Sort books by year
#sorted_by_year = sort_books_by_category('Year Written')
#print("\nBooks Sorted by Year:")
#for book in sorted_by_year:
#    print(f"{book['Title']} by {book['Author']} ({book['Year Written']})")


# Sample usage of the functions
#adicionar_livro( 'Harry Potter and the Sorcerer\'s Stone','J.K. Rowling', 'fantasia',50)
#adicionar_livro( '1984', 'George Orwell','ficção', 30)
#adicionar_livro( 'The Lord of the Rings', 'J.R.R. Tolkien', 'fantasia', 100)
#w, x, y, z = input("Digite os dados do novo livro, separados por virgula: ").split(',')
#adicionar_livro(w,x,y,z)

# Sample usage of the search function

# To search by author
busca_autor = pesquisar_livros('Autor', 'J.K. Rowling')
print("Livros por J.K. Rowling:")
for livro in busca_autor: 
    print(f"{livro['Titulo']} ({livro['Categoria']})")

# To search by title
busca_titulo = pesquisar_livros('Titulo', '1984')
print("\nTitulo de livros '1984':")
for livro in busca_titulo:
    print(f"{livro['Autor']} ({livro['Categoria']})")

# To search by year
busca_categoria = pesquisar_livros('Categoria', 'fantasia')
print("\nLivros na categoria fantasia:")
for livro in busca_categoria:
    print(f"{livro['Titulo']} by {livro['Autor']}")

# Save the livro collection to a CSV file
salvar_csv('biblioteca.csv')

# Load the livro collection from the CSV file (optional)
# load_from_csv('biblioteca.csv')

# Display the livro collection
for livro in biblioteca:
    print(f"{livro['Titulo']} por {livro['Autor']} {livro['Categoria']} comprado por {livro['Valor']}")


# Update a livro by title
book_to_update = "1984"
new_autor = None
new_categoria = 'humor'

if update_book_by_title(book_to_update, new_autor, new_categoria):
    print(f"\nUpdated '{book_to_update}' in the collection.")
else:
    print(f"\nBook '{book_to_update}' not found in the collection.")


rodar = 1
while rodar !=0:
    selecionar=int(input('1-CADASTRAR, 2-REMOVER, 3- ATUALIZAR, 4-BUSCAR, 5-EXTRATO, 6-TOTAL INVESTIDO, 7-ENCERRAR '))
    if selecionar==7:
        rodar = 0
    elif selecionar ==1:
        print('Digite os dados na seguinte ordem:titulo,autor,categoria,valor. Use o vírgula para separar cada sessão.')
        print('\nExemplo:Hamlet,William Shakespeare,ficção,20')
        w, x, y, z = input("Digite os dados do novo livro, separados por virgula: ").split(',')
        adicionar_livro(w,x,y,z)
salvar_csv('biblioteca.csv')        
for livro in biblioteca:
    print(f"{livro['Titulo']} por {livro['Autor']} ({livro['Categoria']}) comprado por ({livro['Valor']})")