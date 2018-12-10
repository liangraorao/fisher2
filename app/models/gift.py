from app.models.base import db
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.base import Base


class Gift(Base):
    id = Column(Integer(), primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False, comment='赠送成功：1 未赠送：0')