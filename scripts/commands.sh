#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

echo "Iniciando coletar arquivos estáticos..."
python manage.py collectstatic --noinput
echo "Arquivos estáticos coletados."

echo "Iniciando migrações..."
python manage.py makemigrations patrocrud
echo "Migrações criadas."

echo "Aplicando migrações..."
python manage.py migrate --noinput
echo "Migrações aplicadas."

python manage.py runserver 0.0.0.0:8000