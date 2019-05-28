import providentia.db
import providentia.entities.result
import logging
from flask import current_app
from config import default_config

config = default_config()
logging.basicConfig(level=config.LOGGING_LEVEL)


def query_results(n=None):
    with current_app.app_context():
        cur = providentia.db.get_db().cursor()
        query = "SELECT id, database_id, dataset_id, date_executed, title, description, query_time, analysis_time " \
                "FROM results ORDER BY date_executed DESC"

        if n is None:
            logging.debug("Executing query: %s", query)
            cur.execute(query)
        else:
            logging.debug("Executing query: %s LIMIT %d", query, n)
            cur.execute(query + " LIMIT %s", (str(n), ))

        columns = ("id", "database_id", "dataset_id", "date_executed", "title", "description", "query_time",
                   "analysis_time")
        rows = []
        if cur.rowcount > 0:
            for row in cur.fetchall():
                rows.append(dict(zip(columns, row)))
        else:
            return None

        deserialized = []

        for row in rows:
            deserialized.append(providentia.entities.result.deserialize(row))

        return deserialized


def find(row_id):
    with current_app.app_context():
        cur = providentia.db.get_db().cursor()
        query = "SELECT id, database_id, dataset_id, date_executed, title, description, query_time, analysis_time " \
                "FROM results WHERE id = %s"

        logging.debug("Executing query: %s", query, row_id)
        cur.execute(query, (row_id,))

        columns = ("id", "database_id", "dataset_id", "date_executed", "title", "description", "query_time",
                   "analysis_time")

        if cur.rowcount > 0:
            result = dict(zip(columns, cur.fetchone()))
        else:
            return None

        logging.debug(str(result))
        deserialized = providentia.entities.result.deserialize(result)

        return deserialized

