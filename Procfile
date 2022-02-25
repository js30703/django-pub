web: gunicorn --bind 127.0.0.1:8000 --workers=3 --threads=3 -k=gevent config.wsgi:application
websocket: daphne -b 127.0.0.1 -p 5000 config.asgi:application
celery: celery -A config worker --concurrency=1 --loglevel=INFO