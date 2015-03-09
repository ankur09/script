sudo do-release-upgrade
sudo sed -i 's/quantal/raring/' /etc/apt/sources.list
sudo apt-get update && apt-get dist-upgrade
