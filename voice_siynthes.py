import torch
import sounddevice as sd
import time

language = "ua"
model_id = "v4_ua"
sample_rate = 48000
speaker = "mykyta" # random
put_accent = True
put_yoo = True
device = torch.device("cpu")

texts = "Привіт Андрій. Як твої справи? Все добре?"


model, _ = torch.hub.load(repo_or_dir="snakers4/silero-models",
                                     model="silero_tts",
                                     language=language,
                                     speaker=model_id)
model.to(device)  # gpu or cpu

def volume_sintes():
    txt = str(input("Send Text: "))
    audio = model.apply_tts(text=txt,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            )


    sd.play(audio, sample_rate)
    volume_sintes()
    # time.sleep(len(audio) / sample_rate)
    # sd.stop()

volume_sintes() # "Мир тобі, -ласкаво сказав ангел, сідаючи поруч з котом на товсту гілку і струшуючи з неї сніг. Привіт, -кіт розплющив зелені очі, ліниво оглянув ангела і відвернувся."