from pathlib import Path


def path(apk):
    return Path(__file__).parent.parent.parent.joinpath(apk).absolute().__str__()

print(path('.env.local_emulator'))