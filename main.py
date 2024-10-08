import requests
import json
import time

# Telegram ID
telegram_id = 

# API untuk bergabung
url_join = "https://www.pandas.pp.ua/api/users/join/"
headers_join = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
}

payload_join = {"user_id": telegram_id}

response_join = requests.post(url_join, headers=headers_join, data=json.dumps(payload_join))

# Memeriksa status respons dari join
if response_join.status_code == 200:
    join_data = response_join.json()
    
    user_data = join_data.get("user", {})
    username = user_data.get("username")  # Mengambil username dari user_data
    balance = user_data.get("balance")
    
    print("Username:", username)
    print("Balance:", balance)
else:
    print("Error joining:", response_join.status_code)

# API pertama untuk mendapatkan reward
url_reward = "https://www.pandas.pp.ua/api/daily_reward/"
headers_reward = {
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Origin": "https://pandas-clone2.vercel.app",
    "Content-Type": "application/json",
}

payload_reward = {"telegram_id": telegram_id}

response_reward = requests.post(url_reward, headers=headers_reward, data=json.dumps(payload_reward))

# Mendapatkan nilai 'message' dan 'ban' dari respons reward
data_reward = response_reward.json()
message = data_reward.get("message")
ban = data_reward.get("ban")

print("Message:", message)
print("Ban:", ban)

# Jeda selama 2 detik sebelum verifikasi tugas pertama
time.sleep(2)

# Berinteraksi dengan API untuk verifikasi tugas pertama
url_verify = "https://www.pandas.pp.ua/api/tasks/verify/"
headers_verify = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
}

payload_verify_1 = {
    "telegram_id": telegram_id,
    "task": "Subscribe to Pandas channel",
    "reward": 1000,
    "username": username
}

response_verify_1 = requests.post(url_verify, headers=headers_verify, data=json.dumps(payload_verify_1))

# Memeriksa status respons verifikasi
if response_verify_1.status_code == 200:
    verify_data_1 = response_verify_1.json()
    print(verify_data_1)
else:
    print("Maybe Task Is Done")

# Jeda selama 2 detik sebelum verifikasi tugas kedua
time.sleep(2)
