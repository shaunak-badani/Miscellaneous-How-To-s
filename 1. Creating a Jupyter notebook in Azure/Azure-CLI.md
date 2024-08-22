# Azure CLI cheat sheet

| Azure command  | What it do |
| ------------- | ------------- |
| az extension list  | List all extensions installed on the compute instance  |
| az extension add -n ml -y  | Add an extension of the name "ml". "-y" signifies for "yes" to any of the prompts that come up during the addition of the extension. |
| az ml --help  |  List what all you can do with the ML extension on the azure app.  |
| az login | Login into the azure cli. A browser opens and you login. |
| az account list | Gives the list of accounts. |

To install azure ml core via conda, run the following:

```
conda install conda-forge::azure-core
```

Via pip:

```
pip3 install azureml-core
```

There is a way to link azure ML with github codespaces - Not yet figured out.

