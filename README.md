#Bem vindo ao meu teste da Cognitivo "Freelance"

## Configurando o ambiente para o teste:

1. Instalar o Docker-CE (17.12+)
2. Instalar o Docker-compose
3. Permissão do docker `sudo usermod -aG docker ${USER}`
4. Permissão do usuário `sudo su - ${USER}`
4. Clonar o projeto: `git clone https://github.com/matheusbiagini/cognitivo`
5. Entre na pasta raiz do projeto.
7. Adicionar permissão: `sudo chown -R $USER:$USER .`
8. Rodar: `docker-compose up -d`
9. Rodar as migrations: `docker-compose exec web python manage.py migrate applestore`
11. Digite no browser `http://localhost:8000/cognitivo/applestore/api`
12. Obrigado :)
