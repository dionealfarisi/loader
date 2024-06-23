from Loader.load import Loader

loader_methods = ["tqdm", "progressbar2", "alive_progress", "rich", "halo", "progress", "click", "yaspin"]

for method in loader_methods:
    print(f"Running loader with method: {method}")
    loader = Loader(method=method, duration=0.05)
    loader.start()
    print()
