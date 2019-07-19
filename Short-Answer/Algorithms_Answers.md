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
