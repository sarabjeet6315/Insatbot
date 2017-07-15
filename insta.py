import requests,urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as py
from termcolor import colored

APP_ACCESS_TOKEN = '2265640628.5457f9b.fa0b73c4dd3e40c68dd638225822ef20'
BASE_URL = 'https://api.instagram.com/v1/'

                #Access Tokken= Sarabjeets45
                #Users in a Sandbox= ls211998,samanskull

        # Here Function self_info is used to  get's your own details

def self_info():
   request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
   print 'GET request url : %s' % (request_url)
   user_info = requests.get(request_url).json()
   if user_info['meta']['code'] == 200:
     if len(user_info['data']):
       print 'Username: %s' % (user_info['data']['username'])
       print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
       print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
       print 'No. of posts: %s' % (user_info['data']['counts']['media'])
     else:
      print 'User does not exist!'
   else:
      print 'Status code other than 200 received!'

        # Here Function is used to get's the ID of user by username

def get_user_id(insta_username):
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      return user_info['data'][0]['id']
    else:
      return None
  else:
    print 'Status code other than 200 received!'
    exit()

        # Here Function is used to get the user info by username

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'

        # Here Function is used to get the own recent post

def get_own_post():
  request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  own_media = requests.get(request_url).json()
  if own_media['meta']['code'] == 200:
     if len(own_media['data']):
         image_name = own_media['data'][0]['id'] + '.jpeg'
         image_url = own_media['data'][0]['images']['standard_resolution']['url']
         urllib.urlretrieve(image_url, image_name)
         print 'Your Image Has Been Start Downloading......'
         print 'Downloading Complete'
         return own_media['data'][0]['id']
     else:
            print 'Post does not exist!'
  else:
     print 'Status code other than 200 received!'

        # Here Function is used to get the recent post of user by username
        # And Download the post of the user

def get_user_post(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print 'User Does Not Exit'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
      if len(user_media['data']):
         image_name=user_media['data'][0]['id'] +'.jpeg'
         image_url=user_media['data'][0]['images']['standard_resolution']['url']
         urllib.urlretrieve(image_url,image_name)
         print 'Your Image Has Been Start Downloading......'
         print 'Downloading Complete'
      else:
          print 'Exit'
    else:
       print "Status code other than 200 received!"

         #Here Function is used to get the ID of the recent post of a user by username

def post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()

        # Here Function is used to Like the post of user by username

def like_a_post(insta_username):
    media_id=post_id(insta_username)
    request_url=(BASE_URL+'media/%s/likes')%(media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful'
    else:
        print 'Please Try Again'

        # Here Function is used to Post a comment on a user post by username

def post_a_comment(insta_username):
    media_id = post_id(insta_username)
    comment_text = raw_input("Write comment")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)
    make_comment = requests.post(request_url, payload).json()
    if make_comment['meta']['code'] == 200:
        print "You have commented on a post"
    else:
        print "Your comment was not posted"

        #Here Function is defined to get comment list from the user post

def get_user_comments(insta_username):
    media_id=post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    print user_info
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
           pos=1
           for i in user_info['data']:
               print "%d. %s : %s"%(pos,i['from']['username'],i['text'])
               pos=pos+1
           else:
               print "There is no  comments"
    else:
        print 'Status code other than 200 received!'

        # Here Function is used to compare positive and negative comments
        # And draw a pie chart between positive and negative comments

def positive_vs_negative_comments(insta_username):
    media_id = post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
    print comment_info
    if comment_info['meta']['code'] == 200:
        position=1
        pos=0
        neg=0
        if len(comment_info['data']):
           for x in comment_info['data']:
               print "%d.%s :%s"%(position,x['from']['username'],x['text'])
               blob=TextBlob(x['text'],analyzer=NaiveBayesAnalyzer())
               print blob.sentiment
               if blob.sentiment.classification=="pos":
                   pos=pos+1
               else :
                   neg=neg+1
               position=position+1
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'
    labels = '+ve comments', '-ve comments'
    sizes = [pos,neg]
    colors = ['blue', 'red']
    py.pie(sizes,labels=labels,colors=colors)
    py.axis('equal')

        # Here Function is used to give a menu choice to the user to perform different operation

def start_bot():
    while True:
        print '\n'
        print colored('Welcome to Instabot','red')
        print colored('Menu choice:','red')
        print colored("1.Get your own details",'blue')
        print colored("2.Get details of a user by username(ls211998,samanskull)",'blue')
        print colored("3.Get your own recent post",'blue')
        print colored("4.Get the recent post of a user by username",'blue')
        print colored("5.Like the post of user",'blue')
        print colored("6.Comment on a post of user",'blue')
        print colored("7.Get the comments list",'blue')
        print colored("8.To Draw a Piechart between Positive & Negative Comments",'blue')
        print colored("9.Exit",'blue')
        choice = raw_input("Enter you choice: ")
        if choice == "1":
            self_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "5":
            insta_username=raw_input("Enter the username of the user")
            like_a_post(insta_username)
        elif choice=="6":
            insta_username=raw_input("Enter the username of the user")
            post_a_comment(insta_username)
        elif choice =="7":
            insta_username = raw_input("Enter the user name of the user")
            get_user_comments(insta_username)
        elif choice=="8":
            insta_username = raw_input("Enter the user name of the user")
            positive_vs_negative_comments(insta_username)
            py.show(insta_username)
        elif choice=="9":
            exit()
        else:
            print "wrong choice"
start_bot()