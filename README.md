# Funny filters

## ⬇️ Installation
1. Clone this repository:
    ```shell
    git clone https://github.com/Milanaaaa/SA_2024_A4_Pipes-and-filters.git
    ```
2. Ensure that you have pip installed:
    ```shell
    python -m ensurepip --upgrade
    ```
3. Install and use virtualenv (optional):
    ```shell
    pip install virtualenv
    python -m venv venv
    ```
    On Windows, run:
    ```shell
    .\venv\Scripts\activate.bat
    ```
    On Unix or MacOS, run:
    ```shell
    source venv/bin/activate
    ```
4. Install requirements:
    ```shell
    pip install -r requirements.txt
    ```

## 🚀 Usage
```shell
python main.py
```
```
options:
  -h, --help                  show this help message and exit
  -w, --black-and-white       Black and white filter
  -m, --mirror                Mirror filter
  -r RESIZE, --resize RESIZE  Resize filter
  -b BLUR, --blur BLUR        Gaussian blur filter
```
