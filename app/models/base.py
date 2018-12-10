from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # create_time = Column('Create_time', Integer)
    status = Column(SmallInteger, default=1, comment='0:删除  1：正常')

    def set_attrs(self, sttrs_dict):
        for key, value in sttrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)