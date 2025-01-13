from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    os.system('cd /home/pam_golive/test-CI-CD && git pull')
    return 'Success', 200
