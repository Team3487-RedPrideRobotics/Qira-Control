git reset --hard
git fetch
git pull
amixer cset numid=3 1 #Set output to 3.5mm
hook=`cat ../qira-hook.txt`
sed -i "s@rephook@${hook}@g" docker-compose.yml
xdotool mousemove 300 300
docker-compose up -d #start servers
sleep 5
chromium-browser --kiosk --app qira.local/qira-face #start chrome
