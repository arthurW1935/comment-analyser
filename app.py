from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()


def get_comments(video_url, n_comments=None):

    comments = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_POPULAR)
    if(n_comments):
        comments = list(islice(comments, n_comments))
    else:
        comments = list(comments)
    return comments