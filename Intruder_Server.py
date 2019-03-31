import asyncio
import json
import logging
import websockets
import random as ran
import time
#I'm aware about the the dirty globals.
NUMBER_OF_ESPION=2
SERVER_PORT=8888
NUMBER_OF_PLAYER_IN_TEAM=3
MINIMUM_PLAYERS=2
logging.basicConfig()
GameStarted=False
USERS  = list() # Websockets, index like names.
NAMES  = list() # Names of the players.
VOTES  = dict()
READY  = dict() # Are players Ready
FACTION = dict() # Revolutionary/Spy 1/0
DECIDE = dict() # Decide either to Succed (1) the mission or to fail (0) it.
SELECTED = list() # Wich players are selected to go to mission
Turn=0 # current index of player who choose the team who go to mission.
Timer=5 # Wait time to vote.
##### Fire config########
import fire
def Setup(port=8888,spy=1,team=2,minimum=2):
    global NUMBER_OF_ESPION
    NUMBER_OF_ESPION=spy
    global NUMBER_OF_PLAYER_IN_TEAM
    NUMBER_OF_PLAYER_IN_TEAM=team
    global SERVER_PORT
    SERVER_PORT=port
    global MINIMUM_PLAYERS
    MINIMUM_PLAYERS=minimum

fire.Fire(Setup)
###############################

#Check if every param is correct.
print(
"NUMBER_OF_ESPION ",NUMBER_OF_ESPION,
"NUMBER_OF_PLAYER_IN_TEAM ",NUMBER_OF_PLAYER_IN_TEAM,
"SERVER_PORT ",SERVER_PORT,
"MINIMUM_PLAYERS",MINIMUM_PLAYERS)

async def Send(m,_type): # Send data to all players
    if USERS:       # asyncio.wait doesn't accept an empty list
        message =json.dumps({'type': _type ,_type: m})
        await asyncio.wait([user.send(message) for user in USERS])


async def Send_Faction():# Send Faction for each player individualy
    for i in range(len(USERS)):
       message =json.dumps({'type': 'faction','faction': FACTION[NAMES[i]]   })
       await USERS[i].send(message)


async def register(websocket): # Handle New connections to the server
    # on player login receive name of the player
    await Send(NAMES,'names')
    if GameStarted:
        websockets.close()
    name = await websocket.recv()
    name = json.loads(name)['Name']
    print('New user:'+name)
    USERS.append(websocket)
    NAMES.append(name)
    READY[name]=False
    DECIDE[name]=1
    #await Send_Users()
    await Send(NAMES,'names')
    await Send(READY,'ready')
    await Send({'NUMBER_OF_PLAYER_IN_TEAM':NUMBER_OF_PLAYER_IN_TEAM},'params')


async def unregister(websocket):
    name = NAMES[USERS.index(websocket)]
    print('Disconnected user:'+name)
    NAMES.remove(name)
    USERS.remove(websocket)
    READY.pop(name)
    VOTES.pop(name)
    await Send(NAMES,'names')


async def GenerateFaction():
    if len(NAMES) < MINIMUM_PLAYERS:
        return False
    for name in NAMES : # check if all ready.
        if READY[name] == False :
            return False
    GameStarted=True

    ##GENERATE  ESPION LOGIC##
    for name in NAMES :
        FACTION[name]=1 # All Revolutionary
    i=0
    while (i < NUMBER_OF_ESPION):
        random_player=NAMES[ran.randint(0,len(NAMES)-1)]
        if FACTION[random_player]: # if the randomly selected player is Revolu
            FACTION[random_player]=0 # Make him Espion
        else : #generate random again, if we selected Espion
            i-=1
        i+=1
    print(FACTION)

    ##################
    print('Game Started.')
    await Send_Faction()
    await Send(NAMES[Turn],'turn') # Send the turn of wich player to vote a team.


async def Count_Votes():
    global VOTES
    global Turn
    global SELECTED
    ##Count Votes##
    y=0
    n=0
    for name in NAMES:
        if name in VOTES.keys()  :
            if VOTES[name]:
                y+=1
            else :
                n+=1
    ######################

    ##### Game Logic ######
    if len(NAMES) == len(VOTES) and len(SELECTED) == NUMBER_OF_PLAYER_IN_TEAM :
        # if all voted and TurnPlayer selected Team to go mission
        Result={'Yes':y,'No':n}
        print('All Voted.',Result)

        if y > n :   # If Vote accepted

            await Send({"timer":Timer},"accepted_vote")
            print('Timer start')
            time.sleep(Timer)
            print('Timer done')
            success= 0
            failure= 0
            for name in SELECTED :
                if DECIDE[name] == 0 and FACTION[name] == 0:  # If player voted Fail and is Spy
            # DECIDE=>Failure=0 Success=1   FACTION=>Revolutionary=1 Spy=0
                    failure +=1
                else :
                    success +=1
            Result['Success']=success
            Result['Failure']=failure




        await Send(Result,'vote_result')
        Turn = (Turn+2) % len(NAMES) -1 # Next player
        await Send(NAMES[Turn],'turn')
        VOTES=dict()
        SELECTED=list()
        await Send(SELECTED,'selected')
        await Send(VOTES,'votes')
    ############################

async def MainLoop(websocket, path): ## Every player start here.

    await websocket.send(json.dumps({'type': 'connected'}))
    global SELECTED
    await Send(NAMES,'names')
    if not GameStarted:
        await register(websocket)
    name = NAMES[USERS.index(websocket)] # Current player name
    try:
        async for message in websocket: # For each message received by the UI
            data = json.loads(message)
            print(data)
            if 'Ready' in data.keys()  : # receive data
                READY[name] = data['Ready']
                print(name," is ready ="+str( READY[name]))
                await GenerateFaction()
                await Send(READY,'ready') # send update to the other players
            elif 'Votes' in data.keys() :
                VOTES[name] = data['Votes']
                print(name," voted="+str( VOTES[name]))
              #await notify_state()
                await Count_Votes()
                await Send(VOTES,'votes')
            elif 'Selected' in data.keys() :
                # SELECTED=list()
                SELECTED = data['Selected'].copy()
                print(SELECTED)
                await Send(SELECTED,'selected')
                await Count_Votes()
            elif 'Decide' in data.keys() :
                DECIDE[name] = data['Decide']
                print(DECIDE)
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)

asyncio.get_event_loop().run_until_complete(websockets.serve(MainLoop, '0.0.0.0', SERVER_PORT))
asyncio.get_event_loop().run_forever()
