Add your answers to the Algorithms exercises here.

Exercise 1)

    a) This will always be O(n). 
        at a = 0, a = n^2
        at a = n^2, a = n^2 + n^2 -> 2n^2
        at a = 2n^2, a = 2n^2 + n^2 -> 3n^2

        to check

        n = 1

        a = 0 ; a = 1; 1 = 1 // stop

        n = 2 

        a = 0; a = 4; 4 < 8
        a = 2; a = 4 + 4 ; 8 = 8

        n = 3

        a = 0; a = 9; 9 < 27 
        a = 9; a = 9 + 9 = 18; 18 < 27
        a = 18; a = 9 + 9 + 9; 27 = 27

        n = 4

        a = 0; a = 16; 16 < 64
        a = 16; a = 16 + 16 = 32; 32 < 64
        a = 32; a = 32 + 16 = 48; 48 < 64
        a = 48; a = 48 + 16 = 64; 64 = 64 

        It will take n steps to break the while loop. The while loop's constraint
        is a strong determinant of how long the step size will be since it determines when the while loop will end. 

    b) This algorithim is O(n^4). There is a nested for loop in this operation.

        - The first for loop will run n times.
        - The second for loop, which is nested, runs i+1 times, or n-1 times, which is equivalent of n.
        - The third for loop, which is nested, runs j+1 times, or n-2 times, which is the equivalent of n. 
        - The forth for loop, which is nested, runs k+1 times, or n-3 times, which is the equivalent of n. 

    Nested for loops always lead to a exponential step size, due to the fact that we have to run an additional n steps in a nested for loop per nTh iteration of a for loop. This is a product that works.

    c) O(1), since this is a true or false statement that only runs 1 step. There are no additional frames needed to run this function.

Exercise 2) (looks like binary search)

This looks like a algorithim determining the pivot point, or floor f, where the eggs won't fall. Any floor less than f, the eggs won't break. Any floor greater 
than f, the eggs will break. 

We don't know what the value of floor f is. But, to minimize, we need to sort the amount of eggs that are breaking per floor in a sorted array. The floor f acts like an index of a sorted array. 

We first drop some eggs at a random floor i. We then drop the eggs at another random floor j.

If floor[i] drops more eggs than floor[j], then we begin dropping eggs at floors less than j. We ignore dropping eggs at floors i or above, since we've determined that floors i or above will lead us to breaking more eggs, which is the opposite of our goal. We assume floors j or less will break less egs.  

We continue this step, this divide and conquer method (which reduces how many floors we need to test, or input size), until we've found an optimal floor f where the eggs break the least, or none at all. 

This is a O(log(n)) time complexity, since we are constantly halving the input size by half (n^(1/2)) each time we divide and conquer.  