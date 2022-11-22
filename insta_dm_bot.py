from time import sleep
from instabot import Bot 

try:
    user_name = str(input("Enter the targeted username:"))
    total_dms = int(input("Enter the number of DMs:"))
except Exception:
    print("Invalid input!")

my_bot = Bot(max_followers_to_follow=500, max_follows_per_day=250) 
a=input("enter username : ")
b=input("enter paasword : ")
#login
my_bot.login(username=a, password=b)

'''#Method 1
#DM the followers of the user
followers_ids = my_bot.get_user_followers("cashapp")
print(followers_ids)

for count, each_follower in enumerate(followers_ids):
    print("follow/dm number", count)
    if count > total_dms:
        break
  #  my_bot.follow(each_follower)
    sleep(5)
    username = my_bot.get_username_from_user_id(each_follower)
    message_text = "Hello "+username+", \n Are you intereted in CashApp Money.? \n You'll learn CashApp unlimited money method, \n Message @PAPAONBEAT on TELEGRAM, \n t.me/papaonbeat, /n https://prnt.sc/CnD1gGm6k3bS"
    my_bot.send_message(message_text, [username]) 
    sleep(10)
    


'''#Method 2
#DM the likers(engaging people) of the user
liker_ids = my_bot.get_user_likers(user_name)

for count, each_liker in enumerate(liker_ids):
    if count > total_dms:
        break
    '''my_bot.follow(each_liker)'''
    sleep(5)
    username = my_bot.get_username_from_user_id(each_liker)
    message_text = "Hello "+username+", \n Are you intereted in CashApp Money.? \n You'll learn CashApp unlimited money method, \n Message @PAPAONBEAT on TELEGRAM, \n t.me/papaonbeat, /n https://prnt.sc/CnD1gGm6k3bS"
    my_bot.send_message(message_text, [username]) 
    sleep(20)


my_bot.logout()

sleep(3600)

