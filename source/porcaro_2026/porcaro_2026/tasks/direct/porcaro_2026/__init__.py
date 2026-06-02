# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

##
# Register Gym environments.
##


gym.register(
    id="Template-Porcaro-2026-Direct-v0",
    entry_point=f"{__name__}.porcaro_2026_env:Porcaro2026Env",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.porcaro_2026_env_cfg:Porcaro2026EnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:PPORunnerCfg",
    },
)