### Installation

- For Arch, Fedora and Ubuntu based distros:
```sh
    pip install -r requirements
    chmod +x install.py
    ./install.py
```
#### Troubleshooting

- First run ```flutter doctor```

    ##### Unable to find the android SDK
    - Open android studio and make sure the android sdk is installed
    - run ```flutter config --android-studio-dir <directory>```

### Setup
- Register a [NewsAPI](https://newsapi.org/ "NewsAPI") API key
- Create your flutter project
	```bash
flutter create news_app
cd news-app/
flutter pub add provider 
flutter pub add dio
flutter pub add json_annotation
flutter pub add json_serializable --dev
flutter pub add build_runner --dev
flutter pub get
```
