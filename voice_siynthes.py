import torch
import sounddevice as sd
import time

language = "ua"
model_id = "v4_ua"
sample_rate = 48000
speaker = "mykyta" # aidar, baya, kseniya, xenia, random
put_accent = True
put_yoo = True
device = torch.device("cpu")
texts = "Привіт Назар. Як справи?"


model, _ = torch.hub.load(repo_or_dir="snakers4/silero-models",
                                     model="silero_tts",
                                     language=language,
                                     speaker=model_id)
model.to(device)  # gpu or cpu


audio = model.apply_tts(text=texts,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        )


sd.play(audio, sample_rate)
time.sleep(len(audio) / sample_rate)
sd.stop()