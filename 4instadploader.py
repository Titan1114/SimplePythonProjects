# we can download anyone insta dp using their username with this code.
import instaloader

insta= instaloader.Instaloader()

dp= input("Enter username : ")
insta.download_profile(dp, profile_pic_only=True)
