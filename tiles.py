import items, enemies, world, actions


class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()

	def adjacent_moves(self):
	    moves = []
	    if world.tile_exists(self.x + 1, self.y):
	        moves.append(actions.MoveEast())
	    if world.tile_exists(self.x - 1, self.y):
	        moves.append(actions.MoveWest())
	    if world.tile_exists(self.x, self.y - 1):
	        moves.append(actions.MoveNorth())
	    if world.tile_exists(self.x, self.y + 1):
	        moves.append(actions.MoveSouth())
	    return moves
 
	def available_actions(self):
	    moves = self.adjacent_moves()
	    moves.append(actions.ViewInventory())
	 
	    return moves

class StartingRoom(MapTile):
	def intro_text(self):
		return """
		You awake to the sound of frantic beeping. Your life support systems are running low. The lights around you are flickering in an unsettling manner. You see two paths presently, each as dark and foreboding as the last.
		"""

	def modify_player(self, player):
		#Room has no action on player
		pass

class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x,y)

	def add_loot(self, player):
		player.inventory.append(self.item)

	def modify_player(self, player):
		self.add_loot(player)

class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x,y)

	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print("Enemy does {} damage. You have {} HP remaining, tread lightly.".format(self.enemy.damage, the_player.hp))




class EmptyCorridorPath(MapTile):
    def intro_text(self):
        return """
        As you venture down the dark hallway, a feeling of unease sets over you.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """

class OrcRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Orc())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An orc turns from the desk to face you, 
            within the blink of an eye he swings his axe. 
            """
        else:
            return """
            The corpse of a filthy Orcses rots on the ground.
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(23))
 
    def intro_text(self):
        return """
        You see a chest covered in spider webs. 
        After you open the chest, you reveal there are 30 Gold peices inside. 
        """

class LeaveShipRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True