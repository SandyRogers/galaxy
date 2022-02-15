"""
Migration script for adding trs_id column to workflow table.
"""

import logging

from sqlalchemy import (
    Column,
    MetaData,
    Text,
)

from galaxy.model.migrate.versions.util import (
    add_column,
    drop_column,
)

log = logging.getLogger(__name__)
metadata = MetaData()


def upgrade(migrate_engine):
    print(__doc__)
    metadata.bind = migrate_engine
    metadata.reflect()

    trs_id_column = Column("trs_id", Text)
    add_column(trs_id_column, "workflow", metadata)


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    metadata.reflect()

    drop_column("trs_id", "workflow", metadata)
