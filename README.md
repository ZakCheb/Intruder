# Intruder Game

    A web based game, very cheerished by OpenMindsClub members.


## Game server
Install dependencies
``` bash
pip install -r requirements.txt
```
Run a server with different params example:
``` bash
python Intruder_Server.py --spy=2  --minimum=5 --team=3
```

    -spy : number of spy generated on game.
    -team : number of players to go to mission.
    -port : server port. (currently hardcoded to be 8888 on the Game UI, fixing that soon.)

## Game UI

Require npm.
Instalation:
``` bash
cat install.sh # for paranoids
./install.sh
```
And finally, to start the Interface:
```bash
npm start 
```
Go to browser at localhost:8080

IMPORTANT: Once in a game, do not REFRESH the tab! or ask to every player to refresh aswell and restart the whole game.
