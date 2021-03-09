### Description: 
Dashcam recording script for raspberry pi (open source tool developed by [learnitbro.com](https://learnitbro.com/))

### Steps:
- Download the script
- Setup a crontab job
- Turn on the raspberry pi

### Dependencies:
- opencv
- python 3

### Hardware:
- Raspberry Pi 4 4GB
- Raspberry Pi Camera Module V2-8 Megapixel
- Camera/Phone Car Mount
- Car Charger Adapter 2.4A
- Type-C Cable

### Configuration:
First, you need to setup the camera

Open the terminal and update/upgrade your device
```
sudo apt update
sudo apt full-upgrade
```
Now you need to enable the camera  using the raspi-config
```
sudo raspi-config
```
Use the cursor keys select and open Interfacing Options then select Camera
Follow the prompt to enable the camera and reboot the device

To test that the system is installed and working, try the following command:
```
raspistill -v -o test.jpg
raspivid -o vid.h264
```
Now you need to install python opencv and its dependencies
```
pip3 install opencv-python
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install python3-pyqt5
sudo apt install libqt4-test
```

Now run the program
```
python3 dashcam.py
```
To specify the segment time, framerate, resolution or even the filename, use the command below
```
python3 dashcam.py -t <segment time> -f <framerate> -w <width> -h <height> -n <name>
```