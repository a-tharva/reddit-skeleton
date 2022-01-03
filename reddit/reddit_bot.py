import praw
import time
import os

def bot_login():
    print('Logging in ...')
    reddit = praw.Reddit('commentbot', user_agent = "comment responder v0.1")
    print(f'Logged in as {reddit.user.me()}')
    
    return reddit
    
    
def run_bot(reddit, comments_replied_to):
    print('Running bot...')
    
    for comment in r.subreddit('test').comments(limit=25): # enter the subreddit you want to use your bot on and limit to check comments
        if "key_word" in comment.body and comment.id not in comments_replied_to and not comment.author == r.user.me(): # enter keyword you want to reply to
            print("String with key_word found in comment" + comment.id)
            comment.reply('reply')  # reply to key_word
            print('Repplied to comment' + comment.id)
            
            comments_replied_to.append(comment.id)
            
            with open("comments_replied_to.txt", "a") as f:
                f.write(comments.id + "\n")
            
    print(comments_replied_to)
    
    print('Sleeping for 10 seconds...')
    #sleep for 10 seconds...
    time.sleep(10)

    
def get_saved_comments():
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
        
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)
        
    return comments_replied_to
    
    

def main():
    reddit = bot_login()    
    comments_replied_to = get_saved_comments()
    print(comments_replied_to)
    while True:
        run_bot(reddit, comments_replied_to)
    
if __name__ == '__main__':
    main()