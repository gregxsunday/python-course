# Manual Installation

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:80 wsgi:app
```

# Using docker

```
docker build -t notes .
docker run --rm -p 80:80 --name notes notes
```

http://localtest.me:80/
