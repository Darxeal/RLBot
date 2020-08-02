import multiprocessing as mp
import sys

from rlbot.agents.base_agent import BaseAgent
from rlbot.agents.standalone_agent import StandaloneAgentConfig
from rlbot.botmanager.bot_manager_struct import BotManagerStruct
from rlbot.matchconfig.match_config import MatchConfig
from rlbot.parsing.bot_config_bundle import get_bot_config_bundle
from rlbot.utils.class_importer import import_agent


class BotManagerStandaloneAgent(BaseAgent):

    def __init__(self, name, team, index):
        super().__init__(name, team, index)


def run_bot(agent_class: BotManagerStandaloneAgent):
    config = StandaloneAgentConfig(sys.argv)

    bundle = get_bot_config_bundle(config.config_file)
    config_obj = agent_class.base_create_agent_configurations()
    config_obj.parse_file(bundle.config_obj, config_directory=bundle.config_directory)
    agent_class_wrapper = import_agent(bundle.python_file)

    bot_manger = BotManagerStruct(terminate_request_event=mp.Event(),
                                  termination_complete_event=mp.Event(),
                                  reload_request_event=mp.Event(),
                                  bot_configuration=config_obj,
                                  name=config.name,
                                  team=config.team,
                                  index=config.player_index,
                                  agent_class_wrapper=agent_class_wrapper,
                                  agent_metadata_queue=mp.Queue(),
                                  match_config=None,
                                  matchcomms_root=None,
                                  spawn_id=config.spawn_id)
    bot_manger.run()
