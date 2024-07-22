from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
comm_arr = ''
comments = downloader.get_comments_from_url('https://youtu.be/ya0Qs0ii7LE?si=qhvea43XPaI', sort_by=SORT_BY_POPULAR)
for comment in islice(comments, 2000):
    comm_arr += comment['text'] + '; '
    print(comment['cid'])

print(comm_arr, "\n")

with open('temp.txt', 'w',  encoding='utf-8') as f:
    f.write(comm_arr)