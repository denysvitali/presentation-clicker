# Clicker
A (Google Slides) presentation remote right in your pocket.

## What's Clicker?
Clicker is a basic presentation remote that can be used when presenting on Google Slides (and w/ a basic customization on ANY app).  
It was made in about 8 minutes before I was giving a presentation, because I didn't have any remote control with me.  
  
The graphics sucks because I did this in a rush, but it works perfectly. A 10 minutes timer is included (client-side) and starts on page load.  
  
Feel free to improve the project as you wish.
## Requirements
- Unix (because of `xdotool`)
- [xdotool](https://github.com/jordansissel/xdotool)
- Python 3
- A device that is going to be used as a remote (your phone?)
- A Wi-Fi connection (you can do tethering w/ your phone)

## Installation
```
$ git clone https://github.com/denysvitali/presentation-clicker
$ cd presentation-clicker
# pip install klein
```
## Run
```
python main.py
```

1. Open TCP/8080 via `iptables -A INPUT -p tcp --dport 8080`
2. Open your Google Slides presentation on your computer (where you started `main.py`)
3. Connect to http://your-pc-ip:8080/ with your remote (your phone or any browser-enabled device)

## Screenshots
![Presentation Remote screenshot](https://i.imgur.com/yq86DKc.jpg)