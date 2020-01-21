git reset --hard
git fetch
git pull
amixer cset numid=3 1
hook=`cat ../qira-hook.txt`
sed -i "s@rephook@${hook}@g" docker-compose.yml
xdotool mousemove 300 300
docker-compose up -d
sleep 5
chromium-browser --kiosk --app qira.local/qira-face
