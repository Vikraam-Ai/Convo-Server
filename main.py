import logging
import requests
import json
import time
import os
import http.server
import socketserver
import threading
import random  

# Setup logging
#import os

#import os
#import logging

log_path = "log.txt"
max_size = 10 * 1024 * 1024  # 10 MB in bytes

# Check if log file exists, if not create it
if not os.path.exists(log_path):
    with open(log_path, "w") as log_file:
        pass

# Check the size of the log file
if os.path.getsize(log_path) >= max_size:
    try:
        # Delete the log file if it exceeds the size limit
        os.remove(log_path)
        print(f"🗑️ {log_path} deleted as it exceeded {max_size} bytes.")
        
        # Recreate the log file
        with open(log_path, "w") as log_file:
            print(f"🆕 {log_path} recreated.")
        
        # Reinitialize logging to use the new log file
        logging.shutdown()  # Shutdown existing logging configuration
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            filemode="a"
        )
        print(f"🔧 Logging reconfigured to use the new {log_path}.")
    except Exception as e:
        print(f"⚠️ Error handling log file: {e}")
else:
    print(f"✅ {log_path} is within the size limit.")

# Configure logging (initial setup or reconfiguration)
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    filemode="a"
)

# Example logging
logging.info("💬💬💬💬💬✅")

uploads_folder = "uploads"
if not os.path.exists(uploads_folder):
    os.makedirs(uploads_folder)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        message = "🔥👑 Vikram King Server Running... 👑🔥".encode("utf-8")
        self.wfile.write(message)

def execute_server():
    PORT = int(os.environ.get("PORT", 4000))
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        logging.info(f"Server running at http://localhost:{PORT}")
        print(f"\n🚀 Server running at ➜ http://localhost:{PORT}")
        httpd.serve_forever()
def validate_token(access_token):
    """ ✅ Check if the Facebook token is valid """
    url = "https://graph.facebook.com/me?access_token={}".format(access_token)
    response = requests.get(url)

    if response.status_code == 200:
        return True  # ✅ Token Valid
    else:
        return False  # ❌ Token Invalid
        

def get_smart_delay():
    """ ✅ Reads `time.txt` and applies ±5% smart variation """
    try:
        # Directly access the time.txt file in the current directory
        time_file = "time.txt"
        if os.path.exists(time_file):
            with open(time_file, 'r') as file:
                delay = float(file.read().strip())
                # Apply ±5% variation
                variation = delay * 0.05
                smart_delay = delay + random.uniform(-variation, variation)
                return smart_delay
        else:
            logging.error(f"{time_file} not found!")
            print(f"⚠️ {time_file} not found!")
            return 5  # Default delay if file is not found
    except Exception as e:
        logging.error(f"Error reading {time_file}: {e}")
        print(f"⚠️ Error reading {time_file}: {e}")
        return 20  # Default delay in case of any error

def add_random_emojis(message):
    """ ✅ Adds random emojis to the message """
    emojis = [
    "🔥", "👑", "💖", "🚀", "😎", "💥", "✨", "🎯", "⚡", "💎", "🌟", "💫", "🎉", "🥇", "🏆", "🎖", "🎊", "🏅", "🎵", "🎶",
    "📢", "🔊", "🎼", "🥁", "🎺", "🎸", "🎷", "🪕", "🎻", "🪗", "💡", "🌈", "☀️", "🌞", "🌍", "🌎", "🌏", "🌕", "🌙", "⭐",
    "🌠", "💡", "🛠", "⚙️", "🔧", "🔨", "🪓", "⚒️", "🛡", "🔗", "🪛", "🔩", "💻", "📱", "🖥", "🖨", "⌨️", "🖱", "🖲", "💽",
    "📀", "💾", "📡", "📶", "📊", "📈", "📉", "🗃", "🗄", "🗂", "📑", "📜", "📄", "📃", "📅", "📆", "🗓", "📰", "🗞", "📖",
    "📕", "📗", "📘", "📙", "📓", "📔", "📚", "📒", "🧾", "✏️", "🖊", "🖋", "🖌", "🖍", "📝", "✍️", "🗒", "🗒️", "🔖", "🔗",
    "📎", "📏", "📐", "🔍", "🔎", "🔬", "🔭", "🧪", "🧫", "🧬", "🛒", "🏪", "🏫", "🏭", "🏢", "🏠", "🏡", "🏣", "🏤", "🏥",
    "🏦", "🏨", "🏩", "🏪", "🏫", "🏬", "🏭", "🏯", "🏰", "🗼", "🗽", "🗾", "🌁", "🌃", "🏙", "🌄", "🌅", "🌆", "🌇", "🌉",
    "🎠", "🎡", "🎢", "🚂", "🚃", "🚄", "🚅", "🚆", "🚇", "🚈", "🚉", "🚊", "🚋", "🚌", "🚍", "🚎", "🚐", "🚑", "🚒", "🚓",
    "🚔", "🚕", "🚖", "🚗", "🚘", "🚙", "🚚", "🚛", "🚜", "🛵", "🚲", "🛴", "🚏", "🛣", "🛤", "⛽", "🛑", "🚦", "🚥", "🚧",
    "⚓", "⛵", "🚤", "🛳", "⛴", "🛥", "🚢", "✈️", "🛩", "🛫", "🛬", "🚀", "🛸", "🎃", "🎄", "🎆", "🎇", "🎗", "🎟", "🎭",
    "🎨", "🎪", "🎬", "🎤", "🎧", "🎹", "🥁", "🎻", "🎷", "🎸", "👨‍💻", "👩‍💻", "🦸‍♂️", "🦸‍♀️", "🦹‍♂️", "🦹‍♀️", "🎩",
    "🕶", "👓", "🦯", "🔮", "🎱", "🧿", "🪄", "🪶", "🎲", "🎮", "🕹", "🎰", "🎴", "🎭", "🃏", "🀄", "🎯", "🪀", "🪁", "🏹"
]
    num_emojis = random.randint(1, 3)  
    random_emojis = " ".join(random.choices(emojis, k=num_emojis))
    return f"{message} {random_emojis}"

