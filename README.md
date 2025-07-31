# get-img
CLI Python script to download random images of a specific size

This script prompts for:
  -The number of images to download
  -The desired size 
  -The destination directory.
  
Then it sends an HTTP request to the https://picsum.photos API and downloads random images to the directory.


# Requirements

The script requires the Python environment to have the **requests** package to be able to send HTTP requests.
It can be installed with pip like this:

**Windows: (through CMD admin mode)**
python -m pip install requests

**MacOS / Linux: **
pip3 install requests

It might be necessary to reset the console after installing the package

After this, the script can be ran from the console as:
"python get-img.py"


Adding the script to the system's scripts directory will allow calling the script without CDing into the directory that contains it.
