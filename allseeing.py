import os
import sys
import time
import itertools
import threading

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from urllib.parse import quote

except ImportError as e:
    print(f"\nFATAL: I require component '{e.name}' but it's not installed.", file=sys.stderr)
    print("Run: pip install -r requirements.txt", file=sys.stderr)
    print("Aborting.", file=sys.stderr)
    
    input("\nPress [Enter] to terminate...")
    sys.exit(1)

API_URL = "https://drastria.gt.tc/api/allseeing.php"
done = False
t = None

def banner():
    print(r" ...  .... .... .....     .%/\    ")
    time.sleep(0.03)
    print(r".  ...  ...  ... ..     .%./  &.    ")
    time.sleep(0.03)
    print(r"..  ....  ..  ...     .%**/     \      ")
    time.sleep(0.03)
    print(r"...  ....  ..       .%***/       &.    ")
    time.sleep(0.03)
    print(r"all seeing eye    .%.***/  .drst_  \      ")
    time.sleep(0.03)
    print(r"... ..... ...   .%*****/ -'      `'.&.    ")
    time.sleep(0.03)
    print(r'..     ..     .%******/  ._."""\'~::,  \   ')
    time.sleep(0.03)
    print(r".......     .%*******/._'` .'^':,  :.,&.    ")
    time.sleep(0.03)
    print(r"...       .%********/',_-^{  ( )  }    :.\  ")
    time.sleep(0.03)
    print(r"  ..    .%*********/%^    '.     .'     ;.&.    ")
    time.sleep(0.03)
    print(r'.     .%**********/;        ".,."        ;#.\    ')
    time.sleep(0.03)
    print(r"     .%***********/  ~'.,,.          ,.-'^    &.    ")
    time.sleep(0.03)
    print(r'   .%************/         ""-.,.-""~           \  ')
    time.sleep(0.03)
    print(r" .%*************/                                &. ")
    time.sleep(0.03)
    print(r"%**************/                                  \\")
    time.sleep(0.03)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate(text='Loading...'):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + text + c + '   ')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(text) + 5) + '\r')
    sys.stdout.flush()

def start_animation(text):
    global done, t
    done = False
    t = threading.Thread(target=animate, args=(text,))
    t.start()

def stop_animation():
    global done, t
    done = True
    try:
        if 't' in globals() and isinstance(t, threading.Thread) and t.is_alive():
            t.join(timeout=1)
    except Exception:
        pass

def open_cctv_window(url, location_name):
    print(f"\nINFO: Opening connection to target : {location_name}...")
    
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-running-insecure-content")
    
    chrome_options.add_argument(f"--app={url}")
    
    chrome_options.add_argument("--window-size=800,600")

    service = ChromeService(ChromeDriverManager().install())
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.execute_script(f"document.title = 'Live Target - {location_name}'")

        print("INFO: System connection established. Viewport active.")

        while True:
            try:
                _ = driver.window_handles
                time.sleep(1)
            except Exception:
                break
                
        print("System terminated.")
        
    except Exception as e:
        print(f"\nConnection bridge failed: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

def get_data_with_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    retries = 3
    for i in range(retries):
        try:
            driver.get(url)
            
            wait = WebDriverWait(driver, 10)
            body_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            page_content = body_element.text
            
            driver.quit()
            return page_content.strip().splitlines()
            
        except StaleElementReferenceException:
            print(f" (WARN : Stale reference. Retry {i + 1}/{retries}...)")
            time.sleep(0.5)
            continue
            
        except Exception as e:
            driver.quit()
            raise e

    driver.quit()
    raise Exception(f"Failed taking data after {retries} tries")

def main():
    while True:
        clear_screen()
        banner()
        print(r"The author take no responsibility for")
        time.sleep(0.03)
        print(r"any damage caused by this tool.")
        time.sleep(0.03)
        print()
        start_animation('Scanning country to peek on..')
        countries = []
        try:
            countries = get_data_with_selenium(f"{API_URL}?list=countries")
            if not countries or "requires Javascript" in countries[0]:
                raise ValueError("Access Denied. Security protocol blocked infiltration")
        except Exception as e:
            print(f"\nTarget acquisition failed : {e}")
            input("\nPress [Enter] to back..")
            break
        finally:
            stop_animation()

        print("Select target country")
        print()
        time.sleep(0.03)
        for i, country in enumerate(countries):
            print(f"{i+1:2d}. {country}")
        print(" 0. Exit")
        print()
        time.sleep(0.03)

        country_choice = input("Selection : ")

        if country_choice.lower() == '0':
            break

        try:
            choice_idx = int(country_choice) - 1
            if 0 <= choice_idx < len(countries):
                selected_country = countries[choice_idx]
                
                while True:
                    clear_screen()
                    banner()
                    print(f"Available target in zone : {selected_country}")
                    print()

                    start_animation(f'Acquiring target from {selected_country}.. ')
                    links = []
                    try:
                        country_encoded = quote(selected_country)
                        links = get_data_with_selenium(f"{API_URL}?negara={country_encoded}")
                        if not links or "Error:" in links[0]:
                            print(f"\nServer : {links[0] if links else 'Target not found'}")
                            input("\nPress [Enter] to back..")
                            break
                    except Exception as e:
                        print(f"Target acquisition failed {e}")
                        input("\nPress [Enter] to back..")
                        break
                    finally:
                        stop_animation()
                                  
                    display_names = []
                    actual_urls = []

                    for line in links:
                        parts = line.split(';')
                        if len(parts) == 2:
                            display_names.append(parts[0])
                            actual_urls.append(parts[1])
                    
                    for i, name in enumerate(display_names):
                        print(f"{i+1:2d}. {name}")
                        
                    print(" 0. Return")
                    print()
                    
                    link_choice = input("Select target to peek at : ")
                            
                    if link_choice.lower() == '0':
                        break
                            
                    link_idx = int(link_choice) - 1
                    
                    if 0 <= link_idx < len(actual_urls):
                        selected_url = actual_urls[link_idx]
                        selected_name = display_names[link_idx]
                        open_cctv_window(selected_url, selected_name)
                                
                    else:
                        print("Unknown directive.")
                        input("Press [Enter] to continue..")
                        
            else:
                print("Unknown command")
                input("Press [Enter] to continue..")
                        
        except ValueError:
            print("Invalid syntax. Numeric input required")
            input("Press [Enter] to continue..")

        print("\nOperation complete")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_animation()
        print("\nProgram terminated") 
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)