# coding:utf-8
# !/usr/bin/env python

from pytube import YouTube
from pytube import Playlist


class youtubeDowload():

    def __init__(self):
        self.video = None
        self.url = 'your youtube playlist'

    # start download video
    def download_video(self):
        try:
            self.yt = YouTube(self.url, on_progress_callback=self.show_progress_bar)
            self.video = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution') .desc() .first()
            self.video.download()
        except KeyError:
            print('can not download this link = ' + self.url)
            pass

    # to show percentage when download
    def show_progress_bar(self, stream, chunk, file_handle, bytes_remaining):
        size = self.video.filesize
        progress = (float(abs(bytes_remaining - size) / size)) * float(100)
        print('downloading ' + str(progress) + '%')
        return


if __name__ == '__main__':
    print('start download')
    svc = youtubeDowload()
    svc.download_video()
    print('completed download')
