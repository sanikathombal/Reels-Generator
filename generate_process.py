# This file looks for new folders inside user and converts them to reel if they are not already converted.
import os
from text_to_audio import text_to_speech_file 
import time 
import subprocess

def text_to_audio(folder):
	print("TTA - ",folder)
	with open(f"user_uploads/{folder}/desc.txt") as f:
		text = f.read()
	print(text,folder)
	text_to_speech_file(text, folder)  # Generate the audio.mp3 from desc.txt but its a paid API so commented out for now.

	# (If you want to use another audio and song then you can just put the audio.mp3 and song.mp3 inside the folder and it will work fine and comment the above line and run in terminal ffmpeg_command.txt command with the folder name you want to convert to reel another song.mp3 can be put in static/songs folder and change the command accordingly)

def create_reel(folder):
	command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''  # Convert the images and audio.mp3 inside the folder to a reel
	subprocess.run(command, shell=True, check=True)

	print("CR - ", folder)

if __name__ == "__main__":
	while True:
		print("Processing queue...")
		with open("done.txt", "r")as f:
			done_folders = f.readlines()
			
		done_folders = [f.strip() for f in done_folders]  # Clean up the list
		folders = os.listdir("user_uploads")	
		for folder in folders:
			if(folder not in done_folders):		
				text_to_audio(folder)   # Generate the audio.mp33 from desc.txt
				create_reel(folder)     # Convert the images and audio.mp3 inside the folder to a reel
				with open("done.txt", "a") as f:
					f.write(folder + "\n")

		time.sleep(4)  # Sleep for 4 seconds before checking again
