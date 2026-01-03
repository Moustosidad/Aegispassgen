import sys
from aegispassgen.config import Config
from aegispassgen.core.engine import AegisEngine
from aegispassgen.ui.menu import MainMenu


def main():
    if len(sys.argv) == 1:
        MainMenu().run()
        return

    config = Config.from_args()
    engine = AegisEngine(config)

    if config.ui:
        from aegispassgen.ui.tui import AegisTUI
        AegisTUI(engine).run()
    else:
        for pwd in engine.generate():
            print(pwd)
