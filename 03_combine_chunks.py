import os
import json
import math
n=5
os.makedirs("newjsons",exist_ok=True)
jsons=os.listdir("jsons")
print(jsons)
for file in jsons:
    if file.endswith(".json"):
        with open(f"jsons/{file}","r") as f:
            data=json.load(f)
            new_chunks=[]
            num_chunks=len(data['chunks'])
            num_groups=math.ceil(num_chunks/n)
            
            for i in range(num_groups):
                start_idx=i*n
                end_idx=min((i+1)*n,num_chunks)
                chunk_groups=data['chunks'][start_idx:end_idx]
                new_chunks.append({
                    "number":chunk_groups[0]['number'],
                    "title":chunk_groups[0]['title'],
                    "start":chunk_groups[0]["start"],
                    "end":chunk_groups[-1]["end"],
                    "text":" ".join(c['text'] for c in chunk_groups)  
                })
        
            
            with open(os.path.join("newjsons",file),"w",encoding="utf-8") as f:
                json.dump({"chunks":new_chunks,"full_text":data['full_text']},f,indent=4)