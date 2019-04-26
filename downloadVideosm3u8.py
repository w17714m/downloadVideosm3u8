from time import sleep

from web.DownloadContain import DownloadContain
from web.seleniumDownload import SeleniumDownload
from progressbar import *
from util import *
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


sys.stdout.write(banner())
# simulacion download
# items = list(range(0, 57))
# l = len(items)
# pb = ProgressBar()
# pb.printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
# for i, item in enumerate(items):
#     sleep(0.1)
#     pb.printProgressBar(i+1, l, prefix='En progreso:', suffix='Completado', length=50)
# t = SeleniumDownload()
# t.testweb()

d = DownloadContain()
path_course = "https://linuxacademy.com/cp/modules/view/id/300"
print(d.downloadContain(path_course))
