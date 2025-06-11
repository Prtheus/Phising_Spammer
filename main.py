import time
from dotenv import load_dotenv
import os
import requests
from tqdm import tqdm


from utils.groups import Group
from utils.person import Person

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
sleep_time = 2
number_of_requests = 20

def send_to_telegram(person: Person):
    text = f"🎖️💰 - {person.email}:{person.password}"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        response = requests.get(BASE_URL, params=payload, timeout=10)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

def main():
    group = Group(number_of_identities= number_of_requests)

    for person in tqdm(group.identities, desc="Send Data", unit="Person"):
        send_to_telegram(person)
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
