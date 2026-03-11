import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from faster_whisper import WhisperModel
import json
os.makedirs("jsons", exist_ok=True)
audios=os.listdir("audios")
model=WhisperModel("small",compute_type="int8")
for audio in audios:
    # print(audio)
    segments,info=model.transcribe(
        f"audios/{audio}",
        language="hi",
        task="translate"
        )
    number=audio.split("_")[0]
    title=audio.split("_")[1][:-4]
    chunks=[]
    full_text=""
    for segment in segments:
        chunks.append({
            "number":number,
            "title":title,
            "start":segment.start,
            "end":segment.end,
            "text":segment.text
        })
        full_text +=segment.text.strip()+" "

    chunks_with_metadata={
        "chunks":chunks,
        "full_text":full_text
    }
    with open(f"jsons/{number}_{title}.json","w",encoding="utf-8") as f:
        json.dump(chunks_with_metadata,f,indent=4, ensure_ascii=False)