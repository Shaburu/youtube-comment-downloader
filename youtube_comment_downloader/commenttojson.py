from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
comm_arr = ''
comment_count = 0
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=nllZrOoxpzc')
for comment in comments:
    comm_arr += comment['text'] + '; '
    print(comment['cid'])
    comment_count += 1

print(comment_count)

with open('aluxTop_nllZrOoxpzc.txt', 'w', encoding='utf-8') as f:
    f.write(comm_arr)