from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Instrument, Base, MenuItem, User

engine = create_engine('postgresql://catalog:udacity@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com")
session.add(User1)
session.commit()


# Menu for Drums
instrument1 = Instrument(user_id=1, name="Drums")

session.add(instrument1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Natal Arcadia", description="A versatile, affordable\
drum kit for your first gigs or recording sessions", price="$699.99",\
instrument=instrument1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Yamaha Stage Custom Birch", description="A great budget all-birch drum set that is most at home on stage",
                     price="649.99", instrument=instrument1)

session.add(menuItem2)
session.commit()



# Menu for Vocals
instrument2 = Instrument(user_id=1, name="Vocals")

session.add(instrument2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Shure SM58", description="Quality sound, consistent performance and extreme durability.",
                     price="$99.99", instrument=instrument2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Sennheiser e935", description="Quality brand and trusted sound.",
                     price="$180", instrument=instrument2)

session.add(menuItem2)
session.commit()



# Menu for Guitars
instrument3 = Instrument(user_id=1, name="Guitars")

session.add(instrument3)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Fender Player Stratocaster", description="Fender's entry-level Strat delivers serious value for money",
                     price="$575", instrument=instrument3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="PRS SE Custom 24", description="The mid-priced, Korean-made, do-it-all solidbody",
                     price="$599", instrument=instrument3)

session.add(menuItem2)
session.commit()



print "added items!"
