from sqlalchemy import Column, Integer, String,  Numeric
from app.database import Base
from app.mixins import mixins

class Product(Base, mixins.BaseMixin, mixins.TimestampMixin, mixins.CRUDMixin):
    
    __tablename__ = 'product'

    item = Column(String, nullable=False)
    qty = Column(Integer)
    price = Column(Integer)

    def __repr__(self):
        return ''

