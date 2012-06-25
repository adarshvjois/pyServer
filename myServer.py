import threading
#import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import re
import shelve

FILE = "Web-Content/my_index.html"
PORT = 8008

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        """Handles request sent via post method.."""
        length = int(self.headers.getheader("content-length"))
        data_string = self.rfile.read(length)
        headers = self.headers
        path = self.path
        print "\n\n\n\n**********New Request***********"
        print str(headers)
        print path
        ind=path.find('=')
        method_name=path[ind+1:]
        print method_name

        try:
            result = self.globals()[method_name]()
            print "result"+result+"\n"
        except Exception as e:
            print   str(e)
            result = 'error'
        
        self.wfile.write(data_string)


    def search_for_user():
        print "hi\n"
        return 'success'

def start_server():
	server_address = ("",PORT)

	server = BaseHTTPServer.HTTPServer(server_address,TestHandler)
	server.serve_forever()

def load_db():
    exaile_db = shelve.open("/home/adarsh/.local/share/exaile/music.db")
    if exaile_db=={}:
        print("Your Exaile database is not present at its location")
        return -1

"""
def open_browser():
	#Start a browser after waiting for half a second.
	def _open_browser():
		webbrowser.open('http://localhost:%s/%s' % (PORT, FILE))
	thread = threading.Timer(0.5, _open_browser)
	thread.start()
"""

if __name__ == "__main__":
	#open_browser()
    load_db()
    start_server()
