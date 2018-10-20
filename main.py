from app import app

if __name__ == '__main__':
    #running as development, so setting some hardcoded values
    app.run(host='0.0.0.0',port=5002,debug=False,threaded=True)
