import os
import instaloader

username = input("Username:")
password = input("Password:")

os.system("instaloader --login " + username + " instaloader --password " + password)

instagram = instaloader.Instaloader()

instagram.load_session_from_file(username)

profile = instaloader.Profile.from_username(instagram.context, username)

followers = profile.get_followers()
followees = profile.get_followees()

followersList = list()
followeesList = list()


for i in followees:
    followeesList.append(i.username)

for j in followers:
    followersList.append(j.username)

number = 0

for i in followeesList:
    if i not in followersList:
        print(i, "does not follow you!")

