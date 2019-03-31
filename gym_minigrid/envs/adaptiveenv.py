from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class AdaptiveEnv(MiniGridEnv):
    """
    Empty grid environment, no obstacles, sparse reward
    """

    def __init__(
        self,
        size=8,
        agent_start_pos=(1,1),
        agent_start_dir=0,
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            see_through_walls=True
        )

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        # self.grid.wall_rect(0, 0, width, height)

        # Place a goal square in the bottom-right corner
        self.grid.set(width - 3, height - 3, Goal())

        # Place the agent
        if self.agent_start_pos is not None:
            self.start_pos = self.agent_start_pos
            self.start_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "get to the green goal square"

class AdaptiveMapping10x10(AdaptiveEnv):
    def __init__(self):
        super().__init__(size=10, agent_start_pos=None)


class AdaptiveMapping16x16(AdaptiveEnv):
    def __init__(self):
        super().__init__(size=16, agent_start_pos=None)


register(
    id='MiniGrid-AdaptiveMapping-10x10-v0',
    entry_point='gym_minigrid.envs:AdaptiveMapping10x10'
)

register(
    id='MiniGrid-AdaptiveMapping-16x16-v0',
    entry_point='gym_minigrid.envs:AdaptiveMapping16x16'
)
