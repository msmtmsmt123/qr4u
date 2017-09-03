from unittest import TestCase
from unittest.mock import call, Mock, patch, MagicMock, PropertyMock

import basic
import settings

class BasicTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # --------------------------------------------------------------------
    def test_must_allow_acceptable_files(self):
        for ext in settings.ALLOWED_EXTENSIONS:
            assert basic.allowed_file("asdf." + ext)

    # --------------------------------------------------------------------
    def test_must_disallow_non_acceptable_files(self):
        assert not basic.allowed_file("asdf.exe")

