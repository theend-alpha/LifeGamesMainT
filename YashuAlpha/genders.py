from YashuAlpha import YashviLovesAlpha

genderdb = YashviLovesAlpha.gender

async def add_male(a: int):
    males = await get_males()
    if a in males:
        return
    males.append(a)
    await genderdb.insert_one({"males": males})

async def 
