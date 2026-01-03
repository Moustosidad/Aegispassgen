from aegispassgen.config import Config
from aegispassgen.core.engine import AegisEngine
from aegispassgen.ui.tui import AegisTUI


def main():
    config = Config.from_args()
    engine = AegisEngine(config)

    if config.ui:
        AegisTUI(engine).run()
    else:
        for pwd in engine.generate():
            print(pwd)
