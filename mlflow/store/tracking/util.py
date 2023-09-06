def table_fullname(table):
    return f'"{table.__table__.schema}"."{table.__tablename__}"'
