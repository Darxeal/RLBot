"""Standalone Bot Script

Usage:
    standalone --config-file=C:/Users/t/code/myBot.cfg --name=ReliefBot --team=0 --player-index=0 [--spawn-id=23245]

Options:
    --config-file=C              Absolute path to .cfg file, which should define the executable path, etc.
    --name=N                     Name of the bot in-game
    --team=T                     Team the bot is playing on, 0 for blue, 1 for orange.
    --player-index=I             Index that the player is running under.
    --spawn-id=S                 Spawn identifier used to confirm the right car in the packet.
"""
from typing import List

from docopt import docopt


class StandaloneAgentConfig:

    def __init__(self, argv: List[str]):
        arguments = docopt(__doc__, argv[1:])
        self.name = arguments['--name']
        self.team = int(arguments['--team'])
        self.player_index = int(arguments['--player-index'])
        self.spawn_id = self.int_or_none(arguments['--spawn-id'])
        self.config_file = arguments['--config-file']

    def int_or_none(self, val):
        if val:
            return int(val)
        return None
