# coding:utf-8
# !/usr/bin/env python

from pytube import YouTube
from pytube import Playlist


class youtubeDowload():

    def __init__(self):
        self.video = None
        self.url = 'your youtube link'
        self.pl = Playlist(self.url)

    # prepare playlist to download
    def downloadPlaylist(self):
        linkArray = self.getAllLinks()
        i = 0
        for link in linkArray:
            try:
                print('start download ' + link)
                self.downloadVideo(link)
                print('complete download ' + link)
                i += 1
                print('total= ' + str(len(linkArray)) + ', completed= ' +
                      str(i) + ', remaining = ' + str(len(linkArray) - i))
            except IndexError:
                print('can not download this link = ' + self.url)
                pass

    # get all youtube links from playlist to download one by one
    def getAllLinks(self):
        allLinks = []
        youtubeLink = 'https://www.youtube.com'
        for linkprefix in self.pl.parse_links():
            allLinks.append(youtubeLink + linkprefix)
        return allLinks

    # start download video
    def downloadVideo(self, link):
        self.yt = YouTube(link, on_progress_callback=self.show_progress_bar)
        self.video = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution') .desc() .first()
        self.video.download()

    # to show percentage when download
    def show_progress_bar(self, stream, chunk, file_handle, bytes_remaining):
        size = self.video.filesize
        progress = (float(abs(bytes_remaining - size) / size)) * float(100)
        print('downloading ' + str(progress) + '%')
        return


if __name__ == '__main__':
    print('start download playlist')
    svc = youtubeDowload()
    svc.downloadPlaylist()
    print('completed download playlist')
