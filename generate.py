import speech_recognition as sr
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import os

PATH = os.getcwd() + '/test/'

for instance in os.listdir(PATH):
    # Load the video clip and audio clip
    video_clip = VideoFileClip(PATH + instance + "/video.mp4")
    audio_clip = AudioFileClip(PATH + instance + "/instrumental.wav")

    # Set up the speech recognizer and load the audio file
    r = sr.Recognizer()
    with sr.AudioFile(PATH + instance + "/vocals.wav") as source:
        audio = r.record(source)

    # Transcribe the audio file using CMU Sphinx
    transcription = r.recognize_sphinx(audio)

    # Create a TextClip from the transcription
    subtitles = TextClip(transcription, fontsize=24, color='white', bg_color='black')

    # Set the duration of the TextClip to match the duration of the audio clip
    subtitles = subtitles.set_duration(audio_clip.duration)

    # Add the audio and subtitle tracks to the video clip
    final_clip = CompositeVideoClip([video_clip, subtitles.set_pos(('center', 'bottom')), audio_clip])

    # Write the final clip to a file
    final_clip.write_videofile(PATH + instance + "/karaoke.mp4")