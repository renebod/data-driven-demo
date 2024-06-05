FROM python:3.8
MAINTAINER René Bod "https://github.com/renebod"

RUN apt-get update
RUN apt-get install -y sshpass

WORKDIR "/code"

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm requirements.txt

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
