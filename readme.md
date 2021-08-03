A little project I have worked on.
I made two differnt versions out of a original version (_firstEverVersion.py)


Version 1: Sums up the differnt threads with temperary arrays

Version 2: All threads writes to the same varible. To avoid datarace each thread have a time interval where they can write.

------------------

Version 1 is a little bit faster but uses more memory but it has the advantage that you dont need to tune write time. (thinking of implementing a function for doing that)

Version 2 is slower uses way less memory.
