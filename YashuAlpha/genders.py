from YashuAlpha import YashviLovesAlpha

genderdb = YashviLovesAlpha.gender

async def add_male(a: int):
    males = await get_males()
    if a in males:
        return
    males.append(a)
    await genderdb.update_one({"males": males}, upsert=True)

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

async def is_female(a: int):
    females = await get_females()
    if a in females:
        return True
    else:
        return False

async def add_female(a: int):
    females = await get_females()
    if a in females:
        return
    females.append(a)
    await genderdb.update_one({"females": females}, upsert=True)

async def del_female(a: int):
    females = await get_females()
    if a in females:
        females.remove(a)
    else:
        return 
    await genderdb.update_one({"females": females}, upsert=True)
