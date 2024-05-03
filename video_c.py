from moviepy.editor import *
import assemblyai as aai
import tempfile


aai.settings.api_key = "4f70d0a2a54e454f90a869173b7a8c48"

# Load the mp4 file
video = VideoFileClip(r"C:\Users\HP\OneDrive\Documents\app\summarizer\summarizer\video_file.mp4")

# Create a temporary file to write the audio
with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
    # Extract audio from video and write to temporary file
    video.audio.write_audiofile(temp_audio_file.name, codec='mp3')

    # Close the file to ensure all data is written
    temp_audio_file.close()

    # Transcribe audio to text
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(temp_audio_file.name)


text_from_audio = transcript.text

print(text_from_audio)