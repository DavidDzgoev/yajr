from sqlalchemy import Boolean, ForeignKey, Integer, String, SmallInteger
from sqlalchemy.orm import mapped_column, Mapped

from database import Base, engine


class Contest(Base):
    __tablename__ = "contest"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_finished: Mapped[bool] = mapped_column(Boolean)
    duration: Mapped[str] = mapped_column(String)
    round: Mapped[int] = mapped_column(SmallInteger, index=True)
    round_code: Mapped[str] = mapped_column(String, index=True)
    round_name: Mapped[str] = mapped_column(String, index=True)
    type: Mapped[int] = mapped_column(SmallInteger, index=True)
    gs: Mapped[int] = mapped_column(SmallInteger, index=True)
    bye: Mapped[int] = mapped_column(SmallInteger, index=True)
    fight_no: Mapped[int] = mapped_column(SmallInteger, index=True)
    weight: Mapped[int] = mapped_column(SmallInteger, index=True)
    id_weight: Mapped[int] = mapped_column(SmallInteger, index=True)
    fight_duration: Mapped[int] = mapped_column(SmallInteger)
    rank_name: Mapped[str] = mapped_column(String, index=True)

    ippon_w: Mapped[int] = mapped_column(SmallInteger)
    waza_w: Mapped[int] = mapped_column(SmallInteger)
    yuko_w: Mapped[int] = mapped_column(SmallInteger)
    penalty_w: Mapped[int] = mapped_column(SmallInteger)
    hsk_w: Mapped[int] = mapped_column(SmallInteger)

    ippon_b: Mapped[int] = mapped_column(SmallInteger)
    waza_b: Mapped[int] = mapped_column(SmallInteger)
    yuko_b: Mapped[int] = mapped_column(SmallInteger)
    penalty_b: Mapped[int] = mapped_column(SmallInteger)
    hsk_b: Mapped[int] = mapped_column(SmallInteger)

    rating_change_w: Mapped[int] = mapped_column(SmallInteger, index=True)
    rating_change_b: Mapped[int] = mapped_column(SmallInteger, index=True)

    id_person_w: Mapped[int] = mapped_column(ForeignKey("person.id"), index=True)
    id_person_b: Mapped[int] = mapped_column(ForeignKey("person.id"), index=True)
    id_winner: Mapped[int] = mapped_column(ForeignKey("person.id"), index=True)
    id_competition: Mapped[int] = mapped_column(ForeignKey("competition.id"), index=True)


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    family_name: Mapped[str] = mapped_column(String, index=True)
    given_name: Mapped[str] = mapped_column(String, index=True)
    gender: Mapped[str] = mapped_column(String, index=True)
    personal_picture: Mapped[str] = mapped_column(String, index=True)
    dob_year: Mapped[int] = mapped_column(SmallInteger, index=True)  # check type

    id_country: Mapped[int] = mapped_column(ForeignKey("country.id"), index=True)


class Rating(Base):
    __tablename__ = "rating"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_weight: Mapped[int] = mapped_column(SmallInteger, index=True)
    weight: Mapped[int] = mapped_column(SmallInteger, index=True)
    system: Mapped[int] = mapped_column(SmallInteger, index=True)  # finish

    id_person: Mapped[int] = mapped_column(ForeignKey("person.id"), index=True)


class Country(Base):
    __tablename__ = "country"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    name_short: Mapped[str] = mapped_column(String, index=True)
    file_flag: Mapped[str] = mapped_column(String, index=True)


class Competition(Base):
    __tablename__ = "competition"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    name_short: Mapped[str] = mapped_column(String, index=True)
    competition_short: Mapped[str] = mapped_column(String, index=True)
    competition_code: Mapped[str] = mapped_column(String, index=True)
    city: Mapped[str] = mapped_column(String, index=True)
    timezone: Mapped[str] = mapped_column(String, index=True)
    date_from: Mapped[str] = mapped_column(String)
    date_to: Mapped[str] = mapped_column(String)

    id_country: Mapped[int] = mapped_column(ForeignKey("country.id"), index=True)

Base.metadata.create_all(engine)
