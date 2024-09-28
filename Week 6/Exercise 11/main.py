"""Entry point to zServer."""
from zServerFramework import Template, startServer

TEMPLATE_HTML = """\
<!DOCTYPE HTML>

<html lang="en-US">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="{name}">
        <title>{name}'s personal webpage</title>
    </head>
    
    <body>
        <main>
            <h1>Welcome to {name}'s webpage</h1>
            
            <p>
                {content}
            </p>
        </main>
    </body>
</html>
"""

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    description = input("Describe yourself: ")
    
    template = Template(TEMPLATE_HTML)
    context = {
        'name': user_name,
        'content': description,
    }
    
    rendered_template = template.render(context)
     
    # Start web server
    startServer(rendered_template)