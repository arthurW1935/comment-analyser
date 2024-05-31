from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
video_url = 'https://www.youtube.com/watch?v=kffacxfA7G4'
comments = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_POPULAR)

with(open('comments.txt', 'w',  encoding='utf-8')) as f:
    for index,comment in enumerate(comments):
        f.write(f"{index} {comment['text']}\n")

