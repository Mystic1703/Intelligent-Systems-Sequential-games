import math
import random

from agents import Agent


# Example agent, behaves randomly.
# ONLY StudentAgent and his descendants have a 0 id. ONLY one agent of this type must be present in a game.
# Agents from bots.py have successive ids in a range from 1 to number_of_bots.
class StudentAgent(Agent):
    def __init__(self, position, file_name):
        super().__init__(position, file_name)
        self.id = 0

    @staticmethod
    def kind():
        return '0'

    @staticmethod
    def form_pairs(curr_agent_id, state):
        actions = state.agents[curr_agent_id].get_legal_actions(state)
        states_list = [state.apply_action(curr_agent_id, act) for act in actions]
        coll = list(zip(actions, states_list))
        return coll

    @staticmethod
    def find_next_agent_id(state):
        last_played = state.last_agent_played_id
        for i in range(0, len(state.agents), 1):
            if state.agents[i].get_id() == last_played:
                next_index = (i + 1) % len(state.agents)
                return state.agents[next_index].get_id()
        return -1

    # Student shall override this method in derived classes.
    # This method should return one of the legal actions (from the Actions class) for the current state.
    # state - represents a state object.
    # max_levels - maximum depth in a tree search. If max_levels eq -1 than the tree search depth is unlimited.
    def get_next_action(self, state, max_levels):
        actions = self.get_legal_actions(state)  # equivalent of state.get_legal_actions(self.id)
        chosen_action = actions[random.randint(0, len(actions) - 1)]
        # Example of a new_state creation (for a chosen_action of a self.id agent):
        # new_state = state.apply_action(self.id, chosen_action)
        return chosen_action


class MinimaxAgent(StudentAgent):

    def get_next_action(self, state, max_levels):
        actions = state.get_legal_actions(self.id)
        next_move = None
        max_score = -math.inf
        for elem in actions:
            new_state = state.apply_action(self.id, elem)
            score = self.minimax(new_state, max_levels, 0)
            if max_score < score:
                max_score = score
                next_move = elem
        return next_move

    def minimax(self, state, max_levels, curr_depth):
        curr_agent_id = StudentAgent.find_next_agent_id(state)
        actions = state.get_legal_actions(curr_agent_id)
        if len(actions) == 0:
            if curr_agent_id == self.id:
                return -9
            else:
                return 9
        if curr_depth == max_levels:
            return len(actions) if curr_agent_id == self.id else -len(actions)
        if curr_agent_id == self.id:
            score = -math.inf
            for elem in actions:
                score = max(score, self.minimax(state.apply_action(curr_agent_id, elem), max_levels, curr_depth + 1))
            return score
        else:
            score = math.inf
            for elem in actions:
                score = min(score, self.minimax(state.apply_action(curr_agent_id, elem), max_levels, curr_depth + 1))
            return score


class MinimaxABAgent(StudentAgent):

    def get_next_action(self, state, max_levels):
        best_move = None
        max_score = -math.inf
        alfa = -math.inf
        beta = math.inf
        actions = state.get_legal_actions(self.id)
        for elem in actions:
            new_state = state.apply_action(self.id, elem)
            score = self.minimax_ab(new_state, alfa, beta, max_levels, 0)
            if max_score < score:
                max_score = score
                best_move = elem
        return best_move

    def minimax_ab(self, state, alfa, beta, max_levels, curr_depth):
        curr_agent_id = StudentAgent.find_next_agent_id(state)
        actions = state.get_legal_actions(curr_agent_id)
        if len(actions) == 0:
            if curr_agent_id == self.id:
                return -9
            else:
                return 9
        if curr_depth == max_levels:
            return len(actions) if curr_agent_id == self.id else -len(actions)
        if curr_agent_id == self.id:
            score = -math.inf
            for elem in actions:
                score = max(score, self.minimax_ab(state.apply_action(curr_agent_id, elem), alfa, beta, max_levels, curr_depth + 1))
                alfa = max(score, alfa)
                if alfa >= beta:
                    break
            return score
        else:
            score = math.inf
            for elem in actions:
                score = min(score, self.minimax_ab(state.apply_action(curr_agent_id, elem), alfa, beta, max_levels, curr_depth + 1))
                beta = min(score, beta)
                if alfa >= beta:
                    break
            return score


class ExpectAgent(StudentAgent):

    def get_next_action(self, state, max_levels):
        actions = state.get_legal_actions(self.id)
        max_score = -math.inf
        best_move = None
        for elem in actions:
            new_state = state.apply_action(self.id, elem)
            score = self.expectimax(new_state, max_levels, 0)
            if max_score < score:
                max_score = score
                best_move = elem
        return best_move

    def expectimax(self, state, max_levels, curr_depth):
        curr_agent_id = StudentAgent.find_next_agent_id(state)
        actions = state.get_legal_actions(curr_agent_id)
        if len(actions) == 0:
            if curr_agent_id == self.id:
                return -9
            else:
                return 9
        if curr_depth == max_levels:
            return len(actions) if curr_agent_id == self.id else -len(actions)
        score = -math.inf if curr_agent_id == self.id else 0
        if curr_agent_id == self.id:
            for elem in actions:
                score = max(score, self.expectimax(state.apply_action(curr_agent_id, elem), max_levels, curr_depth + 1))
            return score
        else: #chance node
            probability = 1.0 / len(actions)
            for elem in actions:
                node_score = self.expectimax(state.apply_action(curr_agent_id, elem), max_levels, curr_depth + 1)
                score += probability * node_score
            return score


class MaxNAgent(StudentAgent):

    def get_next_action(self, state, max_levels):
        actions = state.get_legal_actions(self.id)
        next_move = None
        max_score = -math.inf
        for elem in actions:
            new_state = state.apply_action(self.id, elem)
            score = self.minimax_n(new_state, max_levels, 0)
            if max_score < score:
                max_score = score
                next_move = elem
        return next_move

    def minimax_n(self, state, max_levels, curr_depth):
        curr_agent_id = StudentAgent.find_next_agent_id(state)
        actions = state.get_legal_actions(curr_agent_id)
        if len(actions) == 0:
            if curr_agent_id == self.id:
                return -9
            else:
                return 9
        if curr_depth == max_levels:
            return len(actions) if curr_agent_id == self.id else -len(actions)
        if curr_agent_id == self.id:
            score = -math.inf
            for elem in actions:
                score = max(score, self.minimax_n(state.apply_action(curr_agent_id, elem), max_levels, curr_depth + 1))
            return score
        else:
            score = math.inf
            for elem in actions:
                score = min(score, self.minimax_n(state.apply_action(curr_agent_id, elem), max_levels, curr_depth + 1))
            return score
