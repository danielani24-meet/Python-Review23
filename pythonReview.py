def create_youtube_video(title, description):
	video = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}, "hashtag":[]}
	return video

def like(video):
	if "likes" in video:
		video["likes"] = video["likes"] + 1
	return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"] = video["dislikes"] + 1
	return video

def add_comment(youtubevideo, username, comment_text):
	#comment = {"youtubevideo": video, "username": username, "comment_text": comment_text}
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

#def add_hashtag(username)

for i in range(2):	
	title = input("what's the video's title?")
	description = input("what's the video's description?")
	youtube_video = create_youtube_video(title, description)
	#print(youtube_video)

	youtube_video = like(youtube_video)
	youtube_video = dislike(youtube_video)

	username = input("enter username")
	comments = input("enter comments")
	youtube_video = add_comment(youtube_video, username, comments)

	print(youtube_video)

	for i in range(495):
		youtube_video["likes"] = youtube_video["likes"] + 1
		print(youtube_video["likes"])
	return video

#bonus:
for i in range(5):
	add_hashtag = input("enter your hashtag: ")
	youtube_video["hashtag"].append(add_hashtag)
print(youtube_video)

def similarity_to_video()