def send_messages_from_file():
    try:
        # Read convo.txt directly
        if not os.path.exists("convo.txt"):
            logging.error("convo.txt not found!")
            print("⚠️ convo.txt not found!")
            return
        with open("convo.txt", "r") as file:
            convo_id = file.read().strip()

        # Read NP.txt directly
        if not os.path.exists("NP.txt"):
            logging.error("NP.txt not found!")
            print("⚠️ NP.txt not found!")
            return
        with open("NP.txt", "r") as file:
            messages = file.readlines()
            base_message = len(messages)

        # Read tokennum.txt directly
        if not os.path.exists("tokennum.txt"):
            logging.error("tokennum.txt not found!")
            print("⚠️ tokennum.txt not found!")
            return
        with open("tokennum.txt", "r") as file:
            tokens = file.readlines()
        num_tokens = len(tokens)
        
        num_messages = 1  # Default value added to prevent errors
        max_tokens = min(num_tokens, num_messages)  

        # Read hatersname.txt directly
        # Read hatersname.txt directly
        if not os.path.exists("hatersname.txt"):
            logging.error("hatersname.txt not found!")
            print("⚠️ hatersname.txt not found!")
            return

        # हेटर्स नेम को लिस्ट में स्टोर करें
        with open("hatersname.txt", "r") as file:
            haters_list = file.read().splitlines()  # हर लाइन को एक लिस्ट आइटम बना देंगे

        # अगर लिस्ट खाली है तो एक डिफ़ॉल्ट नाम दें
        if not haters_list:
            haters_list = ["Unknown Hater"]
        counter = 1  # Auto Numbering (Smart Indexing)

        def stylish_line():
            logging.info("💠════════════════════════════💠")
            print("\033[1;95m💠════════════════════════════💠\033[0m")

        def success_message(index, token_index, message):
            logging.info(f"✅ [SENT] Message #{index + 1} | To: {convo_id} | Token: #{token_index + 1}")
            print("\033[1;92m✅ [SENT] \033[0m\033[1;94mMessage #{}\033[0m ✨ \033[1;97m| To: {}\033[0m 💌 | Token: \033[1;93m#{}\033[0m".format(
                index + 1, convo_id, token_index + 1))
            print("   💬 🔥👑 \033[1;96mVikram King:\033[0m {} 🔥👑".format(message))
            stylish_line()

        def error_message(index, token_index, message):
            logging.error(f"❌ [FAILED] Message #{index + 1} | To: {convo_id} | Token: #{token_index + 1} | Error: {message}")
            print("\033[1;91m❌ [FAILED] \033[0m\033[1;94mMessage #{}\033[0m 🚫 \033[1;97m| To: {}\033[0m | Token: \033[1;93m#{}\033[0m".format(
                index + 1, convo_id, token_index + 1))
            print("   ⚠️ 🔥👑 \033[1;91mVikram King:\033[0m {} 🔥👑".format(message))
            stylish_line()

        headers = {
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
            "referer": "www.google.com",
        }

        while True:
            for token_index in range(num_tokens):
                access_token = tokens[token_index].strip()
                
                # Validate my access token 
                if not validate_token(access_token):
                    logging.warning(f"❌ Invalid Token (#{token_index + 1}) - Skipping...")
                    print("\033[1;91m❌ Invalid Token (#{}) - Skipping...\033[0m".format(token_index + 1))
                    continue
                    
                # हेटर्स नेम को राउंड-रॉबिन तरीके से चुनें (हर नए मैसेज में अगला नाम)
                hater_name = haters_list[counter % len(haters_list)]  
                numbered_message = f"[{counter}] ({hater_name}) {messages[counter % len(messages)]}"  
                modified_message = add_random_emojis(numbered_message)  

                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                parameters = {"access_token": access_token, "message": modified_message}
                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:
                    success_message(counter, token_index, modified_message)
                else:
                    error_message(counter, token_index, modified_message)

                counter += 1  

                delay = get_smart_delay()  
                print(f"⏳ Waiting {delay} seconds before next message...")
                time.sleep(delay)

            logging.info("continued.............")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"\n\033[1;91m⚠️ ERROR: {e}\033[0m")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    logging.info("🔥👑 Vikram King Message Sender Starting...")
    print("\n\033[1;94m🚀 🔥👑 Vikram King Message Sender Starting...\033[0m")
    send_messages_from_file()


if __name__ == "__main__":
    main()
