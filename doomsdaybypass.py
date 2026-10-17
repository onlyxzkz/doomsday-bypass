import os
import requests
import subprocess

def run_doomsday():
    folder_path = r"C:\Symbols"
    file_path = os.path.join(folder_path, "temp.pdb")
    download_url = "https://doomsdayclient.com/loader/temp.pdb"

    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except Exception as e:
            print(f"Error creating directory: {e}")
            return

    if not os.path.exists(file_path):
        print(f"File temp.pdb not found. Downloading from {download_url}...")
        try:
            response = requests.get(download_url, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print("Download completed successfully.")
            else:
                print(f"Download failed. Status code: {response.status_code}")
                return
        except Exception as e:
            print(f"An error occurred during download: {e}")
            return
    else:
        print("File temp.pdb found locally.")

    print("Launching application... Waiting for process to exit.")
    try:
        process = subprocess.run(["java", "-jar", file_path], shell=True)
        
        print("\n" + "="*100)
        print("Doomsday silent inject done! After self-destruct please use my string cleaner for better bypass")
        print("="*100)
        
    except FileNotFoundError:
        print("Java was not found in the system. Please install JRE/JDK.")
    except Exception as e:
        print(f"Execution error: {e}")

if __name__ == "__main__":
    run_doomsday()
    input("\nPress Enter to exit...")