from flask import abort
from six import string_types
from sqlalchemy import Column, DateTime as SdateTime, Integer
from datetime import datetime
from sqlalchemy.types import TypeDecorator
from app.database import Base, db_session

from app.config import TIMEZONE

db = Base

import pytz

# tz = pytz.timezone('utc')

class DateTime(TypeDecorator):
    impl = SdateTime
    def process_bind_param(self, value, engine):
        return value
    def process_result_value(self, value, engine):
        return value.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone(TIMEZONE))

class BaseMixin(object):
    """
    Provides the :attr:`id` primary key column
    """
    #: Database identity for this model, used for foreign key
    #: references from other models
    id = Column(Integer, primary_key=True, autoincrement=True)

class TimestampMixin(object):
    """
    Provides the :attr:`created_at` and :attr:`updated_at` audit timestamps
    """
    #: Timestamp for when this instance was created, in UTC
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    #: Timestamp for when this instance was last updated (via the app), in UTC
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    @classmethod
    def query(cls):
        return db_session.query(cls)

    @classmethod
    def get(cls, _id):
        if any((isinstance(_id, string_types) and _id.isdigit(),
                isinstance(_id, (int, float))),):
            return cls.query.get(int(_id))
        return None

    @classmethod
    def get_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_or_404(cls, _id):
        rv = cls.get(_id)
        if rv is None:
            abort(404)
        return rv

    @classmethod
    def get_or_create(cls, **kwargs):
        r = cls.get_by(**kwargs)
        if not r:
            r = cls(**kwargs)
            db_session.add(r)
        return r

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        if kwargs:
            for attr, value in kwargs.iteritems():
                setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db_session.add(self)
        if commit:
            try:
                db_session.commit()
            except Exception:
                db_session.rollback()
                raise
        return self

    def delete(self, commit=True):
        db_session.delete(self)
        return commit and db_session.commit()
