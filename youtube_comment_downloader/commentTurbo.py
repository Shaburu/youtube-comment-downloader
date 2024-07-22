
from youtube_comment_downloader import YoutubeCommentDownloader
import time
from multiprocessing import Pool, cpu_count

def fetch_comments(comment_url, start_index, end_index):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(comment_url)
    return comments[start_index:end_index]

def download_comments_parallel(url):
    downloader = YoutubeCommentDownloader()
    all_comments = list(downloader.get_comments_from_url(url))
    total_comments = len(all_comments)
    num_chunks = cpu_count()
    chunk_size = total_comments // num_chunks

    indices = [(i * chunk_size, (i+1) * chunk_size) for i in range(num_chunks)]
    if total_comments % num_chunks != 0:
        indices[-1] = (indices[-1][0], total_comments)  # Make sure the last chunk contains the remainder

    with Pool(num_chunks) as pool:
        results = pool.starmap(fetch_comments, [(url, start, end) for start, end in indices])

    comm_arr = ''
    comment_count = 0
    for chunk in results:
        for comment in chunk:
            comm_arr += comment['text'] + '; '
            print(comment['cid'])
            comment_count += 1

    print(comment_count)

    with open('temp2.txt', 'w', encoding='utf-8') as f:
        f.write(comm_arr)

if __name__ == "__main__":
    start_time = time.time()
    download_comments_parallel('https://www.youtube.com/watch?v=_9b1G0Ivaas')
    print("Duration with multiprocessing Pool:", time.time() - start_time)