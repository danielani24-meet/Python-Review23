def create_youtube_video(title, description):
	video = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return video

def like(video):
	if "like" in video:
		video["likes"] = video["likes"] + 1

def dislike(video):
	if "dislike" in video:
		video["dislikes"] = video["dislikes"] + 1

def add_comment(youtubevideo, username, comment_text):
	#comment = {"youtubevideo": video, "username": username, "comment_text": comment_text}
	youtubevideo["comment"]["username"] = comments_text
	return youtubevideo

	