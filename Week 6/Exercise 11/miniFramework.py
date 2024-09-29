"""Super Simple Web Framework
author: Zowie
license: MIT
"""

import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from typing import Dict, Any

TEMPLATE_404 = """\
<!DOCTYPE HTML>

<html lang="en-US">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>404 Not Found</title>
    </head>
    
    <body>
        <main>
            <h1>404 Error</h1>
            
            <p>
                The page you visited does not exist.
            </p>
        </main>
    </body>
</html>
"""

# I can improve this to make it somehow include it within
# CustomVCLogic. Figuring this out is tricky
# .. due to how the class is consumed by HTTPServer.

# I could also make a static folder for the user to easily
# edit 404 pages and add more templates

# A little too stateful for my liking, but it works for now.
page_data: dict = {}

class CustomVCLogic(BaseHTTPRequestHandler): 
    """Custom view and controller logic to hand off to the webserver."""       
    def do_GET(self) -> None:
        """Handle response to GET requests."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            for line in page_data['page_template'].splitlines():
                print(line)
                self.wfile.write(bytes(line, "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            for line in page_data['error_template'].splitlines():
                print(line)
                self.wfile.write(bytes(line, "utf-8"))
                
    def log_message(self, format: str, *args) -> None:
        """Log an arbitrary message.

        This is used by all other logging functions.  Override
        it if you have specific logging wishes.

        The first argument, FORMAT, is a format string for the
        message to be logged.  If the format string contains
        any % escapes requiring parameters, they should be
        specified as subsequent arguments (it's just like
        printf!).

        The client ip and current date/time are prefixed to
        every message.

        Unicode control characters are replaced with escaped hex
        before writing the output to stderr.

        """
        return
        
        # don't output entire html doc, just the first line
        # print(format.split('\n'))
        
        # message = first_line % args
        # print(message)
        # sys.stderr.write("%s - - [%s] %s\n" %
        #                  (self.address_string(),
        #                   self.log_date_time_string(),
        #                   message.translate(self._control_char_table)))

            
def startServer(page_template: str,
                host_name: str = "localhost",
                server_port: int = 8000,
                error_template: str = TEMPLATE_404) -> None:
    """Start the webserver with the view and controller logic."""
    # page_template is a required arg
    page_data['page_template'] = page_template
    page_data['error_template'] = error_template
    
    server_address = (host_name, server_port)
    webServer = HTTPServer(
        server_address,
        CustomVCLogic
        # lambda *args, **kwargs: CustomWebServer(
        #     *args, page_template=page_template,
        #     error_template=error_template, **kwargs)
    )
    
    print("\nServer started http://%s:%s" % server_address)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    
    print("\nServer stopped.")
            

class Template:
    """Simple template class with rendering."""
    def __init__(self, template: str) -> None:
        self.template = template
    
    def render(self, context: Dict[str, Any]) -> str:
        """Render the template variables with the given context."""
        return self.template.format(
            **context
        )