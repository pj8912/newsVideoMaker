from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
from moviepy.video.fx.all import resize

import PIL

# Define the paths to your images and audio file
image_files = ['/home/jp/news-auto/test/image1.jpg', '/home/jp/news-auto/test/image2.jpg', '/home/jp/news-auto/test/image3.jpg']  # Add paths to your images
audio_file = '/home/jp/news-auto/test/audio.mp3'  # Path to your MP3 file

# Load the audio file
audio = AudioFileClip(audio_file)

# Calculate the duration each image should be displayed
num_images = len(image_files)
image_duration = audio.duration / num_images

# Create a list to hold the individual clips with effects
clips = []

for image_file in image_files:
    # Create an ImageClip for each image
    img_clip = ImageClip(image_file, duration=image_duration)
    
    # Apply slow zoom in effect
    zoom_in_clip = img_clip.resize(lambda t: 1 + 0.1 * t / img_clip.duration)
    
    # Apply slow zoom out effect
    zoom_out_clip = zoom_in_clip.resize(lambda t: 1 + 0.1 * (img_clip.duration - t) / img_clip.duration)
    
    # Add the clip to the list
    clips.append(zoom_out_clip)

# Concatenate the clips
video_clip = concatenate_videoclips(clips)

# Set the audio to the video clip
video_clip = video_clip.set_audio(audio)

# Write the result to a file
output_file = 'output_video.mp4'
video_clip.fps=24

video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
