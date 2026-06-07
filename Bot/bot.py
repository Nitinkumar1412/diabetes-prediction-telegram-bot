import asyncio
import requests
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "8412589155:AAGIAiaq6jyEOZMhfqrAZJ_YjZhRXV_QRsw"
API_URL = "http://127.0.0.1:8000/predict"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_message(message: types.Message):
    try:
        values = list(map(float, message.text.split(",")))

        if len(values) != 7:
            raise ValueError("Wrong number of inputs")

        data = {
            "age": values[0],
            "pregnancies": values[1],
            "Glucose": values[2],
            "Blood_pressure": values[3],
            "SkinThickness": values[4],
            "insulin": values[5],
            "BMI": values[6]
        }

        response = requests.post(API_URL, json=data)
        result = response.json()
        print("API RESPONSE:", result) 

        await message.answer(
            f"Prediction: {result['prediction']}\n\n{result['explanation']}"
        )

    except Exception as e:
        print("ERROR:", e)   # 👈 VERY IMPORTANT (see terminal)

        await message.answer(
            "Send exactly 7 values like:\n"
            "Age,Pregnancies,Glucose,BP,Skin,Insulin,BMI\n\n"
            "Example:\n45,2,150,85,30,0,33.6"
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())