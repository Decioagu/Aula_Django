# Aula_Django

- Framework Web Django

- O Django é um framework web em Python de alto nível usado para criar aplicações web de forma rápida, segura e escalável.

**01_Aula_HTML**

- __HTML__ (HyperText Markup Language) ou (Linguagem de Marcação de Hipertexto). 
- É a linguagem base usada para criar páginas e conteúdos na web. O HTML não é uma linguagem de programação, mas sim uma linguagem de marcação. Para adicionar comportamentos (como interações com o usuário), geralmente usamos JavaScript.
    - __Tags__ (etiquetas ou marcação) são palavras-chave envolvidas por sinais de menor "<" e maior ">", em __HTML__ são os elementos usados para marcar e estruturar o conteúdo de uma página. Elas dizem ao navegador como exibir o conteúdo.

    - Exemplo de marcação (tag): <p>Olá, mundo!</p>
        - Onde:
            <p>: é a tag de abertura (parágrafo)
            Olá, mundo!: é o conteúdo entre as tags
            </p>: é a tag de fechamento
    
    - Resumindo: 
        - HTML → estrutura

- link: https://developer.mozilla.org/pt-BR/docs/Web/HTML
...

**02_Aula_CSS**

- __CSS__ significa (Cascading Style Sheets) ou (Folhas de Estilo em Cascata).
- É a linguagem usada para definir o estilo visual de elementos HTML, como: Cores, fontes, tamanhos, margens e espaçamentos, layouts (posições, colunas, etc). 

    - Pode se aplicar o CSS de três formas:
        - CSS Inline:
            - O estilo é aplicado diretamente no elemento HTML (tag), usando o atributo style.
        - CSS Interno (ou Embutido):
            - O CSS é escrito dentro da própria página HTML, na tag <style> que vai dentro do <head>.
        - CSS Externo:
            - O CSS é escrito em um arquivo separado com a extensão .css, e esse arquivo é link no <head> do HTML usando <link>.

    - Resumindo: 
        - HTML → estrutura
        - CSS → aparência/estilo
...

**03_Aula_JavaScript**

- __JavaScript__ é uma linguagem de programação usada principalmente para criar interatividade em páginas web.
- Enquanto o __HTML__ define a estrutura e o __CSS__ define o estilo, o __JavaScript__ é o que dá vida à página — permitindo que ela reaja a ações do usuário, modifique elementos, valide formulários, se comunique com servidores e muito mais.

    - Resumindo: 
        - HTML → estrutura
        - CSS → aparência/estilo
        - JavaScript → 	Comportamento e interatividade
...

**04_Aula_frameworks**

- Um framework frontend é um conjunto de ferramentas, bibliotecas e regras prontas que ajudam os desenvolvedores a criar a interface visual de um site ou aplicação web (a parte que o usuário vê e interage), sem precisar "reinventar a roda" toda vez.

- link: https://getbootstrap.com.br/
...

**05_Aula_Templates**

- Templates (ou modelos) são estruturas prontas de código usadas para gerar conteúdo dinâmico de forma mais rápida, organizada e reutilizável.
    - Exemplo de uma estrutura HTML já construida.
...

**Aula_06**

- Projeto_01

- Roteiro para criação de projeto Django:
    - Se você quiser que o Django crie uma pasta automaticamente com o projeto dentro, use:
        - django-admin startproject NOME_DA_PASTA
    - Se já está na pasta onde quer o projeto, use:
        - django-admin startproject NOME_DA_PASTA .

- Roteiro para criação de uma aplicação Django:
    - django-admin startapp NOME_DA_APLICAÇÃO

- Iniciar execução do Django dentro da pasta do projeto:
    - python manage.py runserver

-  Arquivo:
    - core:
        - migrations: Nova aplicação
        - __init__.py: Nova aplicação
        - __admin.py__: Nova aplicação
        - __apps.py__: Nova aplicação
        - __models.py__: Nova aplicação
        - __tests.py__: Nova aplicação
        - __views.py__: Nova aplicação
    - projeto:
        - __asgi.py__: Novo projeto
        - __settings.py__: Mudança de idioma para "pr-br" e adição de 'core' em INSTALLED_APPS
        - __urls.py__: Novo projeto
    - __db.sqlite3__: Novo projeto
    - __manage.py__: Novo projeto

- core:
    - migrations:
        - Pasta vazia
    - __init__.py: 
        - Indica que a pasta é um pacote Python
    - __admin.py__: 
        - Configurações para o Django Admin
    - __apps.py__: 
        - Dados de configuração do app
    - __models.py__: 
        - Onde você define os modelos (tabelas do banco)
    - __tests.py__: 
        - Testes automatizados (opcional)
    - __views.py__: 
        - Funções que respondem às requisições
