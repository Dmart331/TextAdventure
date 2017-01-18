class Enemy:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0

	def available_actions(self):
		if self.enemy.is_alive():
		    return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
		else:
		    return self.adjacent_moves()

class DarkElf(Enemy):
	def __init__(self):
		super().__init__(name="Dark Elf", hp = 50, damage = 29)

class Orc(Enemy):
	def __init__(self):
		super().__init__(name="Orc", hp=40, damage = 20)

class GiantSpider(Enemy):
	def __init__(self):
		super().__init__(name="Giant Spider", hp=52, damage = 30)

