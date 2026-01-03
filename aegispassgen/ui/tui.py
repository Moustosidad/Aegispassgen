from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, ProgressBar
from textual.containers import Vertical
from threading import Thread
from rich.text import Text


class AegisTUI(App):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.count = 0

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Static(self.banner())
            yield ProgressBar(total=self.engine.config.max_results, id="bar")
            yield Static("Starting...", id="status")
        yield Footer()

    def on_mount(self):
        Thread(target=self.run_engine, daemon=True).start()

    def run_engine(self):
        bar = self.query_one("#bar")
        status = self.query_one("#status")

        for _ in self.engine.generate():
            self.count += 1
            bar.advance(1)

            if self.count % 1000 == 0:
                status.update(f"[green]Generated:[/] {self.count}")

        status.update("[bold red]Completed")

    def banner(self):
        return Text(
            """
 █████╗ ███████╗ ██████╗ ██╗███████╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝
███████║█████╗  ██║  ███╗██║███████╗
██╔══██║██╔══╝  ██║   ██║██║╚════██║
██║  ██║███████╗╚██████╔╝██║███████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝
 ADVANCED PASSWORD GENERATION ENGINE
""",
            justify="center",
            style="bold green",
        )
