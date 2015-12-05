#!/bin/sh
BASE_PATH=`pwd`
echo "#!/bin/sh" >> bot_startup.sh
echo "cd "$BASE_PATH >> bot_startup.sh
echo ". venv/bin/activate" >> bot_startup.sh
echo "cd bot" >> bot_startup.sh
echo "nohup python bot.py &" >> bot_startup.sh
sudo chmod +x bot_startup.sh
sudo mv bot_startup.sh /etc/init.d
sudo update-rc.d bot_startup.sh defaults