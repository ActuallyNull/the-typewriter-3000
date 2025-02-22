import time
import random
import pyautogui
import keyboard
from dotenv import load_dotenv
import os
import requests

load_dotenv()
pastebin_api_key = os.getenv("PASTEBIN_API_KEY")
pastebin_url = "https://pastebin.com/RdQHxLYJ"

def get_pastebin_text(pastebin_url):
    """Retrieves text from a Pastebin URL."""
    try:
        raw_url = pastebin_url.replace("pastebin.com/", "pastebin.com/raw/")
        response = requests.get(raw_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pastebin: {e}")
        return None

def human_like_typing(text, wpm=5500):
    """Types text with human-like delays and pauses, handling tabs and spacing."""

    if text is None:
        return

    for char in text:
        if keyboard.is_pressed('*'):
            print("\nTyping stopped by user.")
            return

        delay = random.uniform(0.045, 0.06) / wpm
        time.sleep(delay)

        if char == '\n':
            pyautogui.press('enter')
            time.sleep(random.uniform(0.1, 0.3) / wpm)
            pyautogui.press('tab')

        else:
            pyautogui.write(char)

        if char == " " :
            word_pause = random.uniform(0.1, 0.3) / wpm
            time.sleep(word_pause)
        if char in (".", "?", "!"):
            sentence_pause = random.uniform(0.5, 2) / wpm
            time.sleep(sentence_pause)

    print("\nTyping complete.")

text = get_pastebin_text(pastebin_url)
human_like_typing(text)