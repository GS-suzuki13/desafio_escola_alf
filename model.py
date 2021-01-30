from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
engine = create_engine('sqlite:///desafio_escola_alf.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Proof_Model(Base):
    __tablename__ = 'proof'

    id = Column(Integer, primary_key=True, nullable=False)
    student_identification = Column(Integer, primary_key=True)


class Feedback_Model(Base):
    __tablename__ = 'feedback'

    id_proof = Column(Integer, ForeignKey('proof.id'), primary_key=True, nullable=False)
    question_number = Column(String(), primary_key=True, nullable=False)
    question_value = Column(Integer)
    alternative = Column(String(1))


class Answers_Model(Base):
    __tablename__ = 'answers'

    id_proof = Column(Integer, ForeignKey('proof.id'), primary_key=True, nullable=False)
    student_identification = Column(Integer, ForeignKey('proof.student_identification'))
    question_number = Column(String(), primary_key=True)
    alternative = Column(String(1))
