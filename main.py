import requests
import time
import os
import threading
import http.server
import socketserver
from datetime import datetime

# Custom HTTP server handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Server is running...")

# Start a local server
def execute_server():
    PORT = int(os.environ.get("PORT", 4000))
    while True:  # Server hamesha chalu rahega
        try:
            with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
                print(f"Server running at http://localhost:{PORT}")
                httpd.serve_forever()
        except:
            time.sleep(5)  # Agar koi error aaya toh 5 sec ke baad retry karega

# Read a file safely (Missing file toh bhi script nahi rukegi)
def read_file(filepath):
    try:
        with open(filepath, "r") as file:
            return [line.strip() for line in file.readlines()]
    except:
        return [""]  # File missing toh bhi empty return karega

# Send messages non-stop
def send_messages_from_file():
    while True:  # Yeh loop script ko band nahi hone dega
        convo_id = read_file("convo.txt")[0]  
        messages = read_file("NP.txt")  
        tokens = read_file("tokennum.txt")  
        hatters_names = read_file("hattersname.txt")  
        speed = int(read_file("time.txt")[0]) if read_file("time.txt")[0].isdigit() else 5  

        vikram_name = "\033[1;93m★『VIKRAM K1NG』★\033[0m"  

        message_count = 0  

        while True:  
            for i, message in enumerate(messages):
                token = tokens[i % len(tokens)] if tokens else "INVALID_TOKEN"
                hater_name = hatters_names[i % len(hatters_names)] if hatters_names else "Unknown"
                timestamp = datetime.now().strftime("\033[1;91mTime :- %Y-%m-%d %I:%M:%S %p\033[0m")
                colored_message = f"\033[1;96m{message}\033[0m"  

                full_message = f"{hater_name} {message}"  

                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                response = requests.post(url, json={"access_token": token, "message": full_message})

                message_count += 1  

                # Terminal Log
                print(f"\n🚀 FROM BRANDED KAMEENA VIKRAM ☠️\n{timestamp}")
                print(f"⚔️━━━ {vikram_name} ━━━⚔️")
                if response.ok:
                    print(f"[✔] Sent ({message_count}): {hater_name}: {colored_message}\n")
                else:
                    print(f"[x] Failed ({message_count}): {hater_name}: {colored_message}\n")

                time.sleep(speed)  

# Main function to start server & messaging
def main():
    while True:  # Yeh main loop script ko crash hone nahi dega
        try:
            server_thread = threading.Thread(target=execute_server, daemon=True)
            server_thread.start()
            send_messages_from_file()
        except:
            time.sleep(5)  # 5 sec ke delay ke baad restart karega

if __name__ == "__main__":
    main()
