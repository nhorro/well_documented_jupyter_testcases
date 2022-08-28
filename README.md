# Example project for automation of well-documented testcases

This project explores different ways of testing a dockerized service.

**Motivation**

Testing complex services such as very specific hardware simulators might require code that is difficult to understand, making the test a software itself that can be assessed only to the people working in it.

Jupyter notebooks provide a mechanism to control to the software being tested, while at the same time enriching the output and assertions with explanations, diagrams, and tables. The same code for the testcase can be used as a document for the software scope and as a starting point to debug when a problem is detected.

The problem with Jupyter notebooks are their lack of straightforward method to integrate with standard tests frameworks such as PyTests.

This project tries to combine the best of both worlds for a project.
A simple dockerized service for an RPC integer calculator is provided. See [instructions](services/calculator) to build and run.

**Requirmenents for well documented testcases**

- Automation.
- Summary of passing and failing testcases.
- Clear explanation of what is going on.
- Reduce effort of setting up an environment and writing additional code when debugging.

The following methods are compared:

- [Standard PyTests testcases](./pytest_testcases)
- [Jupyter testcases](./jupyter_testcases)
