.. _contribute:

Contribute
============

Any contribution to this project is more than welcomed ! As small or big as they
are, contributions are what will make this project better. There is still a lot
to do : reporting bugs, proposing fixes, new features, helping with the
documentation...

If it's your first contribution, no worries. As long as you follow the guidelines,
everything is going to be fine :)

Open an issue
-------------

If you spot a bug or want to propose an enhancement, you can open an issue on Github.
Please make sure to avoid duplicates and explain clearly what is your need.


Coding guidelines
-----------------

This project wants to stay close to the standard and was inspired by Flask_, Eve_
and Requests_ code quality.

My advice would be to follow Flask styleguide_ and to respect flake8.


Creating a pull request
-----------------------

- Fork the project
- Install dev dependencies and package
- checkout a new branch based on dev
- (Soon optional) Install Docker tools
- Make your change and run the test suite in a container
- Be sure to respect flake8 conventions
- Run the entire test suite before commiting
- If your commit fixes an open issue, reference it in the commit message (#15).
- Commit with a proper commit message
- Open a PR using this description structure
- Travis (CI) will run on your branch
- If the PR is accepted, it will be merged into the dev branch and then released.

.. _Flask: http://flask.pocoo.org/
.. _Eve: http://python-eve.org
.. _Requests: http://docs.python-requests.org/en/latest/
.. _styleguide: http://flask.pocoo.org/docs/0.10/styleguide/
