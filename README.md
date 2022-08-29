# Example project for automation of well-documented testcases

This project explores different ways of testing a dockerized service.

**Motivation**

Testing complex services such as very specific hardware simulators might require code that is difficult to understand, making the test a software itself that can be assessed only by the people working on it that possess the specific knowledge of the internals.

Jupyter notebooks provide a mechanism to control the software being tested, while at the same time enriching the results and assertions with explanations, diagrams, and tables. The same code for the testcase can be used as a document that:

- describes the software scope
- serves as a user manual
- can be used as a starting point to debug when a problem is detected.

The caveat with Jupyter notebooks is their lack of straightforward method to integrate with standard tests frameworks such as PyTests. Reporting and automation might also require additional steps and non mature libraries.

This project tries to combine the best of both worlds.
A simple dockerized service for an RPC integer calculator is provided. See [instructions](services/calculator) to build and run.

**Requirements for well documented testcases**

- Automation and CI integration.
- Summary of passing and failing testcases XUnit or similar, HTML report, CI.
- Clear explanation of what is going on: tables, plots, text, packet formats, references, etc.
- Reduce effort of setting up an environment and writing additional code when debugging. That is, the testcase should be a program that can be used with minor modifications to advance in the debugging.

The following methods are compared:

- [Standard PyTests testcases](./pytest_testcases)
- [Jupyter testcases](./jupyter_testcases)

## Standard PyTest testcases

WIP.

## Jupyter PyTest Testcases

WIP.
