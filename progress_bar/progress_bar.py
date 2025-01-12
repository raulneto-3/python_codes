from tqdm import tqdm
import time

def main():
    total_instances = 100
    progress_bar = tqdm(total=total_instances, desc="Processing", unit="instance")
    for i in range(total_instances):
        time.sleep(0.1)
        progress_bar.update(1)
    progress_bar.close()

if __name__ == '__main__':
    main()