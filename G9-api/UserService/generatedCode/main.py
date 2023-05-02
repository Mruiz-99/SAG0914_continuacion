from src.app import env, app

if __name__ == '__main__':
    if env == '1':
        app.run(port=5100, debug=True)
    else:
        from waitress import serve
        serve(app, port=5100)
