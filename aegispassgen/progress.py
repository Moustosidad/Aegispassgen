def progress(current, total):
    percent = int((current / total) * 100)
    bar = "#" * (percent // 2)
    print(f"\r[{bar:<50}] {percent}%", end="", flush=True)
