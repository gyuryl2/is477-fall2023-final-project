import requests
import hashlib
import os
import zipfile

expected_iris_sha256 = (
    "d11fe30213d36434a0879aab7cb00ce3c812eb7ba2495874438abff7b7b762e9"
)
iris_url = "https://archive.ics.uci.edu/static/public/53/iris.zip"
response = requests.get(iris_url)
if response.status_code == 200:
    
    if not os.path.exists('data/iris'):
        os.makedirs('data/iris', exist_ok=True)

    local_iris = "./data/iris/iris.zip"

    with open(local_iris, mode="wb") as f1:
        f1.write(response.content)
    
    with open(local_iris, mode="rb") as f1:
        data2 = f1.read()
        computed_iris_recon_sha256 = hashlib.sha256(data2).hexdigest()

    if computed_iris_recon_sha256 != expected_iris_sha256:
        print("WARNING: Computed hash does not match expected hash for iris data!")
    else:
        print("Computed hash matches expected hash for iris data!")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

with zipfile.ZipFile('data/iris/iris.zip') as z:
    z.extractall('data/iris')

print("Iris dataset downloaded and extracted into 'data/' directory and SHA-256 hash verification completed")