

from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])


#http://127.0.0.1:5000/book/search?q=金庸
#9787108006721