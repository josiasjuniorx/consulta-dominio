FROM nginx:latest
ENV LANG pt_BR.UTF-8
MAINTAINER Junior Lima <josiasjuniorx@gmail.com>

RUN apt-get update
RUN apt-get install -yf apt-utils locales python-pip uwsgi uwsgi-plugin-python dnsutils host git
RUN locale-gen pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt:en
ENV LC_ALL pt_BR.UTF-8
RUN pip install django requests
RUN git clone https://github.com/josiasjuniorx/consulta-dominio.git /var/www/html/
ADD dominio.conf /etc/nginx/conf.d/default.conf
ADD init /init
EXPOSE 80
CMD ["/bin/bash", "-c", "source /init"]
