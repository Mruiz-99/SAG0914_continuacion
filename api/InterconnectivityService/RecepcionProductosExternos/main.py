from src.app import env, app

if __name__ == '__main__':
    if env == '1':
        from waitress import serve
        serve(app, port=4020)
    else:
        from waitress import serve
        serve(app, port=4020)