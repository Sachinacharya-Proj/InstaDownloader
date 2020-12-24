import subprocess

profile_name = "shirley_setia_lover_boy_"
subprocess.run(f"instaloader --login profile {profile_name} -V --no-captions --no-metadata-json --no-compress-json", shell=True)
subprocess.run('cls', shell=True)
print("Downloaded....")