import json
import os
import re
from tqdm import tqdm
import wordninja

symbol_json = json.load(open('symbol.json'))

def process_en_text(en_text):
    
    step1_result = re.sub(r'\n', ' ', en_text)
    step2_result = re.sub(r' +', ' ', step1_result)
    cleaned_line = re.sub(r'[^0-9a-zA-Z\s\']', '', step2_result).lower()
    return cleaned_line
def process_kr_text(kr_text):
    
    step1_result = re.sub(r'\n', ' ', kr_text)
    step2_result = re.sub(r' +', ' ', step1_result)
    cleaned_line = re.sub(r'[^0-9a-zA-Z\s가-힣\']', '', step2_result).lower()
    return cleaned_line

def get_initials(gram):
    output = "".join([item[0] for item in gram])

    return output
def get_en_line_from_symbol(symbol_line, en_text):
    n = len(symbol_line[0])
    first = symbol_line[1]
    last = symbol_line[2]
    length = symbol_line[3]
    if n == 1:
        return first
    elif n == 2:
        return first + " " + last
    en_tokens = en_text.split(" ")
    en_tokens = [token for token in en_tokens if len(token)]
    grams = [tuple(en_tokens[i:i+n]) for i, word in enumerate(en_tokens) if word == symbol_line[1]]
    candidates = [gram for gram in grams if gram[-1] == symbol_line[2]]
    candidates = list(set(candidates))
    if len(candidates) == 1:
        return " ".join(candidates[0])
    elif len(candidates) > 1:
        candidate_initials = [get_initials(gram) for gram in candidates]
        for candidate, initial in enumerate(zip(candidates, candidate_initials)):
            if symbol_line[0] == initial:
                return " ".join(candidate)
        
        corpus = en_text.split(first)[1:]
        corpus = [first + " " + item.split("last")[0] + " " + last for item in corpus]
        candidates = [item for item in corpus if abs(len(re.sub(r'[^0-9a-zA-Z\']', '', item)) - length) <= 1]
        candidates = list(set(candidates))
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) > 1:
            for candidate in candidates:
                for initial in symbol_line[0]:
                    if initial not in candidate:
                        break
                if initial in candidate:
                    return candidate
            en_no_space = re.sub(r'[^0-9a-zA-Z\']', '', en_text)
            candidates = [en_no_space[i:i+length] for i in range(len(en_no_space) - length) if "".join(en_no_space[i:i+len(first)]) == first and "".join(en_no_space[i+length-len(last):i+length]) == last]
            try:
                return ' '.join(wordninja.split(candidates[0]))
            except:
                return ""
        else:
            en_no_space = re.sub(r'[^0-9a-zA-Z\']', '', en_text)
            candidates = [en_no_space[i:i+length] for i in range(len(en_no_space) - length) if "".join(en_no_space[i:i+len(first)]) == first and "".join(en_no_space[i+length-len(last):i+length]) == last]
            try:
                return ' '.join(wordninja.split(candidates[0]))
            except:
                return ""
    else:
        corpus = en_text.split(first)[1:]
        corpus = [first + " " + item.split("last")[0] + " " + last for item in corpus]
        candidates = [item for item in corpus if abs(len(re.sub(r'[^0-9a-zA-Z\']', '', item)) - length) <= 1]
        candidates = list(set(candidates))
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) > 1:
            for candidate in candidates:
                for initial in symbol_line[0]:
                    if initial not in candidate:
                        break
                if initial in candidate:
                    return candidate
            en_no_space = re.sub(r'[^0-9a-zA-Z\']', '', en_text)
            candidates = [en_no_space[i:i+length] for i in range(len(en_no_space) - length) if "".join(en_no_space[i:i+len(first)]) == first and "".join(en_no_space[i+length-len(last):i+length]) == last]
            try:
                return ' '.join(wordninja.split(candidates[0]))
            except:
                return ""
        else:
            en_no_space = re.sub(r'[^0-9a-zA-Z\']', '', en_text)
            candidates = [en_no_space[i:i+length] for i in range(len(en_no_space) - length) if "".join(en_no_space[i:i+len(first)]) == first and "".join(en_no_space[i+length-len(last):i+length]) == last]
            try:
                return ' '.join(wordninja.split(candidates[0]))
            except:
                return ""
