import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from faster_whisper import WhisperModel

import json
model=WhisperModel("small",compute_type="int8")
audio_file="audios/6_SEO and Core Web Vitals in HTML.mp3"
print("transcribing audio...")

segments,info=model.transcribe(
    audio_file,
    language="hi",
    task="translate"
    )

data = {
    "audio_file": audio_file,
    "language": info.language,
    "segments": []
}

for segment in segments:
    data["segments"].append({
        "start": segment.start,
        "end": segment.end,
        "text": segment.text
    })

# Save JSON file
with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Transcript saved in transcript.json")
print(info)
with open("segment.json","w",encoding="utf-8") as f:
    json.dump(data["segments"],f,indent=4, ensure_ascii=False)

print("segments saved in segment.json")