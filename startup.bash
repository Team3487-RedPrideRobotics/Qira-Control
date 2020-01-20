git reset --hard
git fetch
git pull
hook=`cat ../qira-hook.txt`
sed -i "s@rephook@${hook}@g" docker-compose.yml
docker-compose up -d
sleep 25
chromium-browser --no-user-action --kiosk qira.local/qira-face
