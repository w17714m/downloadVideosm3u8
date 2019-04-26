import requests
import sys
from bs4 import BeautifulSoup
import re
HEADERS_CONTEND = {
    "Host": "linuxacademy.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Referer": "https://linuxacademy.com/cp/modules/view/id/300",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9",
    "Cookie": "PHPSESSID=sa95b75a7gu9345rfktaugnb84; _gcl_au=1.1.654312592.1556141131; _ga=GA1.2.979344916.1556141132; _gid=GA1.2.515612036.1556141132; slireg=https://scout.us1.salesloft.com; sliguid=392a80f2-3ede-4155-9e53-87a15e7cd182; slirequested=true; hblid=JOSVpinvHn9ybRXG5r6LC0U3aA66r6BB; _okdetect=%7B%22token%22%3A%2215561411495570%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22linuxacademy.com%22%7D; optin=1; olfsk=olfsk9933179598267177; _ok=8636-122-10-6535; contentbox=1; gaCookie=GA1.2.2083270070.1556141154; intercom-id-c3zuyhmd=c7a87222-1f10-46f7-bb10-f2abf6891593; hubspotutk=96799b0beb13e722fc75b618a1ea9d3d; __hssrc=1; visitor_id700003=6802818; visitor_id700003-hash=519b56337f3f5eb1934f429596fa867be967ef61abe7b97abe03c7f75e04dd60a92000df564977e4cd4b2b84fe17ea03940f9fe6; km_ai=5K0XZw8QpsOlDWy11JSciS6PayE%3D; km_lv=x; __hstc=261081106.96799b0beb13e722fc75b618a1ea9d3d.1556201175094.1556211014881.1556231711931.3; altSiteDirection=primary; wcsid=vPvsh9JIAtvBuJY15r6LC0U33jVbB6A6; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1556313900621%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _oklv=1556313905519%2CvPvsh9JIAtvBuJY15r6LC0U33jVbB6A6; km_vs=1; intercom-session-c3zuyhmd=ZzFVNFdiYmdEZTdNVitEZUdGTkcwdU1vMFRONTFFUVRhQmxtdmdvaERuMG81R3pwcTZuTUMvOFYxZlRHNTRMbS0tdFQyRFJ1eVNzNU9aQnA3a3dCRE9WZz09--c36969d846b6513db78c37e0c0510bbde9c300fa; kvcd=1556314015721"
}

URL_ROOT = "https://linuxacademy.com/"

class DownloadContain:
    html = None
    titles = None
    header = None
    urls = None
    all_tags = None
    structure_links = []

    def __init__(self):
        return

    def downloadContain(self, path_course):
        r = requests.get(path_course, headers=HEADERS_CONTEND, verify=False)
        html = r.text

        soup = BeautifulSoup(html, "html.parser")

        self.titles = soup.select("#syllabus > .syllabus-section-title")
        self.header = soup.select("#syllabus > .syllabus-section-header")
        self.urls = soup.select("#syllabus > a")
        self.all_tags = soup.select("#syllabus")

        tags = self.all_tags[0].contents
        cont = 0
        for i in range(len(tags)):
            temp = tags[i]
            if self.contain_tag(temp, self.titles):
                self.structure_links.append({"pos": cont, "type": "title", "tag": temp.text})
                cont += 1
            if self.contain_tag(temp, self.header):
                self.structure_links.append({"pos": cont, "type": "header", "tag": temp.text})
                cont += 1
            if self.contain_tag(temp, self.urls):
                if 'href' in temp.attrs:
                    urlresult = self.get_url_m3u8(temp.attrs['href'])
                    self.structure_links.append({"pos": cont, "type": "url", "tag": temp.attrs['href'], "m3u8": str(urlresult)})
                    cont += 1
        return self.structure_links

    def contain_tag(self, tag, listObject):
        for t in range(len(listObject)):
            if str(tag) == str(listObject[t]):
                return True
        return False

    def get_url_m3u8(self, url):
        r = requests.get(str(URL_ROOT) + str(url), headers=HEADERS_CONTEND, verify=False)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        result = ""
        if re.findall("[\'].+m3u8+.*[\']", soup.text):
            result = str(re.findall("[\'].+m3u8+.*[\']", soup.text)[0]).replace("\'", "")
        return result