from moviepy.editor import ImageSequenceClip, AudioFileClip

# Define the paths to your images and audio file
image_files = ['/home/jp/news-auto/test/image1.jpg', '/home/jp/news-auto/test/image2.jpg', '/home/jp/news-auto/test/image3.jpg']  # Add paths to your images
audio_file = '/home/jp/news-auto/test/audio.mp3'  # Path to your MP3 file

# Load the audio file
audio = AudioFileClip(audio_file)

# Calculate the duration each image should be displayed
num_images = len(image_files)
image_duration = audio.duration / num_images

# Create the video clip from the image sequence
clip = ImageSequenceClip(image_files, durations=[image_duration] * num_images)

# Set the audio to the clip
clip = clip.set_audio(audio)

# Write the result to a file
output_file = 'output_video.mp4'
clip.fps=24
clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
