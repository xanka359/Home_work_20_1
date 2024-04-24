import selene_in_action
from pathlib import Path


def abs_path_from_project(relative_path: str):
    return (
        Path(selene_in_action.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
