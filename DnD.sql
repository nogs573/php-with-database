CREATE TABLE Creature( 
                CreatureName VARCHAR(60) primary key, Size VARCHAR(15), Type VARCHAR(30),
                Alignment VARCHAR(20), AC INTEGER, HP INTEGER, STR INTEGER, DEX INTEGER,
                CON INTEGER, `INT` INTEGER, WIS INTEGER, CHA INTEGER, CR REAL,
                SourceBook VARCHAR(40)
            );
CREATE TABLE Speeds(
                CreatureName VARCHAR(60), Speed VARCHAR(50),
                PRIMARY KEY(CreatureName, Speed),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade
            );
CREATE TABLE CreatureSTs(
                CreatureName VARCHAR(60), SavingThrow VARCHAR(5),
                PRIMARY KEY(CreatureName, SavingThrow),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade
            );
CREATE TABLE Skills(
                CreatureName VARCHAR(60), Skill VARCHAR(30),
                PRIMARY KEY(CreatureName, Skill),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade
            );
CREATE TABLE Senses(
                CreatureName VARCHAR(60), Sense VARCHAR(20),
                PRIMARY KEY(CreatureName, Sense),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade
            );
CREATE TABLE Languages(
                CreatureName VARCHAR(60), Language VARCHAR(20),
                PRIMARY KEY(CreatureName, Language),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade
            );
CREATE TABLE AdditionalFeature(
                CreatureName VARCHAR(60), Feature VARCHAR(60),
                PRIMARY KEY(CreatureName, Feature),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade
            );
CREATE TABLE DamageType(
                DamageName VARCHAR(11) PRIMARY KEY
            );
CREATE TABLE Spell(
                SpellName VARCHAR(50) PRIMARY KEY, Level INTEGER, Ritual VARCHAR(6),
                CastingTime INTEGER, `Range` INTEGER, Verbal VARCHAR(1), 
                Somatic VARCHAR(1), Material VARCHAR(1), Concentration VARCHAR(13),
                Duration INTEGER, DamageDice VARCHAR(30), MaxDamage INTEGER, SourceBook VARCHAR(5),
                Description VARCHAR(500)
            );
CREATE TABLE Weapon(
                WeaponName VARCHAR(20) PRIMARY KEY, SimpleMartial VARCHAR(7),
                MeleeRanged VARCHAR(6), WeaponGroup VARCHAR(8), DamageDice VARCHAR(30), MaxDamage INTEGER,
                Versatile VARCHAR(5), Light VARCHAR(1), Heavy VARCHAR(1),
                `Range` VARCHAR(15), Thrown VARCHAR(1), Finesse VARCHAR(1), Reach VARCHAR(1)
            );
CREATE TABLE PlayerClass(
                ClassName VARCHAR(9) PRIMARY KEY, HitDice VARCHAR(4),
                LightArmor VARCHAR(1), MediumArmor VARCHAR(1), HeavyArmor VARCHAR(1),
                Shield VARCHAR(1)
            );
CREATE TABLE ClassSTs(
                ClassName VARCHAR(60),  
                SavingThrow VARCHAR(60),
                PRIMARY KEY (ClassName,SavingThrow),
                FOREIGN KEY (ClassName) references PlayerClass(ClassName) on delete cascade
            );
CREATE TABLE WeakTo(
                CreatureName VARCHAR(60),
                DamageName VARCHAR(60),
                PRIMARY KEY (CreatureName, DamageName),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade,
                FOREIGN KEY (DamageName) references DamageType(DamageName) on delete cascade
            );
CREATE TABLE ImmuneTo(
                CreatureName VARCHAR(60),
                DamageName VARCHAR(60),
                PRIMARY KEY (CreatureName, DamageName),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade,
                FOREIGN KEY (DamageName) references DamageType(DamageName) on delete cascade
            );
CREATE TABLE Resists(
                CreatureName VARCHAR(60),
                DamageName VARCHAR(60),
                PRIMARY KEY (CreatureName, DamageName),
                FOREIGN KEY (CreatureName) references Creature(CreatureName) on delete cascade,
                FOREIGN KEY (DamageName) references DamageType(DamageName) on delete cascade
            );
CREATE TABLE SpellDmgType(
                SpellName VARCHAR(50),
                DamageName VARCHAR(60),
                PRIMARY KEY (SpellName, DamageName),
                FOREIGN KEY (SpellName) references Spell(SpellName) on delete cascade,
                FOREIGN KEY (DamageName) references DamageType(DamageName) on delete cascade
            );
CREATE TABLE WeaponDmgType(
                WeaponName VARCHAR(20),
                DamageName VARCHAR(60),
                PRIMARY KEY (WeaponName, DamageName),
                FOREIGN KEY (WeaponName) references Weapon(WeaponName) on delete cascade,
                FOREIGN KEY (DamageName) references DamageType(DamageName) on delete cascade
            );
CREATE TABLE CanUseWeapon(
                ClassName VARCHAR(60),
                WeaponName VARCHAR(20),
                PRIMARY KEY (ClassName, WeaponName),
                FOREIGN KEY (ClassName) references PlayerClass(ClassName) on delete cascade,
                FOREIGN KEY (WeaponName) references Weapon(WeaponName) on delete cascade
            );
CREATE TABLE CanUseSpell(
                ClassName VARCHAR(60),
                SpellName VARCHAR(50),
                PRIMARY KEY (ClassName, SpellName),
                FOREIGN KEY (ClassName) references PlayerClass(ClassName) on delete cascade,
                FOREIGN KEY (SpellName) references Spell(SpellName) on delete cascade
            );
