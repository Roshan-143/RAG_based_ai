# How to use this RAG AI Teaching assistant on your own data
## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning 01_video_to_audio

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning 02_audio_to_chunks

## Step 4 - Convert the json files to Vectors
Use the file 03_create_embeddings to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM
04_input
Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM

## How to run orderly
1. First run 01_video_to_audio.py then,
2. run 02_audio_to_chunks.py then,
3. run 03_combine_chunks.py then,
4. run 04_create_embeddings.py
5. And at last run 05_input.py
6. After running 05_input.py the agent says ask a question: , then you can type any topic or subtopic taught in that video
## System Architecture
Video Files
     │
     ▼
FFmpeg (Video → Audio)
     │
     ▼
Faster Whisper (Audio → Text + Timestamp)
     │
     ▼
Chunk Processing
     │
     ▼
BGE-M3 Embeddings
     │
     ▼
Cosine Similarity Search
     │
     ▼
Relevant Answer + Video Timestamp

## Project Structure
RAG_BASED_AI
│
├── videos/                # Input video files
├── audios/                # Audio extracted from videos
├── jsons/                 # Initial transcript chunks
├── newjsons/              # Processed / grouped transcript chunks
├── unused/                # Experimental or unused files
│
├── 01_video_to_audio.py    # Convert videos to audio using FFmpeg
├── 02_audio_to_chunks.py   # Transcribe audio using Faster-Whisper
├── 03_combine_chunks.py    # Combine smaller transcript chunks
├── 04_create_embeddings.py # Generate embeddings using BGE-M3
├── 05_input.py             # User query interface for semantic search
│
├── embedding.joblib        # Stored embeddings for similarity search
├── prompt.txt              # Prompt template used for queries
│
└── README.md               # Project documentation