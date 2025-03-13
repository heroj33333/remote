from flask import Flask, request
import pyautogui
import socket

app = Flask(__name__)

@app.route('/next', methods=['POST'])
def next_slide():
    pyautogui.press('right')
    return 'OK'

@app.route('/previous', methods=['POST'])
def previous_slide():
    pyautogui.press('left')
    return 'OK'

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Slide Controller</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }
            .btn {
                font-size: 50px;
                padding: 20px;
                margin: 10px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                color: white;
            }
            #prev {
                background-color: #ff4444; /* Red */
            }
            #next {
                background-color: #4444ff; /* Blue */
            }
        </style>
    </head>
    <body>
        <button class="btn" id="prev">←</button>
        <button class="btn" id="next">→</button>
        
        <script>
            const buttons = {
                prev: document.getElementById('prev'),
                next: document.getElementById('next')
            };

            function sendCommand(command) {
                fetch(`/${command}`, {
                    method: 'POST'
                }).catch(error => console.error('Error:', error));
            }

            buttons.prev.addEventListener('click', () => {
                sendCommand('previous');
            });

            buttons.next.addEventListener('click', () => {
                sendCommand('next');
            });
        </script>
    </body>
    </html>
    '''

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    ip = get_local_ip()
    print(f'Server starting on {ip}:5000')
    print(f'Open http://{ip}:5000 on your phone')
    app.run(host='0.0.0.0')
