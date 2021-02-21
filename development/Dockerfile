FROM ubuntu:20.04

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
    sqlite3 && \
	pip3 install -U pip setuptools && \
	rm -rf /var/lib/apt/lists/*


COPY requirements.txt /home/docker/code/
RUN pip3 install -r /home/docker/code/requirements.txt

COPY zapatos_bernini /home/docker/code/zapatos_bernini

COPY development/docker_entrypoint.sh /home/docker/code/zapatos_bernini/

EXPOSE 8000

WORKDIR /home/docker/code/zapatos_bernini
ENTRYPOINT ["/bin/python3", "manage.py", "runserver", "0:8000"]