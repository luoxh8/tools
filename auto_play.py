import DrissionPage
from DrissionPage import ChromiumOptions

co = ChromiumOptions()
co.set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
co.extensions.clear()
co.set_argument('deviceName', 'iPhone 12 Pro')
page = DrissionPage.WebPage(chromium_options=co)

for _ in range(40):
    page.new_tab(
        'https://gdedu.szqinqi.com/edu/service/course/courseList.ftl?id=20230703092948000711&tid=2c9201c58a35c81b018a4fea549f2922&semester=202403&room_type=90')
