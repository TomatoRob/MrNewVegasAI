from elevenlabslib.helpers import *
from elevenlabslib import *
import shutil

user = ElevenLabsUser("a5e789c201bf0a31de9489e0b8a97fcf")
voice = user.get_voices_by_name("Mr New Vegas")[0]

print("Conversion started...")

storiesFromFile = []

print("reading file...")
with open('stories.txt') as my_file:
    for line in my_file:
        storiesFromFile.append(line)

print("file read...")
i = 1
for story in storiesFromFile:
    print("Generating sound clip...")
    audioData = voice.generate_and_play_audio(story,playInBackground=False)
    print("sound clip generated...")
    print("saving clip...")
    clipName = "mnvclip" + str(i) + ".mp3"
    save_audio_bytes(audioData, clipName, outputFormat="mp3")
    i = i+1

