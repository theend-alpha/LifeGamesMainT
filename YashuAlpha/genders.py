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

async def get_females():
    _females = genderdb.find_one({"females": females})
    if _females:
        return _females
    else:
        return {}

async def del_male(a: int):
    males = await get_males()
    if a in males:
        males.remove(a)
    else:
        return 
    await genderdb.update_one({"males": males}, upsert=True)

async def is_male(a: int):
    males = await get_males()
    if a in males:
        return True
    else:
        return False
