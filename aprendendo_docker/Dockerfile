
# Usar o python 2.7
FROM python:2.7-slim

# Definindo o diretorio corrente para sendo o /app
WORKDIR /app

# Copiando o conteudo do diretorio corrente para o conteiner dentro de /app
ADD . /app

# Instalando quaisquer pacotes especificados no requirements.txt
RUN pip install -r requirements.txt

# Deixando a porta 80 acessível de fora do container
EXPOSE 80

# Definindo uma variável de ambiente
ENV NAME world

# Executando o app.py quando o container inicia
CMD ["python", "app.py"]


