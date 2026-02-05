import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("EMAIL_USER")
APP_PASSWORD = os.getenv("EMAIL_PASS")

class ContactHandler(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        """Standardizes CORS headers for all responses to prevent browser blocks"""
        # Using '*' for local development flexibility, but match your frontend port if needed
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        """Handles the browser's security preflight request"""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()
        
    def do_POST(self):
        """Processes the contact form submission and sends the email"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))

            # Construct the email
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = SENDER_EMAIL 
            msg['Subject'] = f"New Portfolio Inquiry: {data.get('subject', 'No Subject')}"

            body = f"Name: {data.get('name')}\nEmail: {data.get('email')}\n\nMessage:\n{data.get('message')}"
            msg.attach(MIMEText(body, 'plain'))

            # Secure SMTP Handshake
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls() # Encrypt the connection
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
            server.quit()

            # Success Response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode())

        except Exception as e:
            print(f"Backend Error: {e}")
            # Error Response with CORS headers to ensure the browser sees the actual error
            self.send_response(500)
            self._set_cors_headers()
            self.end_headers()
            response = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=ContactHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Backend listening on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()