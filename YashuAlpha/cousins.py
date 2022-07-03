from YashuAlpha import YashviLovesAlpha

cousinsdb = YashviLovesAlpha.cousins

async def add_cousin(a: int, b: int):
    _cousins = await get_cousins(a)
    if b in _cousins:
        return
    _cousins.append(b)
    await cousinsdb.update_one(
        {"a": a}, {"$set": {"cousins": _cousins}}, upsert=True
    )

async def get_cousins(a: int):
    _cousins = await cousinsdb.find_one({"a": a})
    if _cousins:
        cousins = _cousins["cousins"]
    else:
        cousins = {}
    return cousins

async def del_cousin(a:int, b: int):
    _cousins = await get_cousins(a)
    if b in _cousins:
        _cousins.remove(b)
    else:
        return
    await cousinsdb.update_one(
        {"a": a}, {"$set": {"cousins": _cousins}}, upsert=True
    )

async def are_cousins(a: int, b: int):
    _cousins = await cousinsdb.find_one({"a": a})
    if b in _cousins:
        return True
    else:
        False
