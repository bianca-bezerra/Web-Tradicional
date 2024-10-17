# PATROCARS 🚗

## Objetivo: 
Proporcionar a experiência de trabalhar com Sistemas Web que renderizam HTML prontos à moda anos 2000.

## Descrição 
Sistema Web CRUD Básico para o Cadastro de Montadoras e Veículos associados.

### Funcionalidades

- **Montadoras**: Adicionar, Listar, Editar e Remover.
- **Modelos**: Adicionar, Listar, Editar e Remover.
- **Veículos**: Adicionar, Listar, Editar e Remover.

OBS: A funcionalidade de detalhamento existe e está disponível, mas precisa de melhorias.

### Stack:
- **Framework**: Django
- **Banco de Dados Relacional**: PostgreSQL
- **ORM**: Django ORM
- **Deploy**: Em breve no Render.

## Como executar:
1. Crie um arquivo **.env** na raiz do projeto com a mesma estrutura do arquivo **.env.example.**
2. Para iniciar o ambiente local, execute o comando a seguir:
   
   ```bash
   docker-compose up --build
   ```
3. Acesse o sistema através do ```localhost:8000```

## 📋 TO-DO
- Melhoria na componentização dos templates
- Criação de uma página home mais temática
- Melhoria na funcionalidade de detalhar
- Melhoria nos links entre as páginas para otimizar o relacionamento entre as entidades.
- Adição de filtragem
- Fazer o deploy
