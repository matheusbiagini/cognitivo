
### Teste da Cognitivo:

O teste foi feito utilizando o Docker, Mysql, Python e Django.

### Configurando o ambiente:

1. Instalar o Docker-CE (17.12+)
2. Instalar o Docker-compose (1.2+).
3. Adicionar permissão do docker `sudo usermod -aG docker ${USER}`
4. Adicionar permissão do usuário `sudo su - ${USER}`
4. Clonar o projeto: `git clone https://github.com/matheusbiagini/cognitivo`
5. Entre na pasta raiz do projeto.
7. Adicionar permissão no conteúdo: `sudo chown -R $USER:$USER .`
8. Inicie o docker: `docker-compose up -d`
9. Rode as migrations: `docker-compose exec web python manage.py migrate applestore`

### Executando o Teste:
Digite no browser: `http://localhost:8000/cognitivo/applestore/api`

### Resultado do teste: ###
O teste vai gerar os dados de acordo com o proposto no teste(Json+Tabela+Csv) e o arquivo csv "Reports.csv".

Obrigado. :)
