from db import sql_select_next


def get_next_untagged():
    res = sql_select_next()
    return res
