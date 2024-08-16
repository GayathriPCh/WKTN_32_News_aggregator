import subprocess

def run_script(script_name):
  subprocess.run(["python", f"{script_name}"])

if __name__ == "__main__":
  run_script("src/data/ap_scraper.py")
  run_script("src/data/bbc_scraper.py")
  run_script("src/data/categorized_news.py")
