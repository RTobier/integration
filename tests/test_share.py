import os
from custom_components.hacs.share import (
    SHARE,
    list_removed_repositories,
    get_hacs,
    SHARE,
)


def test_list_removed_repositories():
    list_removed_repositories()


def test_get_hacs():
    SHARE["hacs"] = None
    os.environ["GITHUB_ACTION"] = "value"
    if "PYTEST" in os.environ:
        del os.environ["PYTEST"]
    get_hacs()
    SHARE["hacs"] = None
    del os.environ["GITHUB_ACTION"]
    os.environ["PYTEST"] = "value"
