import os

# Function to rename multiple files
def main():

    folder = r"C:\Users\KuChris\Desktop\20210831\test"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"CDL-FFT-20200831-{str(count)}.fft"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        os.rename(src, dst)
# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()