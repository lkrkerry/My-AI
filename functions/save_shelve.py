import shelve

def save(stuff):
    db = shelve.open(r"..\database\shelve_lite.db")
    try:
        assert type(stuff) == type({})
    except AssertionError:
        return "stuff must be dict"
    else:
        for key in stuff:
            db[key] = stuff[key]
        db.close()
        return "success"
    
def get(key):
    db = shelve.open(r"..\database\shelve_lite.db")
    try:
        return db[key]
    except Exception:
        return "hasn't found"
    
if __name__ == "__main__":    
    save({"hi":"hi"})
    print(get("hiv"))