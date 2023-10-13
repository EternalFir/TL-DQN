""" battle of two armies """

import magent


def get_config(map_size):
    gw = magent.gridworld
    cfg = gw.Config()

    cfg.set({"map_width": map_size, "map_height": map_size})
    cfg.set({"minimap_mode": True})
    cfg.set({"embedding_size": 10})

    small = cfg.register_agent_type(
        "small",
        {'width': 1, 'length': 1, 'hp': 10, 'speed': 2,
         'view_range': gw.CircleRange(6), 'attack_range': gw.CircleRange(1.5),
         'damage': 2, 'step_recover': 0.1,

         'step_reward': -0.005,  'kill_reward': 5, 'dead_penalty': -0.1, 'attack_penalty': -0.1,
         })

    Tank = cfg.register_agent_type(
        "tank",
        {'width': 2, 'length': 2, 'hp': 300, 'speed': 1.5,
         'view_range': gw.CircleRange(10), 'attack_range': gw.CircleRange(2),
         'damage': 30, 'step_recover': 0.1,

         'step_reward': -0.005,  'kill_reward': 50, 'dead_penalty': -0.6, 'attack_penalty': -0.1,
         })

    Marine = cfg.register_agent_type(
        "Marine",
        {'width': 1, 'length': 1, 'hp': 50, 'speed': 2,
         'view_range': gw.CircleRange(10), 'attack_range': gw.CircleRange(6),
         'damage': 6, 'step_recover': 0.1,

         'step_reward': -0.005, 'kill_reward': 10, 'dead_penalty': -0.1, 'attack_penalty': -0.1,
         })

    g0 = cfg.add_group(small)
    g1 = cfg.add_group(small)


    a = gw.AgentSymbol(g0, index='any')
    b = gw.AgentSymbol(g1, index='any')

    # reward shaping to encourage attack
    cfg.add_reward_rule(gw.Event(a, 'attack', b), receiver=a, value=0.4)
    cfg.add_reward_rule(gw.Event(b, 'attack', a), receiver=b, value=0.4)

    # g0 = cfg.add_group(Marine)
    # g1 = cfg.add_group(Tank)
    #
    # a = gw.AgentSymbol(g0, index='any')
    # b = gw.AgentSymbol(g1, index='any')
    #
    # # reward shaping to encourage attack
    # cfg.add_reward_rule(gw.Event(a, 'attack', b), receiver=a, value=0.4)
    # cfg.add_reward_rule(gw.Event(b, 'attack', a), receiver=b, value=2.4)

    return cfg
