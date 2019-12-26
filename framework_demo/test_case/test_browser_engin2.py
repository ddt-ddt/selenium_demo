from framwork_demo.test1.browser_engine import BrowserEngine

# class TestBrowserEngine(object):
#
#     def open_browser(self):
browserengine = BrowserEngine()
driver = browserengine.get_browser()