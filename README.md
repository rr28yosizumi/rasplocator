# rasplocator
raspberrypi用


# install

## i2c
sudo apt install i2c-tools

sudo i2cdetect -y 1

MPU9250
FaBo9AXIS-MPU9250-Python
https://github.com/FaBoPlatform/FaBo9AXIS-MPU9250-Python

## opencv

sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

sudo apt-get install libcblas-dev libatlas3-base libilmbase12 libopenexr22 libgstreamer1.0-0 libqtgui4 libqttest4-perl

sudo pip3 install opencv-python
sudo pip3 install opencv-contrib-python

## gps

sudo apt-get install python-serial

pip install pyserial
git clone https://github.com/inmcm/micropyGPS.git

