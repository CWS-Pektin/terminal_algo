import gamelib
import random
import math
import warnings
from sys import maxsize


class AlgoStrategy(gamelib.AlgoCore):
    def __init__(self):
        super().__init__()
        random.seed()

    def on_game_start(self, config):
        #_____SETUP______
        gamelib.debug_write('Configuring your custom algo strategy...')
        self.config = config
        global FILTER, ENCRYPTOR, DESTRUCTOR, PING, EMP, SCRAMBLER
        FILTER = config["unitInformation"][0]["shorthand"]
        ENCRYPTOR = config["unitInformation"][1]["shorthand"]
        DESTRUCTOR = config["unitInformation"][2]["shorthand"]
        PING = config["unitInformation"][3]["shorthand"]
        EMP = config["unitInformation"][4]["shorthand"]
        SCRAMBLER = config["unitInformation"][5]["shorthand"]


    def on_turn(self, turn_state):
        #____LOOP______
        #____NEEDED____
        game_state = gamelib.GameState(self.config, turn_state)
        gamelib.debug_write('Performing turn {} of your custom algo strategy'.format(game_state.turn_number))
        game_state.suppress_warnings(True)
        #______________
        

        FILTER_DEPLOY_LOCATION = [[ 0, 13],[ 1, 13],[ 2, 13],[ 3, 13],[ 4, 13],[ 5, 13],[ 6, 13],[ 7, 13],[ 8, 13],[ 9, 13],[ 10, 13],[ 17, 13],[ 18, 13],[ 19, 13],[ 20, 13],[ 21, 13],[ 22, 13],[ 23, 13],[ 24, 13],[ 25, 13],[ 26, 13],[ 27, 13]]
        ENCRYPTOR_DEPLOY_LOCATION = [[ 10, 11],[ 17, 11],[ 10, 10],[ 17, 10],[ 4, 9],[ 5, 9],[ 6, 9],[ 7, 9],[ 8, 9],[ 9, 9],[ 18, 9],[ 19, 9],[ 20, 9],[ 21, 9],[ 22, 9],[ 23, 9]]
        DESTRUCTOR_DEPLOY_LOCATION = [[ 1, 12],[ 4, 12],[ 7, 12],[ 10, 12],[ 17, 12],[ 20, 12],[ 23, 12],[ 26, 12],[ 10, 9],[ 17, 9]]
        UNITBLOCK_DEPLOY_LOCATION = [[ 11, 13],[ 16, 13],[ 11, 12],[ 16, 12],[ 11, 11],[ 16, 11],[ 11, 10],[ 16, 10],[ 11, 9],[ 16, 9],[ 5, 8],[ 6, 8],[ 7, 8],[ 8, 8],[ 9, 8],[ 10, 8],[ 11, 8],[ 16, 8],[ 17, 8],[ 18, 8],[ 19, 8],[ 20, 8],[ 21, 8],[ 22, 8]]

        #[[ 5, 8],[ 22, 8],[ 6, 7],[ 21, 7]]
        if game_state.turn_number % 2:
            self.deploy_information(game_state, [5, 8], SCRAMBLER, 2 )
            self.deploy_information(game_state, [6, 7], EMP, 1)
        else:
            self.deploy_information(game_state, [22, 8], SCRAMBLER, 2 )
            self.deploy_information(game_state, [21, 7], EMP, 1)

        
        self.deploy_fireWall(game_state, UNITBLOCK_DEPLOY_LOCATION, FILTER)
        self.deploy_fireWall(game_state, DESTRUCTOR_DEPLOY_LOCATION, DESTRUCTOR)
        self.deploy_fireWall(game_state, FILTER_DEPLOY_LOCATION, FILTER)
        self.deploy_fireWall(game_state, ENCRYPTOR_DEPLOY_LOCATION, ENCRYPTOR)

        game_state.submit_turn()

    
    
        
    def deploy_fireWall(self, game_state, deploy_location, unit):
        #get location-info, check if blockend, if not build unit
        for location in deploy_location:
            if game_state.get_resource(game_state.CORES) >= game_state.type_cost(unit):
                if game_state.can_spawn(unit, location):
                    game_state.attempt_spawn(unit, location)
                    gamelib.debug_write(f"Eine Firewall: {unit} wurde auf der Position {location} für {game_state.type_cost(unit)} Cores gebaut.")

    def deploy_information(self, game_state, location, unit, unitCount):
        #deploy a given count of information-units on spezific location
        if game_state.can_spawn(unit, location):
            game_state.attempt_spawn(unit, location, unitCount)
            gamelib.debug_write(f"Es wurden {unitCount} Informations-Einheiten: {unit} wurde auf der Position {location} für {int(game_state.type_cost(unit)*unitCount)} Bits gebaut")

    def remove_damaged (self, game_state, replace_location):
        #look at given location if a unit needs replacement
        for location in replace_location:           
            unit = game_state.contains_stationary_unit(location)
            if unit and unit.stability / unit.max_stability < 0.5:
                game_state.attempt_remove(location)

    


if __name__ == "__main__":
    algo = AlgoStrategy()
    algo.start()
