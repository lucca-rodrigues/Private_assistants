```bash
python3 -m venv ./venv

source venv/bin/activate

pip install -U pip

arch -arm64 brew install ffmpeg

pip install -r requirements.txt

python script.py --reload
```
