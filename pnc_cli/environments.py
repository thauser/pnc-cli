from argh import arg

from six import iteritems
from pnc_cli.swagger_client import BuildEnvironmentRest
from pnc_cli.swagger_client import EnvironmentsApi
from pnc_cli import utils


envs_api = EnvironmentsApi(utils.get_api_client())

__author__ = 'thauser'


def _create_environment_object(**kwargs):
    created_environment = BuildEnvironmentRest()
    for key, value in iteritems(kwargs):
        if value:
            if key == 'build_type':
                setattr(created_environment, key, value.upper())
            else:
                setattr(created_environment, key, value)
    return created_environment

def _get_environment_id_by_name(name):
    """
    Return the ID of a BuildEnvironment given the name
    """
    for env in envs_api.get_all().content:
        if env.name == name:
            return env.id
    return None


def _environment_exists(search_id):
    """
    Returns true if search_id is a valid BuildEnvironment id.
    """
    existing_ids = [str(x.id) for x in envs_api.get_all().content]
    return str(search_id) in existing_ids


def get_environment_id(search_id, name):
    """
    Given either a name or id, checks for BuildEnvironment existence and returns the valid id, or prints a message otherwise
    """
    if search_id:
        if not _environment_exists(search_id):
            print("No environment with ID {} exists.".format(search_id))
            return
        found_id = search_id
    elif name:
        found_id = _get_environment_id_by_name(name)
        if not found_id:
            print("No environment with name {} exists.".format(name))
            return
    else:
        print("Either a BuildEnvironment name or ID is required.")
        return
    return found_id


@arg("name", help="Unique name of the BuildEnvironment")
@arg("-d", "--description", help="Description of the BuildEnvironment.")
@arg("-bt", "--build-type", help="Type of build for the new BuildEnvironment.")
@arg("-iid", "--image-id", help="ID of the Docker image for this BuildEnvironment.")
@arg("-iru", "--image-repository-url", help="URL for the Docker repository in which the image resides.")
def create_environment(**kwargs):
    """
    Create a new Environment
    """
    environment = _create_environment_object(**kwargs)
    response = utils.checked_api_call(envs_api, 'create_new', body=environment)
    if response:
        return response.content


@arg("id", help="ID of the environment to update.")
@arg("-bt", "--build-type", help="Updated type of build for the new BuildEnvironment.")
@arg("-d", "--description", help="Updated description of the BuildEnvironment.")
@arg("-iid", "--image-id", help="Updated ID of the Docker image for this BuildEnvironment.")
@arg("-iru", "--image-repository-url", help="Updated URL for the Docker repository in which the image resides.")
@arg("-n", "--name", help="Updated unique name of the BuildEnvironment")
def update_environment(id, **kwargs):
    """
    Update a BuildEnvironment with new information
    """
    if not _environment_exists(id):
        print("No environment with id {} exists.".format(id))
        return

    to_update = envs_api.get_specific(id=id).content

    for key,value in iteritems(kwargs):
        if value:
            if key == 'build_type':
                setattr(to_update, key, value.upper())
            else:
                setattr(to_update, key, value)

    response = utils.checked_api_call(
        envs_api, 'update', id=id, body=to_update)
    if response:
        return response.content


@arg("-i", "--id", help="ID of the environment to delete.")
@arg("-n", "--name", help="Name of the environment to delete.")
def delete_environment(id=None, name=None):
    """
    Delete an environment by name or ID
    """
    found_id = get_environment_id(id, name)
    if not found_id:
        return
    response = utils.checked_api_call(envs_api, 'delete', id=found_id)
    return response


@arg("-i", "--id", help="ID of the environment to retrieve.")
@arg("-n", "--name", help="Name of the environment to retrieve.")
def get_environment(id=None, name=None):
    """
    Get a specific Environment by name or ID
    """
    search_id = get_environment_id(id, name)
    if not search_id:
        return
    response = utils.checked_api_call(envs_api, 'get_specific', id=search_id)
    if response:
        return response.content

@arg("-p", "--page-size", help="Limit the amount of product releases returned")
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_environments(page_size=200, sort="", q=""):
    """
    List all Environments
    """
    response = utils.checked_api_call(envs_api, 'get_all', page_size=page_size, sort=sort, q=q)
    if response:
        return response.content
