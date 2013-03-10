import random
import math

class GameTree():

    # constructor
    def __init__(self, param):
        self.reset_count()
        if type(param) == list: # given a list of leaf values
            self.k = int(math.log(len(param), 2)//2)
            self.leaf_list = param
        else: # construct a random list of leaf values
            self.k = param
            self.leaf_list = []
            for i in range(2**(2*self.k)):
                self.leaf_list.append(round(random.random()))

    # These functions help keep count of how many leaves have been examined

    # resets the count to zero
    def reset_count(self):
        self.leaf_read_count = 0

    # returns the count
    def get_count(self):
        return self.leaf_read_count


    # returns a leaf value of the game tree
    def get_leaf(self, param):
        if type(param) == int: # given an integer index into the leaf_list
            if param >= 0 and param < 2**(2*self.k):
                self.leaf_read_count = self.leaf_read_count + 1
                return self.leaf_list[param]
        if type(param) == list: # given a left-right path; 0==left, 1==right
            index = 0
            for i in param:
                index = index*2 + i
            self.leaf_read_count = self.leaf_read_count + 1
            return self.leaf_list[index]

    # deterministic evaluation algorithm
    def evaluate1(self):
        return self.__recursive_evaluate1([])

    def __recursive_evaluate1(self, tree_path):
        if len(tree_path) == 2 * self.k: # have a path of depth 2k, so a leaf
            return self.get_leaf(tree_path)
        elif len(tree_path) < 2 * self.k:
            # evaluate the left subtree recursively
            left = self.__recursive_evaluate1(tree_path + [0])
            # evaluate the right subtree recursively
            right = self.__recursive_evaluate1(tree_path + [1])
            
            if len(tree_path) % 2 == 0:  # node corresponds to AND
                return left * right
            else:  # node corresponds to OR
                return left + right - (left * right)

def main():
    k = eval(input("Enter number of turns (depth/2): "))
    T = GameTree(k)
    if 'y' in input("Print tree? "):
        print(T.leaf_list)
        input("Hit return to continue")
    answer = T.evaluate1()
    count = T.get_count()
    print("The tree evaluates to %d after reading %d leaf values." % (answer, count))

if __name__ == '__main__':
    main()
