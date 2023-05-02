from src.app import app, env


if __name__ == '__main__':
    if env == '1':
        app.run(port=6001, debug=True)
    else:
        from waitress import serve
        serve(app, port=6001)
