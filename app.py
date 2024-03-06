from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Note: Google Cloud Run will set the PORT environment variable to tell you what port to listen on
    import os
    port = int(os.environ.get('PORT', 80))  # Default to 8080 if PORT not set
    app.run(debug=True, host='0.0.0.0', port=port)
