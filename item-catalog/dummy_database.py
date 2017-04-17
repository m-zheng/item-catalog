from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User


engine = create_engine('sqlite:///itemCatalog.db')
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


# Create a dummy user
User1 = User(name="Stephen Curry", email="curry@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# Create a dummy category
category1 = Category(user_id=1, name="Jazz")
session.add(category1)
session.commit()


# Create dummy items for category
item1 = Item(user_id=1, name="Strange Fruit", category=category1)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Lush Life", category=category1)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="God Bless the Child", category=category1)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="How High The Moon", category=category1)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Mack the Knife (in Berlin)", category=category1)
session.add(item5)
session.commit()


category2 = Category(user_id=1, name="Funk")
session.add(category2)
session.commit()


item5 = Item(user_id=1, name="More Bounce to the Ounce", category=category2)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Give Up the Funk", category=category2)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Super Freak", category=category2)
session.add(item7)
session.commit()


category3 = Category(user_id=1, name="Disco")
session.add(category3)
session.commit()


item8 = Item(user_id=1, name="I Feel Love", category=category3)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Love to Love You Baby", category=category3)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Last Dance", category=category3)
session.add(item10)
session.commit()


print "added item catalog!"
