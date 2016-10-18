# Stubs for galaxy.tools.deps.container_resolvers.explicit (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ..container_resolvers import ContainerResolver as ContainerResolver

log = ...  # type: Any

class ExplicitContainerResolver(ContainerResolver):
    resolver_type = ...  # type: str
    def resolve(self, enabled_container_types, tool_info): ...
