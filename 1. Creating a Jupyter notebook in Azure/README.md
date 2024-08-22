# Creating a jupyter notebook in Azure

[Link to Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2)

[Creating a compute instance](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources?view=azureml-api-2)

Notes:

- You need an Azure subscription to set this up. This will cost money. You can use either a credit card, or student credits provided to you. When you setup student credits, a subscription is automatically created for you by the name "Azure for Students"
- Create a workspace in the Machine Learning Studio. 
    - Create a new resource group if you don't have one yet
    - Choose the region closest to yours
    - Make sure to use the "Azure for Students" subscription


- Login into "ml.azure.com"
    - Select your workspace, if not already open
    - On the left, select "Notebooks"

<!-- If you are facing issues with accessing "Notebooks", see steps below:

- Add the role of "AzureML Compute Operator" to your user.
    - Navigate to the resource group created above.
    - In the "Access Control" tab, click on "Add".
    - On the next screen, look for "AzureML Compute Operator". Click View. On the Assignments tab, click on "Add Assignment"
    
    - In the "Members" tab in the "Add role assignment" view, add yourself (look for the email ID associated with your name).
    - Assignment can be permanent as per your wish.
    - Review and Assign. -->

- You can add a notebook, using the following steps:
    - In the "Notebooks" tab, click the "+" sign. Create new file. Select ipynb format, and create the new file
    - You will be able to create a notebook, and edit the notebook, but not run the notebook. In order to run the notebook, you need a kernel, which in turn, requires a compute instance.

- To create a compute instance:
    - Login into [ML Azure](ml.azure.com)
    - Click on the existing workspace.
    - Click on the "New" button. Click on "Compute instance".
    - Select preferred category of compute instance
        - "Standard_DS11_v2" was selected for notebook development.
        - SSH was enabled for the compute instance selected, but not required for notebook development.

- Select the compute instance in your notebook, and the notebook can then be run with the kernel attached to the compute instance.
