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
        
        switch = True

        FILTER_DEPLOY_LOCATION = [[ 4, 12],[ 23, 12],[ 4, 11],[ 5, 11],[ 6, 11],[ 21, 11],[ 22, 11],[ 23, 11],[ 7, 9],[ 20, 9],[ 7, 8],[ 8, 8],[ 9, 8],[ 18, 8],[ 19, 8],[ 20, 8],[ 10, 6],[ 17, 6],[ 10, 5],[ 11, 5],[ 12, 5],[ 15, 5],[ 16, 5],[ 17, 5],[ 13, 3],[ 14, 3]]
        ENCRYPTOR_DEPLOY_LOCATION = [[ 4, 13],[ 23, 13],[ 7, 10],[ 20, 10],[ 10, 7],[ 17, 7],[ 13, 4],[ 14, 4],[ 13, 2],[ 14, 2]]
        DESTRUCTOR_DEPLOY_LOCATION = [[ 3, 13],[ 24, 13],[ 6, 10],[ 21, 10],[ 9, 7],[ 18, 7],[ 12, 4],[ 15, 4],[ 13, 2],[ 14, 2]]

        if switch:
            self.deploy_information(game_state, [13, 0], PING, 5 )
            switch = False

        elif not switch:
            self.deploy_information(game_state, [14, 0], PING, 5)
            switch = True

        
        self.deploy_fireWall(game_state, DESTRUCTOR_DEPLOY_LOCATION, DESTRUCTOR)
        self.deploy_fireWall(game_state, FILTER_DEPLOY_LOCATION, FILTER)
        self.deploy_fireWall(game_state, ENCRYPTOR_DEPLOY_LOCATION, ENCRYPTOR)
        


        game_state.submit_turn()

    
    
        
    def deploy_fireWall(self, game_state, deploy_location, unit):
        #get location-info, check if blockend, if not build unit
        for location in deploy_location:
            if game_state.get_resource(game_state.CORES) >= game_state.type_cost(unit):
                if game_state.can_spawn(unit, location):
                    gamelib.debug_write(f"Eine Firewall: {unit} wurde auf der Position {location} für {game_state.type_cost(unit)} Cores gebaut.")
                    game_state.attempt_spawn(unit, location)

    def deploy_information(self, game_state, location, unit, unitCount):
        #deploy a given count of information-units on spezific location
        if game_state.get_resource(game_state.BITS) >= game_state.type_cost(unit, int(round(unit*unitCount))):
            if game_state.can_spawn(unit, location):
                game_state.attempt_spawn(unit, location, unitCount)


if __name__ == "__main__":
    algo = AlgoStrategy()
    algo.start()
