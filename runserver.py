from app import create_app

from app.exts import db



app = create_app('development')

from app.api import api
app.register_blueprint(api)

db.init_app(app)



if __name__ == "__main__":
    app.run()


