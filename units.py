# class Unit:
#     def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
#                  intellect: int = 1):
#         self.name = name
#         self.clan = clan
#         self.health = health
#         self.strength = strength
#         self.dexterity = dexterity
#         self.intellect = intellect
#         self._ability = ''
#
#     def __str__(self):
#         return f"I am {self.name}, and I am a {self._ability} {type(self).__name__}. I have such stats: \nClan - {self.clan}" \
#                f"\nHealth = {self.health}, \nStrength = {self.strength}, \nDexterity = {self.dexterity}, " \
#                f"\nIntellect = {self.intellect} "
#
#     def heal(self):
#         health = 100 - self.health
#         to_heal = 10 if health >= 10 else health
#         self.health += to_heal
#         print(f"I have been healed on {to_heal} points!")
#         return self.health
#
#
# class Mage(Unit):
#     def __init__(self, name: str, clan: str, health: int = 100, strength: int = 1, dexterity: int = 1,
#                  intellect: int = 1, magic=''):
#         super().__init__(name, clan, health, strength, dexterity, intellect)
#         self._ability = magic
#
#     @property
#     def magic(self):
#         return self._ability
#
#     # def __str__(self):
#     #     return super().__str__(self.magic)
#
#     def increase_stat(self):
#         self.intellect += 1 if self.intellect < 10 else self.health
#         return self.intellect
#
# MAGIC_TYPE = {
#     'f': 'Fire',
#     'a': 'Air',
#     'w': 'Water'
# }
#
# BOW_TYPE = {
#     'b': 'Bow',
#     'cb': 'Crossbow'
# }
#
# WEAPON_TYPE = {
#     's': 'Sword',
#     'a': 'Axe',
#     'p': 'Peak'
# }
#
# mage = Mage('John', 'SunShine', magic=MAGIC_TYPE['f'])
# # archer = Archer('Jack', 'MoonShine', bow_type=BOW_TYPE['cb'])
# # knight = Knight('John', 'RiverFrost', weapon_type=WEAPON_TYPE['a'])
#
# print(mage.magic)








def find_words(text: str, words: list):
    text_lst = (text.lower().strip('\n')).split(' ')
    amount = []
    for word in words:
        if word in text_lst:
            amount.append(text_lst.count(word))
        else:
            amount.append(0)
    my_dict = dict((words[i], amount[i]) for i in range(len(amount)))
    return my_dict


from collections import Counter

def popular_words(text, words):
    text = text.lower()
    text_words = text.split()
    result_dict = {word: text_words.count(word) for word in words}
    return result_dict
    # return {word: text.lower().split().count(word) for word in words}

text = "qw qw e E e"
words = ["a", "e"]
print(popular_words(text, words))
