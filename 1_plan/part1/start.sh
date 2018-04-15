docker-compose rm --force
echo "loading tileserver-gl image"
docker load < ../tileserver-gl.tar.gz
docker-compose up