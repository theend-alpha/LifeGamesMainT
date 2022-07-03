from YashuAlpha import YashviLovesAlpha

genderdb = YashviLovesAlpha.gender

async def add_male(a: int):
    males = await get_males()
    if a in males:
        return
    males.append(a)
    await genderdb.insert_one({"males": males})

async def get_males():
    _males = genderdb.find_one({"males": males})
    if _males:
        return _males
    else:
        return {}
