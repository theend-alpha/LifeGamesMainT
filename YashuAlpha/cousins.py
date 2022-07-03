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
