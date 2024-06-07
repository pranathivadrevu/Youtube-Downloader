# YouTube Downloader

This is a simple YouTube downloader application built with Python using the `tkinter` and `customtkinter` libraries for the GUI, and `pytube` for downloading videos from YouTube.

## Requirements

Before running the application, make sure you have the following libraries installed:

- `tkinter`
- `customtkinter`
- `pytube`

You can install these libraries using `pip`:

```bash
pip install pytube3
pip install customtkinter
```

## Usage

1. Clone the repository to your local machine.
2. Install the required libraries using the commands above.
3. Run the `app.py` script.
4. Enter the YouTube video link in the input field.
5. Click the "Download" button to start downloading the video.

## Code Explanation

- The `startDownload` function:
  - Gets the YouTube link from the input field.
  - Uses `pytube` to get the highest resolution stream.
  - Displays the video title and a download status message.
  - Downloads the video to the current directory.
  - Handles errors and displays a download error message if any issues occur.

- `customtkinter` is used to create a modern-looking GUI.
- The main window (`app`) is initialized with a specific size and title.
- UI elements include:
  - A label for instructions.
  - An input field for the YouTube link.
  - A label to show download status.
  - A download button to start the download process.

## Example

Here is an example of what the GUI looks like:

1. The main window prompts the user to insert a YouTube link.
2. After entering the link and clicking the "Download" button, the app fetches and downloads the video.
3. The app displays the video title and download status.

## License

This project is licensed under the MIT License.

---

Feel free to customize the code and the readme file according to your needs.
