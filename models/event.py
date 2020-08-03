from extensions import db


event_list = []


def get_last_id():
    if event_list:
        last_event = event_list[-1]
    else:
        return 1
    return last_event.id + 1


class Event(db.Model):
    __table_name__ = "event"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(200))

    is_publish = db.Column(db.Boolean(), default=False)

    event_date = db.Column(db.String(100))

    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())

    updated_at = db.Column(
        db.DateTime(),
        nullable=False,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
