<div align="center">
    <h1>Python banking system</h1>
</div>

### Use of this project's files is limited to study purposes only, any other action is strictly prohibited.

<div align="center">
    <h3><a href="https://github.com/Rickzinho3">Rickzinho</a> (c) 2023</h3>
</div>
<hr/>

## If you don't have the libraries, install them:
```bash
pip install os
```
```bash
pip install time
```


## **Updates**
code news 
- transaction history
- new main function `root`
- error correction

> transaction history

This function will save all your transaction data, whether they are: **redemption, deposit or withdrawal**; and will be displayed when choosing the `[ 6 ]` option in the menu.

> new function `root`

The root function will be executed together with the script, using the following block:
```Python
def root():
    # function code

if __name__ == "__main__":
    root()
```
> **Note:** Remember to add the snippet `if __name__ == "__main__":` on the last line of your code.

## **Information**
In the future, a new library will be used in the code, which will be the library **TQDM**.
> **Note**: The Library is not pre-installed by default in Python, so install it using the following code:

```bash
pip install tqdm
```

after that, import the library
```Python
from tqdm import tqdm
```

