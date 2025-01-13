import os
from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Depoyu güncelle
        os.system('cd /home/pam_golive/test-CI-CD && git pull')
 
        # Flask uygulamasını çalıştır veya yeniden başlat
        os.system('pkill -f "python3 /home/pam_golive/test-CI-CD/webhook.py"')
        os.system('nohup python3 /home/pam_golive/test-CI-CD/webhook.py &')
 
        return 'Flask application updated and restarted', 200
    except Exception as e:
        return f"Error: {str(e)}", 500
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)