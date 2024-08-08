#!/usr/bin/env python3
import sys
import string

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Strip extra whitespace
    text = ' '.join(text.split())
    return text

for line in sys.stdin:
    fields = line.strip().split(',')
    
    # Assuming the CSV structure: title,tag,artist,year,views,features,lyrics,id
    if len(fields) < 2:
        continue
    
    title = fields[0]
    tag = fields[1]
    
    if tag == 'pop':
        title = preprocess_text(title)
        words = title.split()
        for word in words:
            print(f"{word}\t1")