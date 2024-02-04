# Texas A&M Admission Check Bot for Discord

This bot allows a user to login in using their NetID and find out way their admission status is without having to load up the website and login in!

All you got to do is run !check to see your status!


![Logo](https://cdn.itsodrjr.dev/tmp/api/public/dl/_G_t2pJE?inline=true)


## Installation

**NOTE: You must have Duo Mobile 2FA off for this to work!**

I've only tested this on Ubuntu 22.04, however it will probably work on Debian. 

**Install Python** (If you don't have it already installed)
```bash
sudo apt-get update
sudo apt-get install python3.6
```
**Clone and install repo along with requirements**
```bash
cd ~
git clone https://github.com/ItsODRJR/tamuAdmissionCheckBot
cd tamuAdmissionCheckBot
pip install -r requirements.txt
```
**Edit the config file**
```bash
nano config.json
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | NetID username |
| `password` | `string` | NetID password |
| `botToken` | `string` | Discord Bot Token [Learn More](https://discord.com/developers) |
| `currentStatus` | `string` | Set this as your current application status (you probably have the default value) |

**Run the bot**
```bash
python3 admissionBot.py
```

Now you can run !check in your discord server to see your status!

Now you can also run !loop in your discord server to start a loop that checks to see if your status changes every 30 seconds!

I know this is kinda stupid but I had fun making it and thought it would be cool to share :D