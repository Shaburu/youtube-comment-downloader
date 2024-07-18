from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
comm_arr = ''
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=nllZrOoxpzc', sort_by=SORT_BY_POPULAR)
for comment in islice(comments, 5000):
    comm_arr += comment['text'] + '; '
    print(comment['cid'])

print(comm_arr, "\n")

with open("commentDump.txt") as f:
    f.write(comm_arr)