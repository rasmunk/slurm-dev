import os
from jhub.mount import SSHFSMounter

c = get_config()

c.JupyterHub.spawner_class = 'jhub.SwarmSpawner'

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.base_url = '/slurm'

mounts = [{'type': 'bind',
           'source': '/home/rasmus/repos/slurm-dev/config/slurm.conf',
           'target': '/etc/slurm/slurm.conf'},
          {'type': 'bind',
           'source': '/home/rasmus/repos/slurm-dev/munge/munge.key',
           'target': '/etc/munge/munge.key'}]

# First pulls can be really slow, so let's give it a big timeout
c.SwarmSpawner.start_timeout = 60 * 15

c.SwarmSpawner.jupyterhub_service_name = 'slurm-dev_jupyterhub'

c.SwarmSpawner.networks = ["slurm-dev_slurm"]

notebook_dir = os.environ.get('NOTEBOOK_DIR') or '/home/jovyan/work/'
c.SwarmSpawner.notebook_dir = notebook_dir

# 'args' is the command to run inside the service
c.SwarmSpawner.container_spec = {
    'env': {'JUPYTER_ENABLE_LAB': '1',
            'TZ': 'Europe/Copenhagen'}
}

c.SwarmSpawner.use_user_options = True

c.SwarmSpawner.dockerimages = [
    {'name': 'base-notebook',
     'image': 'nielsbohr/slurm-notebook:edge',
     'mounts': mounts}
]

# Authenticator -> remote user header
c.JupyterHub.authenticator_class = 'jhubauthenticators.DummyAuthenticator'
c.DummyAuthenticator.password = 'password'

# Pass the encoded username to the spawner
c.Authenticator.enable_auth_state = False
