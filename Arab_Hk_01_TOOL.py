import requests
import threading
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}Request sent. Status code: {response.status_code}")
        else:
            print(f"{Fore.RED}Request sent. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Request failed: {e}")

def stress_test(url, num_requests, num_threads):
    threads = []
    
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    # Wait for all threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    print(f"{Fore.RED}******************************************")
    print(f"{Fore.RED}*           Stress Test Tool             *")
    print(f"{Fore.RED}******************************************")

    target_url = input(f"{Fore.CYAN}Enter the target URL: ").strip()
    total_requests = int(input(f"{Fore.CYAN}Enter the total number of requests: ").strip())
    max_threads = int(input(f"{Fore.CYAN}Enter the number of threads: ").strip())

    start_time = time.time()
    stress_test(target_url, total_requests, max_threads)
    end_time = time.time()

    print(f"Stress test completed in {Fore.GREEN}{end_time - start_time} seconds")
