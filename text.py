from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the IP address and port number
ip = "192.168.1.2"  # localhost
port = 8000

# Create a custom request handler by subclassing SimpleHTTPRequestHandler
class CustomRequestHandler(SimpleHTTPRequestHandler):
    # Override the do_GET method to add custom behavior
    def do_GET(self):
        # Check if the requested path is "/"
        if self.path == "/":
            # Set response status code and headers
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # HTML content to be served
            html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demmo Corp</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main>
        <section>
            <nav>
                <ul>
                    <li><a href="#">SHOP</a></li>
                    <li><a href="#">CONTACT</a></li>
                </ul>
            </nav>
            <img src="image1.jpg" alt="Image 1">
            <img src="image1.jpg" alt="Image 2">
            <img src="image1.jpg" alt="Image 3">
            <img src="image1.jpg" alt="Image 3">
        </section>
    </main>
</body>
</html>
             """
            # Send the HTML content as the response
            self.wfile.write(html_content.encode())
        else:
            # If the requested path is not "/", serve files from the directory
            super().do_GET()

# Create an HTTP server with the custom request handler
server = HTTPServer((ip, port), CustomRequestHandler)

# Print a message indicating the server is running
print(f"Server started at http://{ip}:{port}")

# Start the server
server.serve_forever()
