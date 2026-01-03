import sys
from aegispassgen.config import Config
from aegispassgen.core.engine import AegisEngine


def main():
    # Sin argumentos → menú
    if len(sys.argv) == 1:
        from aegispassgen.ui.menu import MainMenu
        MainMenu().run()
        return

    # Con argumentos → ejecución directa
    config = Config.from_args()
    engine = AegisEngine(config)

    if config.ui:
        from aegispassgen.ui.tui import AegisTUI
        AegisTUI(engine).run()
    else:
        for pwd in engine.generate():
            print(pwd)
