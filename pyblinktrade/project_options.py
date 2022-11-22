from typing import Any


class ProjectOptions:
    def __init__(self, config: str, section: str):
        self.config: str = config
        self.section: str = section

        def make_getters(tag: str):
            @property
            def _getter(self):
                raw_str = self.config.get(self.section, tag)
                try:
                    return self.config.getint(self.section, tag)
                except Exception:
                    pass
                try:
                    return self.config.getfloat(self.section, tag)
                except Exception:
                    pass
                try:
                    return self.config.getboolean(self.section, tag)
                except Exception:
                    pass

                return raw_str

            return _getter

        for k, v in list(self.items()):
            _getter = make_getters(k)
            setattr(ProjectOptions, k, _getter)

    def has_option(self, attribute: str) -> bool:
        return self.config.has_option(self.section, attribute)

    def get(self, attribute: str) -> str:
        return self.config.get(self.section, attribute)

    def getint(self, attribute: str) -> int:
        return self.config.getint(self.section, attribute)

    def getfloat(self, attribute: str) -> float:
        return self.config.getfloat(self.section, attribute)

    def getboolean(self, attribute: str) -> bool:
        return self.config.getboolean(self.section, attribute)

    def items(self) -> list[tuple[Any, Any]]:
        return self.config.items(self.section)

    def options(self) -> list[str]:
        return self.config.options(self.section)
