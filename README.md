# youtube-embedding
This code generates transformer large-language model embeddings for youtube video descriptions and transcripts.

To use this code, retrieve the video ID (everything in the link after "watch?v=" from the video that you want to get embeddings for, and replace the value in the quotations on line 30 of GetTranscripts.py with your video ID. Note that videos cannot be private.
Next, run GetTranscripts.py, which will put the video's description and transcript into a file called "test.txt".
Lastly, run Embeddings.ipynb with "test.txt" set for the variable "file". The embeddings will be stored in the dictionary "embeddings" with the key "1".

The code can easily be altered to loop through a list of videos and generate embeddings for each one, if that is the preferable format.
