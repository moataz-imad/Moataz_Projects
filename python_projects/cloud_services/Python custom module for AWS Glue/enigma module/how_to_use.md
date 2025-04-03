To adjust the functions:

1. **Edit `functions.py`**: Open the `functions.py` file located in the `enigma/enigma` directory. Modify the functions or add new ones as needed.

2. **Navigate to the `enigma` directory**
### The easy way:
- **simply run build_and_upload.ps1**<br>This will build the module and upload it to the correct location
(you will need to allow scripts to run and you need to have aws cli working)
### The old manual way:
- **Generate the wheel file**: run on windows powershell
    ```bash
    python setup.py bdist_wheel
    ```
- **Upload the wheel file to S3**:
    current path is: <br>```s3://s3_bucket/notebooks/inputs/```

-----
```
to load the module in glue use this guide:
- %additional_python_modules uuid6, s3://path/to/enigma_module.whl -> ❌ does not work (converts s3://.. to tmp/s3:/.. )
- %additional_python_modules s3://path/to/enigma_module.whl, uuid6 -> ✅ works fine
- %additional_python_modules s3://path/to/enigma_module.whl -> ✅ works fine
- %additional_python_modules  s3://path/to/enigma_module.whl -> ❌ does not work!!!
```

---
Some functions in the module requires connecting to the current `glueContext` which is why the in the first cell after importing the module, you need to include the already created `glueContext`:<br>
```
def function(glueContext=glueContext): 
    return function_(glueContext) # function_ taken from enigma
    # function = function_ but with a defined glueContext 
```