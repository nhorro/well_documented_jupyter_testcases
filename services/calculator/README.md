Example service: calculator
===========================

This is an example service of an RPC integer calculator written in [FastAPI](https://fastapi.tiangolo.com/) that provides the following methods:

- `/isum`: integer addition.
- `/isub`: integer substraction.
- `/imul`: integer product.
- `/idiv`: integer division.

All methods expect two integer operands: `a` and `b` supplied as GET parameters.

Build docker:

~~~bash
./build.sh
~~~

Run docker with default port (80):

~~~bash
./run.sh
~~~
