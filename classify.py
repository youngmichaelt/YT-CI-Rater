import os
from os import path
from pywordseg import *

def create_hsk_dict():
    HSK = os.getcwd() + "/HSK/"
    hsk_dict = {}
    for file in os.listdir(HSK):
        with open(HSK+file) as hsk_file:
            if file == "HSK1.txt":
                hsk_num = 1
            elif file == "HSK2.txt":
                hsk_num = 2
            elif file == "HSK3.txt":
                hsk_num = 3
            elif file == "HSK4.txt":
                hsk_num = 4
            elif file == "HSK5.txt":
                hsk_num = 5
            elif file == "HSK6.txt":
                hsk_num = 6
            else:
                hsk_num = 0

            for line in hsk_file:
                line = line.strip()
                hsk_dict[line] = hsk_num

    print(hsk_dict)
    return hsk_dict

def create_vid_dict(hsk_dict):

    vid_dicts = []
    text_file_paths = '/Users/mac/Desktop/repos/temp-YT-CI/text_files/'
    seg = Wordseg(batch_size=64, embedding='w2v', mode="TW")
    for file in os.listdir(text_file_paths):
        with open(text_file_paths + file) as vid_file:
            vid_dict = {}
            lines = vid_file.readlines()
            lines = [line.rstrip() for line in lines]
            res = seg.cut(lines)
            print(res)
            for char in res[0]:
                
                char = char.strip()

                if char in hsk_dict:
                    vid_dict[char] = hsk_dict[char]
                else: 
                    vid_dict[char] = 0

                    
            vid_dicts.append(vid_dict)
    
    print(vid_dicts)
    return vid_dicts

def scores(vid_dicts):
    scores = {}
    counter = 0
    for vid_dict in vid_dicts:
        for key, value in vid_dict.items():
            if counter in scores:
                scores[counter] += value
            else:
                scores[counter] = value
        counter += 1
    
    print(scores)

    







    pass

if __name__ == "__main__":
    hsk = create_hsk_dict()
    vids = create_vid_dict(hsk)
    scores(vids)