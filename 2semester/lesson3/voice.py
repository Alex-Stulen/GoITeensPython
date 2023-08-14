import json

import pyaudio

from vosk import Model, KaldiRecognizer

model = Model("vosk-model-en-us-0.22-lgraph")
recognize = KaldiRecognizer(model, 16000)

words = pyaudio.PyAudio()
stream = words.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8192
)

stream.start_stream()


def listening():
    print("start listening")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognize.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(recognize.Result())
            if answer.get("text"):
                yield answer["text"]


commands = {
    "open_google_chrome": {
        "words": ["open google chrome", "chrome", "google", "open internet"],
        "answer": "Відкриваю гугл хром"
    }
}


for text in listening():
    if text == "goodbye":
        break

    print(f"User: {text}")

print("bye!")
