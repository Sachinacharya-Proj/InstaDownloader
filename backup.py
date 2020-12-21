import instaloader
import os
import subprocess

modelImage = instaloader.Instaloader()
profile_name = input('Enter Your Username: ')

modelImage.download_profile(profile_name, profile_pic_only= True)
modelImage.download_profiles(profile_name, profile_pic=True, posts=True, igtv=True, fast_update=True)

# Downloading Images
modelImage.download_profile(profile_name, profile_pic=True, profile_pic_only=False, fast_update=True)

# READING CONTAING DIRECTORY

dirOpen = os.listdir(profile_name)
imageDirCount = 0
videoDirCount = 0


for image in dirOpen:
    if image.endswith(".jpg") or image.endswith(".png"):
        if imageDirCount == 0:
            os.mkdir(f"{profile_name}/Images")
            imageDirCount = 2
        os.system(f"move './{profile_name}/{image}' './{profile_name}/Images/{image}'")
    elif image.endswith(".mp4") or image.endswith(".avi"):
        if videoDirCount == 0:
            os.mkdir(f"{profile_name}/Videos")
            videoDirCount = 2
    else:
        subprocess.run(f'del "{profile_name}\\{image}"', shell=True)
