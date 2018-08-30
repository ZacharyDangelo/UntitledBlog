import sqlite3
import datetime as dt
import Post


"""
Look at the notes and try to plan this out...
I don't know what the best way to handle this would be.
"""

#TODO:  Finish this function
def check_events(db_conn):
    if isinstance(db_conn, sqlite3.Connection):
        current_date = dt.date.strftime(dt.date.today(), '%m/%d/%y')
        current_time = str(dt.datetime.now().time()).split(sep=':')
        current_time = str(current_time[0] + ':' + current_time[1])
        print(current_time)

        events = db_conn.execute('select EventID, ScheduledDate, \
                                 ScheduledTime, EventType, ID \
                                 from ScheduledEvents')
        for row in events.fetchall():
            if current_time == row['ScheduledTime']:
                Post.publish_post(db_conn, row['ID'])

    else:
        return

