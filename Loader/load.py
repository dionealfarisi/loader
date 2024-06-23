import time
from tqdm import tqdm
import progressbar
from alive_progress import alive_bar
from rich.progress import Progress
from halo import Halo
from progress.bar import Bar
import click
from yaspin import yaspin

class Loader:
    def __init__(self, method="tqdm", duration=0.1):
        self.method = method
        self.duration = duration
    
    def start(self):
        if self.method == "tqdm":
            self._tqdm_loader()
        elif self.method == "progressbar2":
            self._progressbar2_loader()
        elif self.method == "alive_progress":
            self._alive_progress_loader()
        elif self.method == "rich":
            self._rich_loader()
        elif self.method == "halo":
            self._halo_loader()
        elif self.method == "progress":
            self._progress_loader()
        elif self.method == "click":
            self._click_loader()
        elif self.method == "yaspin":
            self._yaspin_loader()
        else:
            raise ValueError("Invalid loading method. Choose from: 'tqdm', 'progressbar2', 'alive_progress', 'rich', 'halo', 'progress', 'click', 'yaspin'.")

    def _tqdm_loader(self):
        for _ in tqdm(range(100), desc="Loading", ascii=False, ncols=75):
            time.sleep(self.duration)

    def _progressbar2_loader(self):
        bar = progressbar.ProgressBar(maxval=100, widgets=[
            ' [', progressbar.Percentage(), '] ',
            progressbar.Bar(), ' (', progressbar.ETA(), ') '
        ])
        bar.start()
        for i in range(100):
            time.sleep(self.duration)
            bar.update(i + 1)
        bar.finish()

    def _alive_progress_loader(self):
        with alive_bar(100, title="Loading") as bar:
            for i in range(100):
                time.sleep(self.duration)
                bar()

    def _rich_loader(self):
        with Progress() as progress:
            task = progress.add_task("[red]Loading...", total=100)
            for i in range(100):
                time.sleep(self.duration)
                progress.update(task, advance=1)

    def _halo_loader(self):
        spinner = Halo(text='Loading', spinner='dots')
        spinner.start()
        for _ in range(100):
            time.sleep(self.duration)
        spinner.stop()
    
    def _progress_loader(self):
        bar = Bar('Processing', max=100)
        for i in range(100):
            time.sleep(self.duration)
            bar.next()
        bar.finish()
    
    def _click_loader(self):
        with click.progressbar(length=100, label='Loading') as bar:
            for i in range(100):
                time.sleep(self.duration)
                bar.update(1)
    
    def _yaspin_loader(self):
        with yaspin(text="Loading", color="cyan") as spinner:
            for _ in range(100):
                time.sleep(self.duration)
        spinner.ok("✔")
                 
