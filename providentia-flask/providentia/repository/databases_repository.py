import providentia.db
import providentia.entities.database
import logging
from flask import current_app
from config import default_config

config = default_config()
logging.basicConfig(level=config.LOGGING_LEVEL)

TABLE = 'databases'
COLUMNS = ("id", "name", "description", "icon")


def query_results(n=None):
    with current_app.app_context():
        cur = providentia.db.get_db().cursor()
        query = "SELECT id, name, description, icon " \
                "FROM {} ORDER BY name DESC".format(TABLE)

        if n is None:
            logging.debug("Executing query: %s", query)
            cur.execute(query)
        else:
            logging.debug("Executing query: %s LIMIT %d", query, n)
            cur.execute(query + " LIMIT %s", (str(n), ))

        rows = []
        if cur.rowcount > 0:
            for row in cur.fetchall():
                rows.append(dict(zip(COLUMNS, row)))
        else:
            return None

        deserialized = []

        for row in rows:
            deserialized.append(providentia.entities.database.deserialize(row))

        return deserialized


def find(row_id):
    with current_app.app_context():
        cur = providentia.db.get_db().cursor()
        query = "SELECT id, name, description, icon " \
                "FROM {} WHERE id = %s".format(TABLE)

        logging.debug("Executing query: %s", query.replace('%s', '{}').format(row_id))
        cur.execute(query, (row_id, ))

        if cur.rowcount > 0:
            result = dict(zip(COLUMNS, cur.fetchone()))
        else:
            return None

        deserialized = providentia.entities.database.deserialize(result)

        return deserialized


def find_name(row_name):
    with current_app.app_context():
        cur = providentia.db.get_db().cursor()
        query = "SELECT id, name, description, icon FROM {} WHERE name = %s".format(TABLE)

        logging.debug("Executing query: %s", query.replace('%s', '{}').format(row_name))
        cur.execute(query, (row_name,))

        if cur.rowcount > 0:
            result = dict(zip(COLUMNS, cur.fetchone()))
        else:
            return None

        deserialized = providentia.entities.database.deserialize(result)

        return deserialized