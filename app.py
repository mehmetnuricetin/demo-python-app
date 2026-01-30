from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv('APP_VERSION', '1.0.0')

@app.route('/')
def hello():
  return f'''
    <html>
      <body style="font-family: Arial; padding: 50px;">
      <h1>Demo Python App</h1>
      <p>Version: {VERSION}</p>
      <p>GitOps CI/CD Demo with ArgoCD</p>
      </body>
    </html>
  '''

@app.route('/health')
def health():
  return {'status': 'healthy', 'version': VERSION}

@app.route('/info')
def info():
  return {
    'app': 'Demo Python App',
    'version': VERSION,
    'message': 'CI/CD with GitOps!'
  }

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)