import os
import unittest
import mock


class Utils(object):
    
    @classmethod
    def mount_samba_share(cls, a, b, c, share_name):
        """
        Mount the share and return the mount point
        """
        raise Exception("Couldn't mount {}".format(share_name))


class TestMount(unittest.TestCase):

    mount_mock = None

    def setUp(self):
        super(TestMount, self).setUp()
        mount_patcher = mock.patch('test_mount.Utils.mount_samba_share')
        self.mount_mock = mount_patcher.start()

        def mount_mock(a, b, c, share_name):
            mount_point = '/{}'.format(share_name)
            if os.path.isdir(mount_point):
                return mount_point
            raise Exception('Failed to find test share {}'.format(share_name))
        self.mount_mock.side_effect = mount_mock

    def tearDown(self):
        self.mount_mock.stop()
        super(TestMount, self).tearDown()

    def test_mount(self):
        mount_point = Utils.mount_samba_share(None, None, None, 'test_share_1')
        
        files = os.listdir(mount_point)
        self.assertEqual(len(files), 1)
