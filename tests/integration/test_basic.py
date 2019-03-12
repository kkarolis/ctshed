"""Most simple integration testing."""
import unittest
import uuid
import tempfile
import shutil
import os
import mock

from ctshed import get_tool_options, install


def random_namespace():
    return uuid.uuid4().hex[:7]


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    @mock.patch('ctshed.utils.run_docker_build')
    def test_tool_namespace(self, docker_build):
        cli_options = {
            'source': 'biocontainers/blast:2.2.31',
            'cmd': None,
            'packages': None,
            'path': self.tmp_dir,
        }
        namespace = random_namespace()
        options = get_tool_options(namespace, cli_options)
        executable_path = install(namespace, options)
        self.assertTrue(docker_build.called)
        self.assertTrue(os.path.exists(executable_path))

    @mock.patch('ctshed.utils.run_docker_build')
    def test_cmd_namespace(self, docker_build):
        cli_options = {
            'cmd': 'curl',
            'packages': 'curl',
            'path': self.tmp_dir,
        }
        namespace = random_namespace()
        options = get_tool_options(namespace, cli_options)
        executable_path = install(namespace, options)
        self.assertTrue(docker_build.called)
        self.assertTrue(os.path.exists(executable_path))
