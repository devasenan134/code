from instabot import Bot
from time import sleep
from random import randint

username = "devasenan134"
passwd = "Dev@9629113249"

bot = Bot()
bot.login(username = username, password = passwd)
#non_followers = set(bot.following) - set(bot.followers)
non_followers = bot.save_unfollowers_info_file()

'''
for non_follower in non_followers:
	print(non_follower)
	try:
		bot.unfollow(non_followers)
		sleep(randint(6,12))
	except Exception as e:
		print(e)
		sleep(randint(30,300))
	'''
