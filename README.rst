Demonstrative Ansible playbook to deploy a Django project
=========================================================

For PyCon 8, Florence, April 2017
---------------------------------

The pycon8 folder includes a single Django project having a single app, a
single model and a single view. That project features the minimal setup
required to make it easy deployable with PIP and uses environment variables for
configuration.

The deploy folder contains a bunch of Ansible playbooks to configure the
servers and deploy the project using the following technologies:

* CentOS 7
* NGiNX
* uWSGI
* Python 3.6
* PostgreSQL

To install a local development environment clone the repo and create a virtual
environment with Python 3.6, then run the command:

.. code-block:: bash

    pip install -r requirements/local.txt

To create an `installation bundle`_ in the ``deploy/files`` folder you can run
the following command:

.. code-block:: bash

    invoke build --bundle

.. _`installation bundle`:
    https://pip.pypa.io/en/stable/user_guide/#installation-bundles

To create two local CentOS virtual machines use the provided Vagrantfile tested
with the VirtualBox provider:

.. code-block:: bash

    cd deploy
    vagrant up

To run the Ansible playbook a [virtual] environment with Python 2.7 is
required, until Ansible will be fully compatible with Python 3.

To configure the project for the local environment create and edit the dotenv
file in the ``deploy/files`` folder copying it from the ``.env.example`` file:

.. code-block:: bash

    cp .env.example deploy/files/pycon8.env

Then to deploy on the two local Vagrant boxes run the main playbook:

.. code-block:: bash

    ansible-playbook -i hosts/local all_servers.yml --extra-vars "pycon8=0.1.0" -vvv

The two CentOS 7 machines will be configured as web server and database server
and the project will be deployed using the installation bundle.

Using the ``git_repo`` variable it is possible to deploy in the target machines
directly from GIT and PyPI:

.. code-block:: yaml

    ansible-playbook -i hosts/local web_servers_git.yml --extra-vars "pycon8=master" -vvv

Using tags it is possible to perform a deploy, skipping all the configuration
steps and  without any internet access:

.. code-block:: bash

    ansible-playbook -i hosts/local web_servers.yml --extra-vars "pycon8=0.1.0" --tags=deploy -vvv
