import os
from jhub.mount import SSHFSMounter

c = get_config()

c.JupyterHub.spawner_class = 'jhub.SwarmSpawner'

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.base_url = '/slurm'

# First pulls can be really slow, so let's give it a big timeout
c.SwarmSpawner.start_timeout = 60 * 15

c.SwarmSpawner.jupyterhub_service_name = 'slurm-dev'

c.SwarmSpawner.networks = ["slurm-dev_default"]

notebook_dir = os.environ.get('NOTEBOOK_DIR') or '/home/jovyan/work/'
c.SwarmSpawner.notebook_dir = notebook_dir


# 'args' is the command to run inside the service
c.SwarmSpawner.container_spec = {
    'args': ['/usr/local/bin/start-singleuser.sh',
             '--NotebookApp.ip=0.0.0.0',
             '--NotebookApp.port=8888'],
    'env': {'JUPYTER_ENABLE_LAB': '1'}
}

# Before the user can select which image to spawn,
# user_options has to be enabled
c.SwarmSpawner.use_user_options = True

# Available docker images the user can spawn
c.SwarmSpawner.dockerimages = [
    {'image': 'nielsbohr/slurm-notebook:latest',
     'name': 'Base Image'
     }
]

# Authenticator -> remote user header
c.JupyterHub.authenticator_class = 'jhubauthenticators.DummyAuthenticator'
c.DummyAuthenticator.password = 'password'

# Pass the encoded username to the spawner
c.Authenticator.enable_auth_state = False

