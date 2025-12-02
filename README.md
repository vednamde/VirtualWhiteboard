# Virtual AI Whiteboard

A touchless virtual whiteboard application that allows you to draw on the screen using hand gestures. Built with Python, OpenCV, and MediaPipe.

## 🎨 Features

- **Hand Tracking**: Real-time hand detection and tracking using MediaPipe.
- **Gesture Control**:
  - **Draw**: Raise your **Index Finger** to draw.
  - **Select/Hover**: Raise **Index + Middle Fingers** to select colors or brush sizes (stops drawing).
  - **Clear Screen**: Raise **All Fingers** to clear the canvas.
- **Tools**:
  - **Brush Sizes**: Choose from Small, Medium, or Large brush sizes.
  - **Colors**: Select from Pink, Blue, Green, or use the Eraser.
- **Save Work**: Press `s` on your keyboard to save your artwork as an image.

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV**: For image processing and webcam feed.
- **MediaPipe**: For robust hand tracking and landmark detection.
- **NumPy**: For array manipulations and canvas handling.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/vednamde/VirtualWhiteboard.git
    cd VirtualWhiteboard
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  Run the application:
    ```bash
    python main.py
    ```

2.  **How to Use**:
    *   **Selection Mode**: Keep your **Index and Middle fingers up**. Move your hand to the top of the screen to select a color or brush size.
    *   **Drawing Mode**: Keep only your **Index finger up**. Move your finger around to draw.
    *   **Clear Canvas**: Open your hand (all fingers up) to wipe the screen.
    *   **Save**: Press `s` to save the current drawing as `whiteboard_art.jpg`.
    *   **Quit**: Press `q` to exit the application.

## 📁 Project Structure

```
VirtualWhiteboard/
├── main.py                # Main application entry point
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── utils/
    └── hand_tracking.py   # Hand detection and tracking module
```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
