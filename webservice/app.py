import http.server
import socketserver

# Define the request handler
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the response code to 200 (OK)
        self.send_response(200)
        # Set the content type to text/html
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Define the response body
        response_body = "<html><body><h1>Hello, World!</h1></body></html>"
        
        # Write the response body
        self.wfile.write(response_body.encode('utf-8'))

# Define the port for the server
PORT = 8000

# Create the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    # Run the server
    httpd.serve_forever()
