from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
comm_arr = []
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=8xJgXs8AaOs', sort_by=SORT_BY_POPULAR)
for comment in islice(comments, 10):
    comm_arr.append(comment['text'])


print(comm_arr, "\n")