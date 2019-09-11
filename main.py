import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def render(world,current_location):
    ''' print out a description of the current location '''
    room = world[current_location]
    print(room["name"])
    print(room["desc"])
    return True

def check_input():
    ''' request input from the player '''
    user_input = input("What would you like to do?") #first question/ interaction
    # do we want to validate?
    return user_input

def update():
    '''check if we need to move to a new location, etc ''' 
    return True


def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'

    quit = False
    while not quit:
    #render the world
        render(game["rooms"],current)
        user_input = check_input()
    #check for player input
    #update the state of the world




#if we are running this from the command line, run main
if __name__ == '__main__':
	main()