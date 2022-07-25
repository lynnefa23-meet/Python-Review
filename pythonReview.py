def create_youtube_video (title,discription):
	youtube_video = {"Title": title, "Discription": discription, "Likes": 0, "dislikes":0, "Comments":comments={} }

def like (youtube_video):
	if "Likes" in youtube_video: 
		youtube_video["Likes"]+=1

def dislike (youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1

def add_comment (youtube_video, username, comment_text):
	
