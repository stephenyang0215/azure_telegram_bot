FROM ubuntu:latest
LABEL authors="stephenyang"
 docker run -it -e NGROK_AUTHTOKEN=<token> ngrok/ngrok http 80
ENTRYPOINT ["top", "-b"]