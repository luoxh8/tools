from DrissionPage import WebPage, ChromiumOptions

# 播放进度 三棱针疗法
co = ChromiumOptions()
co.set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
page = WebPage(chromium_options=co)

page.get("https://xxzpx.91huayi.com/exercise/ExerciseHome/index")
