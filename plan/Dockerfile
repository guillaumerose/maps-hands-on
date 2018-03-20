FROM nginx

RUN apt-get update;apt-get install -y curl
COPY static/* /usr/share/nginx/html/

RUN curl https://api.tiles.mapbox.com/mapbox-gl-js/v0.44.1/mapbox-gl.js -o /usr/share/nginx/html/js/mapbox-gl.js --create-dirs
RUN curl https://code.jquery.com/jquery-3.3.1.js -o /usr/share/nginx/html/js/jquery.js --create-dirs
RUN curl https://api.tiles.mapbox.com/mapbox-gl-js/v0.44.1/mapbox-gl.css -o /usr/share/nginx/html/css/mapbox-gl.css --create-dirs

RUN chmod 555 -R /usr/share/nginx/html/*
CMD ["nginx", "-g", "daemon off;"]