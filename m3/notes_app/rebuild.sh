docker build -t notes .
docker run --rm -p 80:80 --name notes notes