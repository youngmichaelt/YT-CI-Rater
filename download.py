from __future__ import unicode_literals
import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
from os import path
import speech_recognition as sr
import os

class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def download_captions(code, title):
    # code = "ChCJmbW2d_8"
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(code)
        print(transcript_list)
        srt = YouTubeTranscriptApi.get_transcript(code, languages=['zh-Hans'])
        print(srt)
        sentences = []
        for x in srt:
            sentences.append(x['text'])

        f = open("/Users/mac/Desktop/repos/temp-YT-CI/text_files/" + title +".txt", "w")
        for sentence in sentences:
            for x in sentence.split():
                f.write(x)
        f.close()
                

    except:
        download_wav(code)
    


def download_wav(code):
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
            
        }],
        'outtmpl': '/Users/mac/Desktop/repos/temp-YT-CI/temp_wav/%(title)s.%(ext)s'
        # 'no_check_certificate': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v='+code])
    
    recognize('/Users/mac/Desktop/repos/temp-YT-CI/')


def recognize(file_path):
    r = sr.Recognizer()
    wav_file_path = file_path + "temp_wav/"
    text_file_path = file_path + "text_files/"

    wav_files = []


    for file in os.listdir(wav_file_path):
        wav_files.append(file)

    for file in wav_files:
        if file.split('.')[1] == "wav":
            with sr.AudioFile(wav_file_path + file) as source:
                audio = r.record(source)  
            result = r.recognize_google(audio, language = 'zh').lower()

            print(result)
            f = open(text_file_path + file.split('.')[0]+".txt", "w")
            f.writelines(result)
            f.close()
            os.replace(wav_file_path + file, file_path + "wav_files/" + file)

        else:
            print("Not a WAV file...")

if __name__ == "__main__":
    download_captions("ck8Sq8qo9dY", "Comprehensible Input Chinese - Slow & Clear | How Chinese Parents Show Love | Hit Chinese TPRS")
    # recognize('/Users/mac/Desktop/repos/temp-YT-CI/')
    # download_wav("oaA5N6Wso_o")

