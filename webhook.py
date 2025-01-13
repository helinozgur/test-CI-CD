from flask import Flask, request, abort
import os
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    os.system('cd /home/pam_golive/test-CI-CD && git pull')
    return 'Success', 200


if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000, debug=True)
