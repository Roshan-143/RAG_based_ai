import requests
import os
import pandas as pd
import json
import joblib

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
        })
    embedding=r.json()['embeddings']
    return embedding
my_dict=[]
chunk_id=0
jsons=os.listdir("newjsons")
for json_file in jsons:
    with open(f"newjsons/{json_file}","r") as f:
        content=json.load(f)
    print(f"creating embedding for {json_file}")
    embedding=create_embedding([c["text"] for c in content["chunks"]])
    for i,chunk in enumerate(content["chunks"]):
        chunk["embedding"]=embedding[i]
        chunk["chunk_id"]=chunk_id
        chunk_id +=1
        my_dict.append(chunk)

df=pd.DataFrame.from_records(my_dict)
# with open("embedd.json","w") as f:
#     json.dump(my_dict,f,indent=4)
# print("successfully saved my_dict")
joblib.dump(df,"embedding.joblib")
print(df)
# a=create_embedding(["cat sat on mat","Soham bought mat from market."])
# print(a[:1])
