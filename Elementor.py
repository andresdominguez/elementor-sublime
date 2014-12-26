import sublime, sublime_plugin
import urllib
import urllib2
import threading
import json


class ElementorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """Starting point for the plugin"""
        selections = []
        sels = self.view.sel()
        for sel in sels:
            selections.append(self.view.substr(sel))

        threads = []
        for sel in sels:
            string = self.view.substr(sel)
            thread = ElementorCall(sel, string, 5)
            threads.append(thread)
            thread.start()

        self.handle_threads(threads)

    def handle_threads(self, threads):
        next_threads = []
        for thread in threads:
            if thread.is_alive():
                next_threads.append(thread)
                continue
            if thread.result == False:
                continue
            offset = self.show_results(thread)
        threads = next_threads

        if len(threads):
            sublime.set_timeout(lambda: self.handle_threads(threads), 100)
            return

    def show_results(self, thread):
        """Show the results of the element explorer HTTP request"""
        if thread.result:
            json_result = json.loads(thread.result)
            if json_result['results']:
                results = json_result['results']
                response = ''
                for key, value in results.items():
                    response = '%s: %s' % (key, value)
                print response
                sublime.status_message(response)


class ElementorCall(threading.Thread):
    def __init__(self, sel, selectedText, timeout):
        self.sel = sel
        self.selectedText = selectedText
        self.timeout = timeout
        self.result = None
        threading.Thread.__init__(self)
        # by.css('div')

    def run(self):
        try:
            data = urllib.urlencode({'popupInput': self.selectedText})
            request = urllib2.Request('http://localhost:13000/testSelector?' + data)
            http_file = urllib2.urlopen(request, timeout=self.timeout)
            self.result = http_file.read()
            return

        except (urllib2.HTTPError) as (e):
            err = '%s: HTTP error %s contacting API' % (__name__, str(e.code))
        except (urllib2.URLError) as (e):
            err = '%s: URL error %s contacting API' % (__name__, str(e.reason))

        sublime.error_message(err)
        self.result = False
