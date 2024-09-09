from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from datetime import datetime
import pytz

# from config import API_ID, API_HASH

API_ID = 0000000  #insert your api_id
API_HASH = ''  #insert your api_hash
timeZone = 'Europe/Kiev'  #select your time zone
nickname = ''  #select your nickname

client = TelegramClient('session_name', API_ID, API_HASH)


def get_time():
    current_time = datetime.now(pytz.timezone(timeZone))
    hour = f'{current_time.hour:02}'
    minutes = f'{current_time.minute:02}'
    return f'{nickname}|{hour}:{minutes}'


async def change_name(new_first_name):
    await client(UpdateProfileRequest(first_name=new_first_name))


async def main():
    old_time = get_time()
    while True:
        if old_time != get_time():
            old_time = get_time()
            async with client:
                await change_name(f'{old_time}')
            #print('Changed to: ' + old_time)
            await asyncio.sleep(55)
        else:
            #print('Wait: ' + old_time)
            await asyncio.sleep(1)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
