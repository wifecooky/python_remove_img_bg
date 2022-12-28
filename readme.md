# Use Rembg to remove background from image

https://github.com/danielgatis/rembg

## How
    
    ```bash
    rembg p ./input/ ./output/
    ```

OR 
    
    ```bash
    python3 main.py
    ```

> コマンドは初回実行時にモデルを自動的にダウンロードしてくれるようですが、
> ダウンロード失敗の場合は、
> このURLからモデルをダウンロードし、~/.u2net/u2net.onnxに配置。

```
Downloading data from 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx' to file '/home/vscode/.u2net/u2net.onnx'.
```

# Reference
https://dev.classmethod.jp/articles/python-rembg/



