import pandas as pd
import mysql.connector
import os

# Connect to the MySQL database
cnx = mysql.connector.connect(user='bigBoss', password='newPass',
                               host='localhost', database='dnd')
cursor = cnx.cursor()

# Get the path to CSVs
cwd = os.getcwd()

data_path = os.path.join(cwd, 'data/')

# ----------------------------------------------------------------------------
# Read data from CSV files and insert into database

# Creatures

df = pd.read_csv(data_path + 'Creature.csv')

# Iterate over rows and insert data into MySQL table
for index, row in df.iterrows():
    query = "INSERT INTO Creature (CreatureName, Size, Type, Alignment, AC, HP, STR, DEX, CON, `INT`, WIS, CHA, CR, Sourcebook) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (row['CreatureName'], row['Size'], row['Type'], row['Alignment'], row['AC'], row['HP'], row['STR'], row['DEX'], row['CON'], row['INT'], row['WIS'], row['CHA'], row['CR'], row['Sourcebook'])    
    cursor.execute(query, data)

# Speeds

df = pd.read_csv(data_path + "Speeds.csv")
for index, row in df.iterrows():
    query = "INSERT INTO Speeds (CreatureName, Speed) VALUES (%s, %s)"
    data = (row['CreatureName'], row['Speed'])
    cursor.execute(query, data)

# CreatureSTs

df = pd.read_csv(data_path + "CreatureSTs.csv")
for index, row in df.iterrows():
    query = "INSERT INTO CreatureSTs (CreatureName, SavingThrow) VALUES (%s, %s)"
    data = (row['CreatureName'], row['SavingThrow'])
    cursor.execute(query, data)

# Skills

df = pd.read_csv(data_path + "Skills.csv")
for index, row in df.iterrows():
    query = "INSERT INTO Skills (CreatureName, Skill) VALUES (%s, %s)"
    data = (row['CreatureName'], row['Skill'])
    cursor.execute(query, data)

# Senses

df = pd.read_csv(data_path + "Senses.csv")
for index, row in df.iterrows():
    query = "INSERT INTO Senses (CreatureName, Sense) VALUES (%s, %s)"
    data = (row['CreatureName'], row['Sense'])
    cursor.execute(query, data)

# Languages

df = pd.read_csv(data_path + "Languages.csv")
for index, row in df.iterrows():
    query = "INSERT INTO Languages (CreatureName, Language) VALUES (%s, %s)"
    data = (row['CreatureName'], row['Language'])
    cursor.execute(query, data)

# AdditionalFeature

df = pd.read_csv(data_path + "AdditionalFeatures.csv")
for index, row in df.iterrows():
    query = "INSERT INTO AdditionalFeature (CreatureName, Feature) VALUES (%s, %s)"
    data = (row['CreatureName'], row['Feature'])
    cursor.execute(query, data)

# DamageType

df = pd.read_csv(data_path + "DamageType.csv")
for index, row in df.iterrows():
    query = "INSERT INTO DamageType (DamageName) VALUES (%s)"
    data = (row['DamageName'],) #tuple with one element
    cursor.execute(query, data)

# Spell

df = pd.read_csv(data_path + "Spell.csv")
for index, row in df.iterrows():
    query = "INSERT INTO Spell (SpellName, Level, Ritual, CastingTime, `Range`, Verbal, Somatic, Material, Concentration, Duration, DamageDice, MaxDamage, Description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (row['SpellName'], row['Level'], row['Ritual'], row['CastingTime'], row['Range'], row['Verbal'], row['Somatic'], row['Material'], row['Concentration'], row['Duration'], row['DamageDice'], row['MaxDamage'], row['Description'])
    cursor.execute(query, data)

# Weapon

df = pd.read_csv(data_path + "Weapon.csv")
for index, row in df.iterrows():
    query = "INSERT INTO Weapon (WeaponName, SimpleMartial, MeleeRanged, WeaponGroup, DamageDice, MaxDamage, Versatile, Light, Heavy, `Range`, Thrown, Finesse, Reach) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (row['WeaponName'], row['SimpleMartial'], row['MeleeRanged'], row['WeaponGroup'], row['DamageDice'], row['MaxDamage'], row['Versatile'], row['Light'], row['Heavy'], row['Range'], row['Thrown'], row['Finesse'], row['Reach'])
    cursor.execute(query, data)

# PlayerClass

df = pd.read_csv(data_path + "PlayerClass.csv")
for index, row in df.iterrows():
    query = "INSERT INTO PlayerClass (ClassName, HitDice, LightArmor, MediumArmor, HeavyArmor, Shield) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (row['ClassName'], row['HitDice'], row['LightArmor'], row['MediumArmor'], row['HeavyArmor'], row['Shield'])
    cursor.execute(query, data)

# ClassSTs

df = pd.read_csv(data_path + "ClassSTs.csv")
for index, row in df.iterrows():
    query = "INSERT INTO ClassSTs (ClassName, SavingThrow) VALUES (%s, %s)"
    data = (row['ClassName'], row['SavingThrow'])
    cursor.execute(query, data)

# WeakTo

df = pd.read_csv(data_path + "WeakTo.csv")
for index, row in df.iterrows():
    query = "INSERT INTO WeakTo (CreatureName, DamageName) VALUES (%s, %s)"
    data = (row['CreatureName'], row['DamageName'])
    cursor.execute(query, data)

# ImmuneTo

df = pd.read_csv(data_path + "ImmuneTo.csv")
for index, row in df.iterrows():
    query = "INSERT INTO ImmuneTo (CreatureName, DamageName) VALUES (%s, %s)"
    data = (row['CreatureName'], row['DamageName'])
    cursor.execute(query, data)

# Resists

df = pd.read_csv(data_path + "Resists.csv")
for index, row in df.iterrows():
    query = "INSERT INTO Resists (CreatureName, DamageName) VALUES (%s, %s)"
    data = (row['CreatureName'], row['DamageName'])
    cursor.execute(query, data)

# SpellDmgType

df = pd.read_csv(data_path + "SpellDmgType.csv")
for index, row in df.iterrows():
    query = "INSERT INTO SpellDmgType (SpellName, DamageName) VALUES (%s, %s)"
    data = (row['SpellName'], row['DamageName'])
    cursor.execute(query, data)

# WeaponDmgType

df = pd.read_csv(data_path + "WeapDmgType.csv")
for index, row in df.iterrows():
    query = "INSERT INTO WeaponDmgType (WeaponName, DamageName) VALUES (%s, %s)"
    data = (row['WeaponName'], row['DamageName'])
    cursor.execute(query, data)

# CanUseWeapon

df = pd.read_csv(data_path + "CanUseWeapon.csv")
for index, row in df.iterrows():
    query = "INSERT INTO CanUseWeapon (ClassName, WeaponName) VALUES (%s, %s)"
    data = (row['ClassName'], row['WeaponName'])
    cursor.execute(query, data)

# CanUseSpell

df = pd.read_csv(data_path + "CanUseSpell.csv")
for index, row in df.iterrows():
    query = "INSERT INTO CanUseSpell (ClassName, SpellName) VALUES (%s, %s)"
    data = (row['ClassName'], row['SpellName'])
    cursor.execute(query, data)

cnx.commit()
cnx.close()