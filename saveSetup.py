import pickle
from parameters import NUM_SAVE_FILES as num
for i in range(1,num+1):
    db = {"MaxHealth" : 0, 
            "currentHealth":0, 
            "maxShields":0, 
            "currentShields":0, 
            "shieldRegen":0,
            "turnSpeed": 0,
            "acceleration":0,
            "bulletSpeed":0,
            "bulletStrength":0,
            "fireRate":0,
            "topSpeed":0,
            "wallet":0,
            "cargo":0,
            "maxCargo":0,
            "cargoValue":0,
            "maxed":0,
            "upgradeCost":0,
            "level":0}
    dbfile = open(f"savefile{i}", 'wb')
    pickle.dump(db, dbfile)
    dbfile.close()