import creature
import util
from abilities import abilities
from classes import LevelProgression, GOOD, AVERAGE, POOR

class Monster(creature.Creature):
    
    def __init__(self, raw_stats, level, verbose = False):
        self.level = level
        self.verbose = verbose

        self._init_core_statistics()
        self._interpret_raw_stats(raw_stats)
        self._interpret_raw_attributes(raw_stats)
        self.creature_type = raw_stats['creature type']

        self._set_creature_type(raw_stats)
        self._calculate_class_stats()

        #self._interpret_raw_attributes(util.parse_stats_from_file('data/attributes/warrior.txt'))

        self._calculate_derived_statistics()

    @classmethod
    def from_monster_name(cls, monster_name, level):
        monster_filename = 'data/monsters/'+monster_name+'.txt'
        raw_stats = util.parse_stats_from_file(monster_filename)
        return cls(raw_stats, level)

    def _set_creature_type(self, raw_stats):
        self.level_progression = {
                'aberration': Aberration,
                'animal': Animal
                }[raw_stats['creature type']](self.level)
        #Now that we have a level progression, apply templates
        self._apply_templates()

class Aberration(LevelProgression):
    bab_progression = AVERAGE
    save_progressions = {'fortitude': AVERAGE, 'reflex':POOR, 'will':AVERAGE}
    hit_value = 5

    def apply_modifications(self, base_creature):
        pass

class Animal(LevelProgression):
    bab_progression = AVERAGE
    save_progressions = {'fortitude': AVERAGE, 'reflex': AVERAGE, 'will': POOR}
    hit_value = 6

    def apply_modifications(self, base_creature):
        if base_creature.alignment is None:
            base_creature.alignment = 'neutral'
        base_creature.add_ability(abilities['scent'])
        base_creature.add_ability(abilities['low-light vision'])
        base_creature.add_ability(abilities['natural armor'])

if __name__=="__main__":
    monster = Monster.from_monster_name('brown_bear', 4)
    print monster
