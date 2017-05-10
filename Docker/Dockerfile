FROM nginx:latest
MAINTAINER Junior Lima <josiasjuniorx@gmail.com>

RUN apt-get update
RUN apt-get install -yf apt-utils python-pip uwsgi uwsgi-plugin-python whois dnsutils host git
RUN pip install django
RUN git clone https://github.com/josiasjuniorx/consulta-dominio.git /var/www/html/
ADD dominio.conf /etc/nginx/conf.d/default.conf
ADD init /init
EXPOSE 80
CMD ["/bin/bash", "-c", "source /init"]
