# Clock Script

The script makes your Telegram nickname more interactive by adding a clock to it.

# Easy start
Just clone the repository:
```bash
git clone https://github.com/SerhiiKuzmenko/clockInNickTg
```
To work with the script, you need to get your API_ID and API_HASH telegram. 
And also in the code, initialize the corresponding variables with your data: API_ID, API_HASH, timeZone, nickname. 
Set your time zone and choose a nickname. Ultimately, your nickname will look like this - nickname|00:00
---
**Create and activate your virtual environment:**
```bash
python -m venv .venv
```
Windows:
```powershell
.venv/Scripts/activate
```
Unix-systems:
```bash
source .venv/bin/activate
```
**Install packages**:
```bash
pip install telethon pytz
```
---
And run your script!
```bash
python run.py
```
You will also need to log in to your telegram account upon first launch. 
You will need to enter your number and telegram confirmation code. 
It may also ask for a cloud password if you have one.
