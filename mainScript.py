import os, instaloader, subprocess

permissionAsk = input('Wanna a Download Videos to (Y/N)(Default: N)=>> ')
permissionAsk = permissionAsk.lower()

permissionCode = 0

if permissionAsk == 'y':
    permissionCode = 1
elif permissionAsk == 'n':
    permissionCode = 0
else:
    permissionCode = 0

profile_name = input("Enter username: ")
modelImage = instaloader.Instaloader()

modelImage.download_profile(profile_name, profile_pic=True, profile_pic_only=False, fast_update=True)


dirOpen = os.listdir(profile_name)

for image in dirOpen:
    if image.endswith(".jpg") or image.endswith(".png"):
        pass
    elif image.endswith(".mp4") or image.endswith(".avi"):
        if permissionCode == 0:
            subprocess.run(f'del "{profile_name}\\{image}"', shell=True)
        else:
            pass
    else:
        subprocess.run(f'del "{profile_name}\\{image}"', shell=True)

subprocess.run('cls', shell=True)
print(f'Download Completed and files are stored in Folder {profile_name}')