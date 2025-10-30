import asyncio
import os

async def run_bot():
    while True:
        try:
            print("🚀 Bot ishga tushyapti...")
            os.system("python bot.py")  # Asosiy bot fayling
        except Exception as e:
            print(f"Xato yuz berdi: {e}")
            print("♻️ 10 soniyadan so‘ng qayta ishga tushadi...")
            await asyncio.sleep(10)

asyncio.run(run_bot())
