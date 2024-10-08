import requests
import json
import time

# Telegram ID
telegram_id = 1656996131

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
    username = "slamet 🍅"  # Mengganti username
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

response_verify_1 = requests.get(url_verify, headers=headers_verify, data=json.dumps(payload_verify_1))

# Memeriksa status respons verifikasi
if response_verify_1.status_code == 200:
    verify_data_1 = response_verify_1.json()
    claimed_1 = verify_data_1.get("claimed", False)  # Ambil nilai claimed dari response
    print("Subscribe to Pandas channel:", claimed_1)
else:
    print("Maybe Task Is Done")

# Jeda selama 2 detik sebelum verifikasi tugas kedua
time.sleep(2)

# Berinteraksi dengan API untuk verifikasi tugas kedua
payload_verify_2 = {
    "telegram_id": telegram_id,
    "task": "Subscribe to Official telegram channel",
    "reward": 10,
    "username": username
}

response_verify_2 = requests.get(url_verify, headers=headers_verify, data=json.dumps(payload_verify_2))

# Memeriksa status respons verifikasi untuk tugas kedua
if response_verify_2.status_code == 200:
    verify_data_2 = response_verify_2.json()
    claimed_2 = verify_data_2.get("claimed", False)  # Ambil nilai claimed dari response
    print("Subscribe to Official telegram channel:", claimed_2)
else:
    print("Maybe Task Is Done")

# Jeda selama 2 detik sebelum verifikasi tugas ketiga
time.sleep(2)

# Berinteraksi dengan API untuk verifikasi tugas ketiga
payload_verify_3 = {
    "telegram_id": telegram_id,
    "task": "Subscribe to X",
    "reward": 500,
    "username": username
}

response_verify_3 = requests.get(url_verify, headers=headers_verify, data=json.dumps(payload_verify_3))

# Memeriksa status respons verifikasi untuk tugas ketiga
if response_verify_3.status_code == 200:
    verify_data_3 = response_verify_3.json()
    claimed_3 = verify_data_3.get("claimed", False)  # Ambil nilai claimed dari response
    print("Subscribe to X:", claimed_3)
else:
    print("Maybe Task Is Done")

# Jeda selama 2 detik sebelum verifikasi tugas keempat
time.sleep(2)

# Berinteraksi dengan API untuk verifikasi tugas keempat
payload_verify_4 = {
    "telegram_id": telegram_id,
    "task": "Join Water on Ton",
    "reward": 500,
    "username": username
}

response_verify_4 = requests.get(url_verify, headers=headers_verify, data=json.dumps(payload_verify_4))

# Memeriksa status respons verifikasi untuk tugas keempat
if response_verify_4.status_code == 200:
    verify_data_4 = response_verify_4.json()
    claimed_4 = verify_data_4.get("claimed", False)  # Ambil nilai claimed dari response
    print("Join Water on Ton:", claimed_4)
else:
    print("Maybe Task Is Done")

# Jeda selama 2 detik sebelum verifikasi tugas kelima
time.sleep(2)

# Berinteraksi dengan API untuk verifikasi tugas kelima
payload_verify_5 = {
    "telegram_id": telegram_id,
    "task": "Join Water Telegram",
    "reward": 500,
    "username": username
}

response_verify_5 = requests.get(url_verify, headers=headers_verify, data=json.dumps(payload_verify_5))

# Memeriksa status respons verifikasi untuk tugas kelima
if response_verify_5.status_code == 200:
    verify_data_5 = response_verify_5.json()
    claimed_5 = verify_data_5.get("claimed", False)  # Ambil nilai claimed dari response
    print("Join Water Telegram:", claimed_5)
else:
    print("Maybe Task Is Done")

# Mengupdate saldo
url_update_balance = "https://www.pandas.pp.ua/api/users/update_balance/"
headers_update_balance = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
}

# Menghitung saldo baru
new_balance = balance + 500

# Payload untuk memperbarui saldo
payload_update_balance = {
    "telegram_id": telegram_id,
    "balance": new_balance
}

# Mengirim permintaan POST untuk memperbarui saldo
response_update_balance = requests.post(url_update_balance, headers=headers_update_balance, data=json.dumps(payload_update_balance))

# Memeriksa status respons
if response_update_balance.status_code == 200:
    update_data = response_update_balance.json()
    print("Balance updated successfully:", update_data)
else:
    print("Error updating balance:", response_update_balance.status_code)
