To get the Waveshare Hat installed and working with Python 3:

```bash

sudo apt install python3 python3-dev python3-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
sudo apt-get install libatlas-base-dev libopenjp2-7 # things needed for numpy and pillow
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libtbb2 libtbb-dev libjpeg-dev libpng12-dev libtiff-dev libjasper-dev libdc1394-22-dev

```