def get_kr_line_from_symbol(symbol_line, kr_text):
    n = len(symbol_line[0])
    first = symbol_line[1]
    last = symbol_line[2]
    length = symbol_line[3]
    if n == 1:
        return first
    elif n == 2:
        return first + " " + last
    kr_tokens = kr_text.split(" ")
    kr_tokens = [token for token in kr_tokens if len(token)]
    grams = [tuple(kr_tokens[i:i+n]) for i, word in enumerate(kr_tokens) if word == symbol_line[1]]
    candidates = [gram for gram in grams if gram[-1] == symbol_line[2]]
    candidates = list(set(candidates))
    if len(candidates) == 1:
        return " ".join(candidates[0])
    elif len(candidates) > 1:
        candidate_initials = [get_initials(gram) for gram in candidates]
        for candidate, initial in enumerate(zip(candidates, candidate_initials)):
            if symbol_line[0] == initial:
                return " ".join(candidate)
        
        corpus = kr_text.split(first)[1:]
        corpus = [first + " " + item.split("last")[0] + " " + last for item in corpus]
        candidates = [item for item in corpus if abs(len(re.sub(r'[^0-9a-zA-Z\']', '', item)) - length) <= 1]
        candidates = list(set(candidates))
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) > 1:
            for candidate in candidates:
                for initial in symbol_line[0]:
                    if initial not in candidate:
                        break
                if initial in candidate:
                    return candidate
            kr_no_space = re.sub(r'[^0-9a-zA-Z가-힣\']', '', kr_text)
            candidates = [kr_no_space[i:i+length] for i in range(len(kr_no_space) - length) if "".join(kr_no_space[i:i+len(first)]) == first and "".join(kr_no_space[i+length-len(last):i+length]) == last]
            try:
                return candidates[0]
            except:
                return ""
        else:
            kr_no_space = re.sub(r'[^0-9a-zA-Z\']', '', kr_text)
            candidates = [kr_no_space[i:i+length] for i in range(len(kr_no_space) - length) if "".join(kr_no_space[i:i+len(first)]) == first and "".join(kr_no_space[i+length-len(last):i+length]) == last]
            try:
                return candidates[0]
            except:
                return ""
    else:
        corpus = kr_text.split(first)[1:]
        corpus = [first + " " + item.split("last")[0] + " " + last for item in corpus]
        candidates = [item for item in corpus if abs(len(re.sub(r'[^0-9a-zA-Z\']', '', item)) - length) <= 1]
        candidates = list(set(candidates))
        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) > 1:
            for candidate in candidates:
                for initial in symbol_line[0]:
                    if initial not in candidate:
                        break
                if initial in candidate:
                    return candidate
            kr_no_space = re.sub(r'[^0-9a-zA-Z\']', '', kr_text)
            candidates = [kr_no_space[i:i+length] for i in range(len(kr_no_space) - length) if "".join(kr_no_space[i:i+len(first)]) == first and "".join(kr_no_space[i+length-len(last):i+length]) == last]
            try:
                return ' '.join(wordninja.split(candidates[0]))
            except:
                return ""
        else:
            kr_no_space = re.sub(r'[^0-9a-zA-Z\']', '', kr_text)
            candidates = [kr_no_space[i:i+length] for i in range(len(kr_no_space) - length) if "".join(kr_no_space[i:i+len(first)]) == first and "".join(kr_no_space[i+length-len(last):i+length]) == last]
            try:
                return ' '.join(wordninja.split(candidates[0]))
            except:
                return ""
count = 0
lyrics_json = {}
for lid in tqdm(symbol_json):
    count +=1
    item = symbol_json[lid]
    
    if os.path.exists('./processed_lyrics/' + lid + 'kr.txt'):
        continue
    else:
        with open('./unprocessed_lyrics/' + lid + 'kr.txt', 'r') as file:
            kr_text = file.read()
    kr_text = process_kr_text(kr_text)
    kr_symbol_splits = item['kr']
    kr_split_lists = [[get_kr_line_from_symbol(line, kr_text) for line in section] for section in kr_symbol_splits]
    
    if os.path.exists('./processed_lyrics/' + lid + 'en.txt'):
        with open('./processed_lyrics/' + lid + 'en.txt', 'r') as file:
            file_contents = file.read()
        sections = file_contents.split("\n\n")
        en_split_lists = [section.split("\n") for section in sections]
    
        
    else:
        with open('./unprocessed_lyrics/' + lid + 'en.txt', 'r') as file:
            en_text = file.read()
        en_text = process_en_text(en_text)
        en_symbol_splits = item['en']
        en_split_lists = [[get_en_line_from_symbol(line, en_text) for line in section] for section in en_symbol_splits]
    
    
    aligned_lyrics = [[(kr_line, en_line) for kr_line, en_line in zip(kr_section, en_section) if len(kr_line) and len(en_line)] for kr_section, en_section in zip(kr_split_lists, en_split_lists)]
    aligned_lyrics = [lyrics for lyrics in aligned_lyrics if len(lyrics)]
    lyrics_json[lid] = aligned_lyrics
    
with open('lyrics.json', 'w') as json_file:
    json.dump(lyrics_json, json_file)
