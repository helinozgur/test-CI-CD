from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    os.system('cd /test-CI-CD && git pull')
    return 'Success', 200