- projeto:
    - __asgi.py__:
        - É um ponto de entrada para servidores web compatíveis com ASGI (Asynchronous Server Gateway Interface), como o Uvicorn, Daphne ou Hypercorn. Ele é equivalente ao __wsgi.py__, mas voltado para comunicação assíncrona.
    - __settings.py__:
        - Arquivo responsável pela configuração de banco de dados, segurança, diretórios, apps instalados, idiomas, entre muitos outros ajustes.
    - __urls.py__:
        - Arquivo responsável por definir as rotas do seu site (url).
    - __wsgi.py__:
        - É o ponto de entrada para servidores web compatíveis com WSGI (Web Server Gateway Interface), como o Gunicorn, uWSGI ou mod_wsgi (Apache). Ele serve para inicializar e expor a aplicação Django para o servidor web em ambiente de produção.
- __db.sqlite3__: 
    - Banco de Dados.
- __mannge.py__:
    - Inicia o servidor local de desenvolvimento e gerencia tarefas.
...

**Aula_07**

- Projeto_01

-  Arquivo:
    - core:
        - __admin.py__: Configuração de registro "Django admin"
        - __models.py__: Modelagem tabela do Banco de Dados
        - __views.py__: Adição de requisições para templates (paginas HTML)
        - migrations:
            - __0001_initial.py__: Modelagem automática após __models.py__
        - templates:
            - __500.html__: Pagina HTML
            - __400.html__: Pagina HTML
            - __index.html__: Pagina HTML (context de views.py)
            - __produto.html__: Pagina HTML (context de views.py)
            - __contato.html__: Pagina HTML
    - projeto:
        - __settings.py__: Adição de diretório ('DIRS': ['templates']) em TEMPLATES
        - __urls.py__: Adição de rotas de requisições __views.py__

- __0001_initial.py__:
    - Quando você cria ou altera um modelo (por exemplo, adiciona um novo campo em uma tabela) em __models.py__, o Django não aplica essas mudanças diretamente no banco de dados. Em vez disso, ele precisa de um "roteiro" (chamado de migração) que diga exatamente o que deve ser feito.

    - Roteiro para ativação Banco de dados:
        - Após modelagem do Banco de Dados em "__models.py__" aplicar comando para modelagem automática: 
            - python manage.py makemigrations

        - Depois de criar a migração, você aplica as mudanças no Banco de Dados com:
            - python manage.py migrate

    - Roteiro para usuário administrador do Banco de dados via Django: 
        -  Criar um usuário administrador (superusuário) do sistema para acesso a rota Django admin:
            - python manage.py createsuperuser
    
    - Usuário e senha cadastrado:
        - http://127.0.0.1:8000/admin/login/?next=/admin/
            - Usuário: decio
            - Senha: dsa
...

**Aula_08**

- Projeto_01

- Arquivo:
    - core:
        - static:
            - css:
                - __estilos.css__: Estilo para pagina HTML
            - images:
                - __django.png__: Imagem para pagina HTML
            - js:
                - __script.js__: Programação JavaScript para pagina HTML
        - templates:
            - __500.html__: pagina HTML (exceção personalizado)
            - __400.html__: pagina HTML (exceção personalizado)
            - __index.html__: adição de arquivos pasta static
            - __produto.html__: adição de arquivos pasta static
        - __views.py__: Adição de requisições exceção personalizado (paginas de erro HTML personalizada)
    - projeto:
        - __settings.py__: Redirecionamento de pagina "index.html" e adição de  STATIC_ROOT
        - __urls.py__: Adição de exceção personalização (erro)
    - staticfiles:
        - __*arquivos static__: gerados por "python manage.py collectstatic"

- __settings.py__: 
    - STATIC_ROOT: Caminho onde o Django vai colocar todos os arquivos estáticos coletados de cada app e do diretório STATICFILES_DIRS.

    - Roteiro de ativação:
        - python manage.py collectstatic

    - Será gerado pasta "staticfiles"
    
    - OBS: o  comportamento do Django muda de acordo com DEBUG:
        - Com DEBUG = True: Django serve arquivos estáticos automaticamente durante o desenvolvimento.
        - Com DEBUG = False: Django não serve arquivos estáticos sozinho — você precisa usar collectstatic e configurar um servidor web externo (como Nginx ou Apache) para isso.
...

**Aula_09**

pip install whitenoise gunicorn
- Projeto_01

-------------------------------------------------
Arquivo:
    - core:
        - static:
            - css:
                - __estilos.css__: 
            - images:
                - __django.png__: 
            - js:
                - __script.js__: 
        - migrations:
            - __0001_initial.py__: 
        - templates:
            - __500.html__: 
            - __400.html__: 
            - __index.html__: 
            - __contato.html__: 
            - __produto.html__: 
        - __init__.py: 
        - __admin.py__: 
        - __apps.py__: 
        - __models.py__: 
        - __tests.py__: 
        - __views.py__: 
    - projeto:
        - __asgi.py__:
        - __settings.py__: 
        - __urls.py__:
    - staticfiles:
        - __*arquivos static__: gerados por "python manage.py collectstatic"
    - __db.sqlite3__:
    - __manage.py__:


