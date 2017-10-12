# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Justin Rohweller Pac-man project 1
# I used the internet to figure out how to delete the last item from my array:
# newPathGuide = newPathGuide[:-1]


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "STARTDEPTHFIRSTSEARCH"
    #print ""
    #print ""

    from game import Directions
    from util import Stack
    myFringe = Stack()
    exploredStates = set()
   
    
    
    startState = [[problem.getStartState(), -1], []]
    myFringe.push(startState)
    if (problem.isGoalState(problem.getStartState())):
      
      return Directions.STOP
    #loop forever (only return escapes.)
    while (True):
      #if fringe is empty, we failed to add another item.
      if (myFringe.isEmpty()):
        #print 'failure fringe is empty.'
        return ['failure']
      #if not empty, take most recent one, check if goal, return how got there.
      else:
        poppedState = myFringe.pop()
        if (problem.isGoalState(poppedState[0][0])):
          answerArray = []
          #for length of array, #print poppedStates directionArray,
          # populate answerArray with Directions to reach goal.
          for i in range(0, len(poppedState[1])):
            if (poppedState[1][i] == "North"):
              answerArray.append(Directions.NORTH)
            if (poppedState[1][i] == "South"):
              answerArray.append(Directions.SOUTH)
            if (poppedState[1][i] == "East"):
              answerArray.append(Directions.EAST)
            if (poppedState[1][i] == "West"):
              answerArray.append(Directions.WEST)
          #print len(answerArray)
          return answerArray
        #if poppedState not in fringe (shouldn't be we just popped it.) or exploredState (should not explore repeated states)
        # then add it to explored, and add children to the fringe.
        if (not(poppedState[0][0] in exploredStates)):
          exploredStates.add(poppedState[0][0])
          #print "NODE EXPLORED: ", poppedState[0][0]
          #call successor only on coordinates.
          newSuccessors = problem.getSuccessors(poppedState[0][0])
          newPathGuide = poppedState[1]
      #get all successors, put them all in fringe. with how to get there.
          for i in range(0, len(newSuccessors)):
            newPathGuide.append(newSuccessors[i][1])
            nextNode = [newSuccessors[i], newPathGuide]
            myFringe.push(nextNode)
            newPathGuide = newPathGuide[:-1]

    #print ""
    #print ""
    #print "ENDDEPTHFIRSTSEARCH"

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print "STARTBREADTHFIRSTSEARCH"
    #print ""
    #print ""

    from game import Directions
    from util import Queue
    myFringe = Queue()
    exploredStates = set()
   
    
    
    startState = [[problem.getStartState(), -1], []]
    myFringe.push(startState)
    if (problem.isGoalState(problem.getStartState())):
      
      return Directions.STOP
    #loop forever (only return escapes.)
    while (True):
      #if fringe is empty, we failed to add another item.
      if (myFringe.isEmpty()):
        #print 'failure fringe is empty.'
        return ['failure']
      #if not empty, take most recent one, check if goal, return how got there.
      else:
        poppedState = myFringe.pop()
        if (problem.isGoalState(poppedState[0][0])):
          answerArray = []
          #for length of array, #print poppedStates directionArray,
          # populate answerArray with Directions to reach goal.
          for i in range(0, len(poppedState[1])):
            if (poppedState[1][i] == "North"):
              answerArray.append(Directions.NORTH)
            if (poppedState[1][i] == "South"):
              answerArray.append(Directions.SOUTH)
            if (poppedState[1][i] == "East"):
              answerArray.append(Directions.EAST)
            if (poppedState[1][i] == "West"):
              answerArray.append(Directions.WEST)
          #print len(answerArray)
          return answerArray
        #if poppedState not in fringe (shouldn't be we just popped it.) or exploredState (should not explore repeated states)
        # then add it to explored, and add children to the fringe.
        if (not(poppedState[0][0] in exploredStates)):
          exploredStates.add(poppedState[0][0])
          #print "NODE EXPLORED: ", poppedState[0][0]
          #call successor only on coordinates.
          newSuccessors = problem.getSuccessors(poppedState[0][0])
          newPathGuide = poppedState[1]
      #get all successors, put them all in fringe. with how to get there.
          for i in range(0, len(newSuccessors)):
            newPathGuide.append(newSuccessors[i][1])
            nextNode = [newSuccessors[i], newPathGuide]
            myFringe.push(nextNode)
            newPathGuide = newPathGuide[:-1]

    #print ""
    #print ""
    #print "ENDBREADTHFIRSTSEARCH"

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #print "STARTUNIFORMCOSTSEARCH"
    #print ""
    #print ""

    from game import Directions
    from util import PriorityQueue
    myFringe = PriorityQueue()
    exploredStates = set()
   
    
    
    startState = [[problem.getStartState(), 0], [], 0]
    myFringe.push(startState, 0)
    if (problem.isGoalState(problem.getStartState())):
      return Directions.STOP
    #loop forever (only return escapes.)
    while (True):
      #if fringe is empty, we failed to add another item.
      if (myFringe.isEmpty()):
        #print 'failure fringe is empty.'
        return ['failure']
      #if not empty, take most recent one, check if goal, return how got there.
      else:
        poppedState = myFringe.pop()
        if (problem.isGoalState(poppedState[0][0])):
          answerArray = []
          #for length of array, ##print poppedStates directionArray,
          # populate answerArray with Directions to reach goal.
          for i in range(0, len(poppedState[1])):
            if (poppedState[1][i] == "North"):
              answerArray.append(Directions.NORTH)
            if (poppedState[1][i] == "South"):
              answerArray.append(Directions.SOUTH)
            if (poppedState[1][i] == "East"):
              answerArray.append(Directions.EAST)
            if (poppedState[1][i] == "West"):
              answerArray.append(Directions.WEST)
          #print len(answerArray)
          return answerArray
        #if poppedState not in fringe (shouldn't be we just popped it.) or exploredState (should not explore repeated states)
        # then add it to explored, and add children to the fringe.
        if (not(poppedState[0][0] in exploredStates)):
          exploredStates.add(poppedState[0][0])
          # print "NODE EXPLORED: ", poppedState[0][0]
          #call successor only on coordinates.
          newSuccessors = problem.getSuccessors(poppedState[0][0])
          newPathGuide = poppedState[1]
          # print poppedState[2]
          prevCost = poppedState[2]
      #get all successors, put them all in fringe. with how to get there. and how much it cost.
          for i in range(0, len(newSuccessors)):
            newPathGuide.append(newSuccessors[i][1])
            # print newSuccessors[i][2]
            newPathCost = prevCost + newSuccessors[i][2]

            nextNode = [newSuccessors[i], newPathGuide, newPathCost]
            myFringe.push(nextNode, newPathCost)
            newPathGuide = newPathGuide[:-1]

    #print ""
    #print ""
    #print "ENDUNIFORMCOSTSEARCH"

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #print "STARTASTARSEARCH"
    #print ""
    #print ""
    
    from game import Directions
    from util import PriorityQueue
    myFringe = PriorityQueue()
    exploredStates = set()
    # heuristic(problem.getStartState(), problem)
    # print "HEURISTIC: ", heuristic(problem.getStartState(), problem)
    
    
    
    startState = [[problem.getStartState(), 0], [], 0]
    myFringe.push(startState, heuristic(problem.getStartState(), problem))
    # print "HEURISTIC: ", heuristic(problem.getStartState(), problem)
    if (problem.isGoalState(problem.getStartState())):
      
      return Directions.STOP
    #loop forever (only return escapes.)
    while (True):
      #if fringe is empty, we failed to add another item.
      if (myFringe.isEmpty()):
        #print 'failure fringe is empty.'
        return ['failure']
      #if not empty, take most recent one, check if goal, return how got there.
      else:
        poppedState = myFringe.pop()
        if (problem.isGoalState(poppedState[0][0])):
          answerArray = []
          #for length of array, #print poppedStates directionArray,
          # populate answerArray with Directions to reach goal.
          for i in range(0, len(poppedState[1])):
            if (poppedState[1][i] == "North"):
              answerArray.append(Directions.NORTH)
            if (poppedState[1][i] == "South"):
              answerArray.append(Directions.SOUTH)
            if (poppedState[1][i] == "East"):
              answerArray.append(Directions.EAST)
            if (poppedState[1][i] == "West"):
              answerArray.append(Directions.WEST)
          #print len(answerArray)
          return answerArray
        #if poppedState not in fringe (shouldn't be we just popped it.) or exploredState (should not explore repeated states)
        # then add it to explored, and add children to the fringe.
        if (not(poppedState[0][0] in exploredStates)):
          exploredStates.add(poppedState[0][0])
          #it is popping off the wrong node.
          # print "NODE EXPLORED: ", poppedState[0][0]
          #call successor only on coordinates.
          newSuccessors = problem.getSuccessors(poppedState[0][0])
          newPathGuide = poppedState[1]
      #get all successors, put them all in fringe. with how to get there.
          prevCost = poppedState[2] 

          for i in range(0, len(newSuccessors)):
            newPathGuide.append(newSuccessors[i][1])
            # nextNodeValue = (len(poppedState[1])+nextNode[0][2])+(heuristic(nextNode[0][0], problem))
            # print "2nd: ", nextNode[0][0]

            newPathCost = prevCost + newSuccessors[i][2] + heuristic(newSuccessors[i][0], problem)
            nextNode = [newSuccessors[i], newPathGuide, newPathCost]
            myFringe.push(nextNode, newPathCost)
            newPathGuide = newPathGuide[:-1]

    #print ""
    #print ""
    #print "ENDASTARSEARCH"


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
