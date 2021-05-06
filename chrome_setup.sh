#!/bin/bash

# #setup chrome and chrome driver for selenium use
# #install dependencies
sudo apt update
sudo apt install -qy unzip xvfb libxi6 libgconf-2-4

# #install chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
sudo rm ./google-chrome-stable_current_amd64.deb

# #install chrome driver
LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
echo $LATEST

chrome_version=$(google-chrome --version | cut -d " " -f3)
echo $chrome_version

chrome_driver_url=$"https://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip"
echo $chrome_driver_url

wget $chrome_driver_url
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

sudo rm chromedriver_linux64.zip