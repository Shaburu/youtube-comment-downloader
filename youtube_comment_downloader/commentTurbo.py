from youtube_comment_downloader import YoutubeCommentDownloader
from multiprocessing import Process, Manager
import time

def download_comments(url, start, end, return_dict, index):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(url)
    comm_arr = ''
    comment_count = 0
    for i, comment in enumerate(comments):
        if i < start:
            continue
        if i >= end:
            break
        comm_arr += comment['text'] + '; '
        comment_count += 1
    return_dict[index] = (comm_arr, comment_count)

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=G8AT01tuyrk'
    num_processes = 4 # Number of processes you want to run
    total_comments_to_fetch = 1005 # Total number of comments to fetch
    comments_per_process = total_comments_to_fetch // num_processes

    manager = Manager()
    return_dict = manager.dict()
    
    processes = []

    start_time = time.time()

    for i in range(num_processes):
        start = i * comments_per_process
        end = (i + 1) * comments_per_process
        proc = Process(target=download_comments, args=(url, start, end, return_dict, i))
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

    combined_comments = ''
    total_comment_count = 0
    for i in range(num_processes):
        combined_comments += return_dict[i][0]
        total_comment_count += return_dict[i][1]

    with open('temp2.txt', 'w', encoding='utf-8') as f:
        f.write(combined_comments)

    end_time = time.time()
    print(f'Total comments fetched: {total_comment_count}')
    print(f'Time taken: {end_time - start_time} seconds')