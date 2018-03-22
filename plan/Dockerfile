FROM nginx
ADD static/ /usr/share/nginx/html/
RUN chmod 555 -R /usr/share/nginx/html/*
CMD ["nginx", "-g", "daemon off;"]