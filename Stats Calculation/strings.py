
STRENGTH = 'strength'
DEXTERITY = 'dexterity' 
CONSTITUTION = 'constitution'
INTELLIGENCE = 'intelligence'
WISDOM = 'wisdom'
CHARISMA = 'charisma'
ATTRIBUTE_NAMES = [STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE, WISDOM,
        CHARISMA]

ARMOR = 'armor'
SHIELD = 'shield'
DODGE = 'dodge'
NATURAL = 'natural armor'
MISC = 'misc'
AC_MODIFIERS = [ARMOR, SHIELD, DODGE, NATURAL, MISC]

AC_NORMAL = 'normal'
AC_TOUCH = 'touch'
AC_FLAT = 'flat-footed'
AC_TYPES = [AC_NORMAL, AC_TOUCH, AC_FLAT]

FORTITUDE = 'fortitude'
REFLEX = 'reflex'
WILL = 'will'
SAVE_NAMES = [FORTITUDE, REFLEX, WILL]

WEAPON_DAMAGE = 'damage'
WEAPON_ENCUMBRANCE = 'encumbrance'
WEAPON_FEATURES = [WEAPON_DAMAGE, WEAPON_ENCUMBRANCE]

ARMOR_BONUS = 'ac bonus'
ARMOR_ENCUMBRANCE = 'encumbrance'
ARMOR_CHECK = 'check penalty'
ARMOR_ASF = 'arcane spell failure'
ARMOR_FEATURES = [ARMOR_BONUS, ARMOR_ENCUMBRANCE, ARMOR_CHECK, ARMOR_ASF]
ARMOR_TYPE_BODY = 'body'
ARMOR_TYPE_SHIELD = 'shield'

ENCUMBRANCE_LIGHT = 'light'
ENCUMBRANCE_MEDIUM = 'medium'
ENCUMBRANCE_HEAVY = 'heavy'
ENCUMBRANCE_DOUBLE = 'double'
ENCUMBRANCE_NONE = 'none'

ATTACK_TYPE_MELEE = 'melee'
ATTACK_TYPE_PROJECTILE = 'projectile'
ATTACK_TYPE_THROWN = 'thrown'
ATTACK_TYPE_SPECIAL = 'special'

GOOD = 'good'
AVERAGE = 'average'
POOR = 'poor'

SIZE_FINE = 'fine'
SIZE_DIMINUITIVE = 'diminuitive'
SIZE_TINY = 'tiny'
SIZE_SMALL = 'small'
SIZE_MEDIUM = 'medium'
SIZE_LARGE = 'large'
SIZE_HUGE = 'huge'
SIZE_GARGANTUAN = 'gargantuan'
SIZE_COLOSSAL = 'colossal'

DAMAGE_PHYSICAL = 'physical'
DAMAGE_SLASHING = 'slashing'
DAMAGE_PIERCING = 'piercing'
DAMAGE_BLUDGEONING = 'bludgeoning'
DAMAGE_ACID = 'acid'
DAMAGE_COLD = 'cold'
DAMAGE_ELECTRICITY = 'electricity'
DAMAGE_FIRE = 'fire'