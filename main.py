import asyncio
from telethon import TelegramClient, errors
from datetime import datetime
import random
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE")

message_to_send = """
🎰 Online Earning Opportunity 🎰

Earn money using:
🎡 Spin Wheel
🎰 Slot Machine
🎁 Daily Bonus
👥 Refer & Earn

❌ No deposit required  
✅ Free registration  
📱 Works on mobile & PC

Join now:
Link 1 - https://is.gd/UAW1va
Link 2 - https://is.gd/zZlQjh
Link 3 - https://is.gd/Frkk3C
"""

target_groups = [
    "@online_earningmethods",
    "@emolgroup",
    "@Onlineearning06741",
    "@online_earn_money55",
    "@torontopubliccommunity"
]

client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.start()
    cycle = 1

    while True:
        print(f"🔁 Cycle {cycle} started at {datetime.now()}")

        for group in target_groups:
            try:
                await client.send_message(group, message_to_send)
                await asyncio.sleep(random.randint(60, 110))

            except errors.FloodWaitError as e:
                await asyncio.sleep(e.seconds)

            except Exception as e:
                print(e)

        cycle += 1
        await asyncio.sleep(300)  # 6 hours

asyncio.run(main())

