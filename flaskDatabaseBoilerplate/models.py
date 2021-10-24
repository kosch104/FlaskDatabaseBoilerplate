from flaskDatabaseBoilerplate import db


class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"<MyModel> (id={self.id}, name={self.name})"