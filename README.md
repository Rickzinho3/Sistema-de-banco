# Sistema de banco com Python

### O uso dos arquivos deste projeto é limitado apenas a fins de estudos, qualquer outra ação está estrictamente proibida.

**`Rickzinho (c) 2023`**
<hr/>

## caso não tenha as bibliotecas, instale-as:
```bash
pip install os
```
```bash
pip install time
```


## **Atualizações**
Novidades do código 
- Histórico de transações
- nova função principa `root`
- correção de erros

> Histórico de transações

Esta função irá guardar todos os dados das suas transações, sejam elas: **resgate, depósito ou retirada**; e serão exibidas ao escolher a opção `[ 6 ]` no menu.

> Nova função `root`

A função root será executada juntamente ao script, sendo utilizado o bloco a seguir:
```Python
def root():
    # código da função

if __name__ == "__main__":
    root()
```
> **Nota:** Lembre-se de adicionar o trecho `if __name__ == "__main__":` na última linha do seu código.

## **Informações**
Futuramente será usada uma nova biblioteca no código, na qual será a biblioteca **TQDM**.
> **Nota**: A Biblioteca não vem pré-instalada por padrão no Python, por isso, instale-a usando o código a seguir:

```bash
pip install tqdm
```

após isso, importe a biblioteca
```Python
from tqdm import tqdm
```

