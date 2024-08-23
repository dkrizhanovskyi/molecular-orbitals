Contributing Guide
==================

We are excited that you want to contribute to the Molecular Orbitals and Reaction Modeling project! By contributing, you help us make this library better for everyone. Below are guidelines for contributing to the project.

Getting Started
---------------

 **Fork the Repository**

1. Navigate to the `Molecular Orbitals repository`_ on GitHub.
2. Click the "Fork" button in the upper-right corner to create your copy of the repository.

 **Clone Your Fork**

Clone the repository to your local machine to start making changes:

.. code-block:: bash

    git clone https://github.com/dkrizhanovskyi/molecular_orbitals.git
    cd molecular_orbitals

 Set Up the Development Environment

1. **Create a Virtual Environment:**

   Create and activate a virtual environment to isolate your dependencies:

   .. code-block:: bash

       python -m venv venv
       source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. **Install Dependencies:**

   Install the necessary dependencies for development:

   .. code-block:: bash

       pip install -r requirements.txt

3. **Install the Package in Editable Mode:**

   This allows you to make changes to the source code and test them immediately:

   .. code-block:: bash

       pip install -e .

Coding Standards
----------------

To ensure consistency and readability across the codebase, please follow these guidelines:

1. **Code Style:**
   - Follow the PEP 8 style guide for Python code.
   - Use meaningful variable names and write clear, concise comments where necessary.
   - Ensure that lines of code do not exceed 79 characters.
   - Use tools like `black` for code formatting and `flake8` for linting.

2. **Docstrings:**
   - Write docstrings for all public classes, methods, and functions using the Google style guide for Python docstrings.
   - Example:

     .. code-block:: python

         def add(x, y):
             """
             Add two numbers together.

             Args:
                 x (int): The first number.
                 y (int): The second number.

             Returns:
                 int: The sum of x and y.
             """
             return x + y

3. **Testing:**
   - All new features and bug fixes should include unit tests.
   - We use `unittest` for testing. Ensure that your tests cover as many edge cases as possible.

4. **Commit Messages:**
   - Use clear and descriptive commit messages.
   - Prefix each commit message with a tag such as `FIX`, `FEAT`, `DOC`, etc., to indicate the type of change.

Making Changes
--------------

1. **Create a New Branch:**

   Always create a new branch for your work. Use a descriptive name for your branch:

   .. code-block:: bash

       git checkout -b feature-new-functionality

2. **Make Your Changes:**

   Implement your changes or add new features in the appropriate module(s). Make sure to write tests for any new functionality.

3. **Run Tests:**

   After making changes, run the tests to ensure everything works as expected:

   .. code-block:: bash

       python -m unittest discover

4. **Commit Your Changes:**

   Commit your changes with a meaningful message:

   .. code-block:: bash

       git commit -am 'FEAT: Add new functionality to calculate molecular energy'

5. **Push to Your Fork:**

   Push your changes to your GitHub fork:

   .. code-block:: bash

       git push origin feature-new-functionality

Submitting Changes
------------------

1. **Open a Pull Request:**

   Navigate to the original repository and click "New Pull Request." Compare your branch with the `main` branch of the original repository.

2. **Describe Your Changes:**

   In the pull request description, provide a brief explanation of your changes, why they are necessary, and any relevant context.

3. **Wait for Review:**

   Your pull request will be reviewed by the maintainers. Be open to feedback and ready to make adjustments if necessary.

Reporting Issues
----------------

If you encounter any bugs or have suggestions for new features, please open an issue on GitHub. Be as detailed as possible, providing steps to reproduce the issue and any relevant context.

Code of Conduct
---------------

We are committed to fostering a welcoming and respectful community. Please review our `Code of Conduct`_ before contributing.

Thank you for your contributions! Together, we can make Molecular Orbitals and Reaction Modeling an even better tool for the community.

.. _Molecular Orbitals repository: https://github.com/dkrizhanovskyi/molecular_orbitals
.. _Code of Conduct: code_of_conduct.rst
