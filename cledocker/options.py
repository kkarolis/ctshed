import dataclasses

from typing import List


@dataclasses.dataclass
class Options:
    cmd: str
    image_name: str
    executable_name: str
    source_image: str
    path: str
    packages: List[str] = dataclasses.field(default_factory=list)
