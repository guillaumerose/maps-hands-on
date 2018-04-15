docker-compose rm --force
echo "loading tileserver-gl image from ../tileserver-gl.tar.gz"
docker load < ../tileserver-gl.tar.gz
docker-compose up