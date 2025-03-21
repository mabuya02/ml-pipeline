FROM ubuntu:latest
LABEL authors="mabuya"

ENTRYPOINT ["top", "-b"]