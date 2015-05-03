from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
images = Table('images', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('file', Unicode(length=1000)),
)

projects = Table('projects', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('description', String),
    Column('button_list_title', String),
    Column('button_list_url', String),
    Column('tags', String),
    Column('file', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['images'].create()
    pre_meta.tables['projects'].columns['file'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['images'].drop()
    pre_meta.tables['projects'].columns['file'].create()
