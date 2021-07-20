docker build -t notes .
docker tag idors:latest gregxsunday/notes:prod
docker push gregxsunday/notes:prod