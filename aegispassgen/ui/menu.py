from textual.app import App, ComposeResult
from textual.widgets import Static, Footer
from textual.containers import Vertical
from textual.reactive import reactive
from rich.text import Text
import sys


BANNER = r"""
 █████╗ ███████╗ ██████╗ ██╗███████╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝
███████║█████╗  ██║  ███╗██║███████╗
██╔══██║██╔══╝  ██║   ██║██║╚════██║
██║  ██║███████╗╚██████╔╝██║███████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝

 ADVANCED PASSWORD GENERATION FRAMEWORK
 RED TEAM • AUDIT • RESEARCH
"""


OPTIONS = [
    "Start interactive generation",
    "Quick demo (5k)",
    "About",
    "Exit",
]


class MainMenu(App):
    CSS = """
    Screen {
        background: black;
        color: #00ff00;
    }
    """

    index = reactive(0)

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static(Text(BANNER, justify="center", style="bold green"))
            yield Static(self.render_menu(), id="menu")
        yield Footer()

    def render_menu(self):
        text = Text(justify="center")
        for i, opt in enumerate(OPTIONS):
            prefix = "▶ " if i == self.index else "  "
            style = "bold white" if i == self.index else "green"
            text.append(f"\n{prefix}{opt}", style=style)
        return text

    def on_key(self, event):
        if event.key == "up":
            self.index = (self.index - 1) % len(OPTIONS)
            self.refresh()

        elif event.key == "down":
            self.index = (self.index + 1) % len(OPTIONS)
            self.refresh()

        elif event.key == "enter":
            self.select()

    def refresh(self):
        self.query_one("#menu").update(self.render_menu())

    def select(self):
        choice = OPTIONS[self.index]

        if choice.startswith("Start"):
            self.exit()
            self.launch_interactive()

        elif choice.startswith("Quick"):
            self.exit()
            self.launch_demo()

        elif choice == "About":
            self.query_one("#menu").update(
                Text(
                    "\nAEGISPASSGEN\n\nTerminal-based password generation framework\nFocused on human patterns and efficiency\n",
                    justify="center",
                    style="green",
                )
            )

        elif choice == "Exit":
            self.exit()
            sys.exit(0)

    def launch_interactive(self):
        from aegispassgen.config import Config
        from aegispassgen.core.engine import AegisEngine
        from aegispassgen.ui.tui import AegisTUI

        config = Config(
            words=["example", "password"],
            numbers=["2024"],
            max_results=100_000,
            seed=None,
            ui=True,
        )
        engine = AegisEngine(config)
        AegisTUI(engine).run()

    def launch_demo(self):
        from aegispassgen.config import Config
        from aegispassgen.core.engine import AegisEngine
        from aegispassgen.ui.tui import AegisTUI

        config = Config(
            words=["demo", "test"],
            numbers=["123"],
            max_results=5000,
            seed=42,
            ui=True,
        )
        engine = AegisEngine(config)
        AegisTUI(engine).run()
