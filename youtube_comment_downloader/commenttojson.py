from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
import time

comm_arr = ''
comment_count = 0
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=G8AT01tuyrk')
for comment in comments:
    start_time = time.time()
    comm_arr += comment['text'] + '; '
    print(comment['cid'])
    comment_count += 1

end_time = time.time()

print(comment_count)
print(f'Time taken: {end_time - start_time} seconds')

with open('temp2.txt', 'w', encoding='utf-8') as f:
    f.write(comm_arr)