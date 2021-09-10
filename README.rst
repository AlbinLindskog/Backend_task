Backend task
************
Your task is to build a reliable, fault-tolerant integration towards Bindit, a digital, financial service that takes
your money.

Your task is to implement the function ´create_account_and_transfer´ that creates an account and transfer to Bindit,
stores the information in the db through the models ´Account´ and ´Transfer´, and most importantly; gracefully handles
any errors and problems that could occur.

To your help you have a python client that communicates with Bindit's API over HTTPS, ´BinditClient´. Note that you do
not need to implement BinditClient, it is a stub, intended to be mocked in tests. Likewise are the actual tests stubs,
you will need to write them based on what you think are important to test. You may need to write additional tests.

Spend as much or as little time as you would like, just take a note of how much time you did spend, as we will take
that into consideration when assessing your solution.

Good luck!
