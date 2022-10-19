# ansible-collection-download
On RedHat page https://access.redhat.com/articles/3642632 they have a curated list of Ansible Supported Collections.
This python script will download the collections mentioned on this site. Ansible >=2.12 needs to be installed, because
of the ansible-galaxy collection download option that is being used.

After download, these collections can be imported in an on-premise (without internet connection) automation-hub.
For instance using RedHat COP Automation Hub Configuration Collection - https://github.com/redhat-cop/ah_configuration 