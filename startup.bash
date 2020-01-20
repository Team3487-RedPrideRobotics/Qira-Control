git reset --hard
git fetch
git pull
amixer cset numid=3 1
hook=`cat ../qira-hook.txt`
sed -i "s@rephook@${hook}@g" docker-compose.yml
docker-compose up -d
chromium-browser --kiosk --app qira.local/qira-face
xdotool mousemove 300 300
