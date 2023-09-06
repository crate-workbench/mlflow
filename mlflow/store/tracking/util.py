from vasuki import generate_nagamani19_int


def generate_unique_integer() -> int:
    return generate_nagamani19_int(size=10)


def table_fullname(table):
    return f'"{table.__table__.schema}"."{table.__tablename__}"'
