class MediaFile:
    def __init__(self, filename1, filesize1, format1):
        self.file_name = filename1
        self.file_size = filesize1
        self.format = format1

    def getFileName(self):
        return self.file_name
    def setFileName(self, newfilename):
        self.file_name = newfilename

    def getFileSize(self):
        return self.file_size
    def setFileSize(self, newfilesize):
        self.file_size = newfilesize

    def getFormat(self):
        return self.format
    def setFormat(self, newformat):
        self.format = newformat

    def display(self):
        print(f"File Name={self.file_name}\tFile Size={self.file_size}\tFormat={self.format}")


p1 = MediaFile("Song", "5 MB", "MP3")
p2 = MediaFile("Video", "50 MB", "MP4")

print(p1.getFileName())

p1.display()
p2.display()

p2.setFileSize("60 MB")

p2.display()