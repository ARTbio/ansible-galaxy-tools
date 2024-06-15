This Ansible role is for automated installation of tools from a Tool Shed into
Galaxy.

When run, this role will create an execution environment, install
[ephemeris](https://github.com/galaxyproject/ephemeris) and invoke the
shed-install command to install desired tools into Galaxy. The list of tools to
install is provided in `files/tool_list.yaml` file.

Usage
-----
To use the role, you need to create a playbook and include the role in it. A
sample playbook is available [here](https://github.com/afgane/galaxy-tools-playbook)
that will get you up and running in minutes.

Variables
---------
### Required variables ###
Warning ! warning !
tool_admin_user name, email, and password are now hardcoded in the
python script `manage_bootstrap_user.py`, for the sake of simplicity.
A new api key is simply generated for this user, each the playbook is run.

### Optional variables ###
See `defaults/main.yml` for the available variables and their defaults.

### Control flow variables ###
The following variables can be set to either `yes` or `no` to indicate if the
given part of the role should be executed:

 - `galaxy_tools_install_tools`: (default: `yes`) whether or not to run the
   tools installation script
