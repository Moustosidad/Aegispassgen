from aegispassgen.core.scheduler import Scheduler


class AegisEngine:
    def __init__(self, config):
        self.config = config
        self.scheduler = Scheduler(
            words=config.words,
            numbers=config.numbers,
            max_results=config.max_results,
            seed=config.seed,
        )

    def generate(self):
        yield from self.scheduler.run()
