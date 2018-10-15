import util

from game import Directions

UNREACHABLE_GOAL_STATE = [Directions.STOP]


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """

    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    right = Directions.RIGHT
    print "this is right direction : " + Directions.RIGHT[w]
    return ['South', 'South', 'West', 'South', 'West', 'West', 'South', 'West']


def right_hand_maze_search(problem):
    """
    Q1: Search using right hand rule

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's next states:", problem.getNextStates(problem.getStartState())

    :param problem: instance of SearchProblem
    :return: list of actions
    """
    "*** YOUR CODE HERE ***"
    print "search called"
    path_to_goal = ['West']
    pacman_direction = path_to_goal[len(path_to_goal)-2]
    current_state = problem.getStartState()
    print "current_state:", current_state
    next_states = problem.getNextStates(current_state)
    print "next_states:", next_states
    for state in next_states:
        print "state in next_states:", state
        print "state[0]:", state[0]
        next_state_walls = calculate_walls(state[0], problem)
        for wall in next_state_walls:
            print "right of next position:", Directions.RIGHT[state[1]]
            if Directions.RIGHT[state[1]] == wall and pacman_direction == state[1]:
                path_to_goal.append(state[1])
                if problem.isGoalState(state[1]):
                    goal_reached = True
                print "path_to_goal", path_to_goal
    print "path_to_goal:", path_to_goal
    # return path_to_goal


def calculate_walls(state, problem):
    current_state_next_states = problem.getNextStates(state)
    print "current_state_next_states:", current_state_next_states
    all_directions = ['North', 'East', 'South', 'West']
    current_state_directions = get_state_directions(current_state_next_states)
    wall_directions = set(all_directions) - set(current_state_directions)
    print "wall_directions:", wall_directions
    return wall_directions


def get_state_directions(state_array):
    state_directions = []
    for state in state_array:
        state_directions.append(state[1])
        print "state_directions:", state_directions
    return state_directions






    # base_next_states = problem.getNextStates(problem.getStartState())
    # for state in base_next_states:
    #     print "state:", state
    #     print "state[0]:", state[0]
    #     print "next next states:", problem.getNextStates(state[0])
    # s = Directions.SOUTH
    # w = Directions.WEST
    # return [s, s, w, s, w, w, s, w]
    # util.raiseNotDefined()


def dfs(problem):
    """
    Q2: Search the deepest nodes in the search tree first.
    """

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def bfs(problem):
    """
    Q3: Search the shallowest nodes in the search tree first.
    """

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def ucs(problem):
    """
    Q6: Search the node of least total cost first.
    """

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
