from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
comm_arr = ''
comments = downloader.get_comments_from_url('https://youtu.be/ya0Qs0ii7LE?si=s7GbA_Fp77rLk4Nx', sort_by=SORT_BY_POPULAR)
for comment in islice(comments, 5000):
    comm_arr += comment['text'] + '; '
    print(comment['cid'])

print(comm_arr, "\n")

with open('s7GbA_Fp77rLk4Nx.txt', 'w') as f:
    f.write(comm_arr)