import pandas as pd
import requests
import os
import json
import joblib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# from 03_read_chunks import create_embedding

# emb=create_embedding(["i am roshan"])
# print(emb)
df=joblib.load("embedding.joblib")
# df=pd.read_json("embedd.json")
# print(df.tail())
def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
        })
    embedding=r.json()['embeddings']
    return embedding

def inference(prompt):
    r=requests.post("http://localhost:11434/api/generate",json={
        "model": "llama3",
        "prompt":prompt,
        "stream": False
        })
    response=r.json()['response']
    return response
incoming_query=input("Ask a question:")
query_embedding=create_embedding([incoming_query])[0]
# print(query_embedding)
# print(np.vstack(df["embedding"].values))
# print(np.vstack(df["embedding"]).shape)
similarity=cosine_similarity(np.vstack(df["embedding"]),[query_embedding]).flatten()
# print(similarity)
top_results=5
max_indx=similarity.argsort()[::-1][0:top_results]
# print(max_indx)
new_df=df.loc[max_indx].sort_values("start")
# print(new_df[["number","title","text"]])
context=new_df[["title","number","start","end","text"]].to_string(index=False)

prompt=f"""
I am learning web development using Sigma Web Development course.

These are subtitle chunks from the course videos:

{context}

------------------------------------------------

User Question: "{incoming_query}"

Instructions:
1. Tell in which video the topic is explained.
2. Mention all timestamps clearly.
3. If multiple chunks belong to the same video, combine them.
4. Guide the user where to watch.

If the question is unrelated, say you can only answer questions related to the course videos.
"""
with open("prompt.txt","w") as f:
    f.write(prompt)
# print(new_df['embedding'])
response=inference(prompt)
print(response)
# for index,item in new_df.iterrows():
#     print(index,item["number"],item["start"],item["end"],item["title"],item["text"])