def create_youtube_video (title,discription):
	youtube_video = {"Title": title, "Discription": discription, "Likes": 0, "dislikes":0, "Comments":{} }
	return youtube_video

def like (youtube_video):
	if "Likes" in youtube_video: 
		youtube_video["Likes"]+=1
		return youtube_video

def dislike (youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1
		return youtube_video

def add_comment(youtube_video, username, comment_text):
					youtube_video["Comments"][username] = comment_text
					return youtube_video

new_video = create_youtube_video("song", "amazing song")
for i in range (495):
	new_video= like(new_video)
	new_video = dislike(new_video)
	new_video = add_comment(new_video, "nice song" ,"oh yes!")
print (new_video)
