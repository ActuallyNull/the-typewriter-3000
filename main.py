import time
import random
import pyautogui
import keyboard

def human_like_typing(text, wpm=110):
    """Types text with human-like delays and pauses, stopping on numpad *."""

    words = text.split()

    for i, word in enumerate(words):
        for char in word:
            if keyboard.is_pressed('*'):
                print("\nTyping stopped by user.")
                return  # Exit the function

            delay = random.uniform(0.045, 0.06) / wpm
            time.sleep(delay)
            pyautogui.write(char)

        pyautogui.write(" ")
        word_pause = random.uniform(0.1, 0.3) / wpm
        time.sleep(word_pause)

        if random.random() < 0.05:
            sentence_pause = random.uniform(0.5, 2)
            time.sleep(sentence_pause)

        if word.endswith((".", "?", "!")):
            sentence_pause = random.uniform(0.5, 2) / wpm
            time.sleep(sentence_pause)

    print("\nTyping complete.")

# Example usage
text = """This is a very long text that I am writing to simulate human-like typing.
It should have various pauses, both short and long, to mimic the way a person
would type.  Sometimes, there will be long thinking breaks, where the person
contemplates what to write next. This is important to make it seem realistic.
We also want to have realistic word per minute.  We will try to make it around 110.
Sometimes, the user will make mistakes and have to go back and correct them.
But we are not going to simulate that in this example.  We will just keep typing.
This is a good way to test the function and see if it works as expected.
It should be fun to watch it type out the text.  We will see how it goes.
Hopefully, it will be convincing.  We can even add some random capitalization
or spelling errors, but that might be a bit too much for this example.  We can save
that for a more advanced version of the script.  For now, this should be enough.
"""

human_like_typing(text)