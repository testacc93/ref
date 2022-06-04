# import twitter
print("inside 1")
consumer_key = '7x1acaIGA45sRffagIPgNplQc'
consumer_sec = 'MNIFleE7GzOGSe9V7Qmj9kP3bM40eVxjA0owEIiNnoCNr0RHz4'
access_token='1383777392221573130-PE6Qnn8pwekel6djp8zQ7Ik1YrfI5i'
access_sec = 'GiWFdmkPvaig4zWxobG3JjLqlkOtQJ059WriM4JUJezGf'
# api = twitter.Api(consumer_key='5SvFyxAo6wo2hyIFSjmfsHDPh', consumer_secret='RMFmYIxpFxlpPvLf9GxVavjJ5TUhD1fcb9ifJRjhsb1olkrQav', access_token_key='953947929978392576-VkLApMyWx2WWSTt1vg9BsyUHFwGHJb5', access_token_secret='58IFF5XYC31fblJLDQrvf3Y8mARtrbJgEQG5qk8tE70n1')
#
# print(twitter.api.Api.GetFollowers())
import tweepy
print("inside 2")
from time import sleep
auth = tweepy.OAuthHandler(consumer_key, consumer_sec)
auth.set_access_token(access_token, access_sec)
data = ['get your first $15 bonus at ',
        'feeling lucky tonight? win some #btc and much more at ','good at sports? test your skills at ',
        'love #UFCFightIsland? place your bets at ','bunch of bonuses, in #btc and many #cryptocurrency. register at ',
        'like to win 0.005 #btc by placing bets in #UCL? get bonus as well only at ',
        'getting $15 level up bonus was never so easy. start at ','get rakeback in #btc #eth and all coins. only at ',
        'over 700 slots to win from. start playing at ', 'over 50 sports to bet on. only at ',
        'maximum level up bonus is $5000 in #btc or any currency. NO KIDDING!!!! check out ',
        'win over $50 in btc every saturday. at ', 'daily 10 min reloads in btc or any currency at ',
        'live #casino has multiple including #blackjack, #baccarat and more. only at ',
        'try your luck once to win #btc. check out ','lost too much in trading? no worries, play and recover at ',
        'this is where I reached 0.25 #btc within a week. only at ','grab the opportunity to win upto 0.005 btc per week only at ',
        'test your sports betting skills. only at ', 'all you need is patience to win #btc. register now at ',
        'put your #casino skills at test. register and get bonus at ', 'with risk comes the reward. get your bonus in any currency only at ',
        'dont let anything stop u. risk once and double $$ only at ',
        'here is how i took 0.0022 btc to 0.25 btc in a week. register at ',
        'all you need is patience in order to win btc. here --> ','get the taste of winning in a #casino by playin from home. only at ',
        'saved enough? wish to double it instantly with small risk? ', 'got ballz to win big? register at ',
        'feeling lucky tonight? u can win up to 0.005 btc only at ', 'Figuring out an easy way to win #btc? here it is ',
        'get level up bonus of upto $50 only at ', 'double your money instantly only at ','sports betting? only at ',
        'play from over a ton of slots only at ', 'choose from over a ton of sports to be bet on ',
        'weekly and daily bonus, thats right!! DAILY BONUS only at ', 'not only daily and weekly bonuses, we got monthly too. At ',
        'Win and invest any currency you like. only at ','redeem bonus in the currency of your choice at ',
        'i usually play blackjack. it took me to 0.25 #btc in a week. try ur luck at ',

        ]
hash_tags = '#cryptocurrency #crypto #casino #bitcoin #blackjack #btc #gambling #betting #cryptocurrencies #invest #cryptonews #bitcoincash #litecoin #eth'
link = ' https://stake.com/?c=b980983c1a   '
print("inside 3")
import datetime
api = tweepy.API(auth)
for j in range(0, 10000):
    for items in data:
        
        tweet = items + link + hash_tags + str(datetime.datetime.now())
        print(len(tweet))
        sleep(600)
        

        if len(tweet) < 280:
            print(tweet)
            try:
                if "win" in items.lower():
                    media = api.update_status(tweet)
                    continue
                if "slots" in items.lower():
                    media = api.update_status(tweet)
                    continue
                if "sports" or "Sports" in items.lower():
                    media = api.update_status(tweet)
                    continue
                if "bonuses" or "reload" or "bonus" in items.lower():
                    media_1 = api.media_upload("vid.gif")
                    media = api.update_status(tweet)
                    continue
                if "#casino" or "#casinos" in items.lower():
                    media = api.update_status(tweet)
                    continue
                media = api.update_status(tweet)

            except:
                pass
        
