class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def moveAllTheWayToTheLeft(self):
        for i in range(self._position, 0, -1):
            self._position -= 1
            self._time += 1

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # step 1) turn on the light - this keeps track of whether an object has swapped or not. 
        self.set_light_on() 

        # step 2) pick up your item and begin moving 

        # step 2) begin moving from left to right, and end swapping once you hit the end of the list
        while self.light_is_on():

            self.swap_item()
            self.move_right()

            # turn off the light first and loop through  
            self.set_light_off()
            while self.can_move_right:

                if self.can_move_right:

                    if self.compare_item() == 1:
                        self.swap_item()
                        self.move_left()

                        # put that item in the front in the right place
                        self.swap_item()
                        # go back to your original position
                        self.move_right()

                        # keep the light on to let the user know that this has been swapped at this iteration of this list. 
                        self.set_light_on()
                    else:
                        # drop the item where you first picked it up
                        self.move_left()
                        self.swap_item()

                        # go back to your original position  
                        self.move_right()

                        # note, if this step always happens, the light will always be off and the swappinng will end. 
                    
                    # move to next position
                    self.move_right()

                else:
                    self.moveAllTheWayToTheLeft()




    # plan:

    # use recursion, make the robot work less harder (ideal for large input sizes) by moving less, since
    # these sort methods will require the robot to move less, saving energy?

    # merge sort
    # quick sort

    # or use iterative sorts (ideal for small input sizes):
    
    #  insertion sort,
    #  bubble sort, 
    #  selection sort

    # lets use bubble sort 
    
    # first, pick up the first item and begin moving right.
    # second, turn on the light and compare the item you are at, with the item one is currently holding

    # if the item you have is greater than what is in front of you, swap the positions asap, move the item to the left. 
    # else put the object back where you picked it up, and pick up the new object on the position where you are at, and continue comparing

    # do this until you've 

d = SortingRobot([8,5,1])
print(d.sort())

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)