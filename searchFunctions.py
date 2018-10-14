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
    return [s, s, w, s, w, w, s, w]


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
    current_state = problem.getStartstate()
    next_states = problem.getNextStates(current_state)
    for state in next_states:
        next_next_states = problem.getNextStates(state)


def calculate_walls(state, problem):
    next_states = problem.getNextStates(state)
    all_directions = ['North', 'East', 'South', 'West']
    next_state_directions = next_states[0]
    for state in next_states:
        directions = state[1]





    # print "Start's next states:", problem.getNextStates(problem.getStartState())
    # base_next_states = problem.getNextStates(problem.getStartState())
    # print "next_state array:", base_next_states
    # print "in nextstate:", base_next_states[0]
    # print "next_state array:", base_next_states
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
