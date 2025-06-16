# Perform syntax check on all Python files in the project
$pythonFiles = Get-ChildItem -Recurse -Filter *.py
foreach ($file in $pythonFiles) {
    $result = python -m py_compile $file.FullName 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Syntax check failed for $($file.FullName):"
        Write-Host $result
        Read-Host -Prompt "Press Enter to exit"
        exit $LASTEXITCODE
    }
}
Write-Host "Syntax check passed for all files."

# Build the wheel and suppress output
$result = python setup.py bdist_wheel 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Build failed:"
    Write-Host $result
    Read-Host -Prompt "Press Enter to exit"
    exit $LASTEXITCODE
} else {
    Write-Host "Build successful!"
}

# Upload the wheel to S3 and capture any errors
$result = aws s3 cp dist\enigma-1.0-py3-none-any.whl s3://s3_bucket/notebooks/inputs/ 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Upload failed:"
    Write-Host $result
    Read-Host -Prompt "Press Enter to exit"
    exit $LASTEXITCODE
} else {
    Write-Host "Upload successful!"
}

# Get the last modified time of the uploaded file
$result = aws s3api head-object --bucket s3_bucket --key notebooks/inputs/enigma-1.0-py3-none-any.whl 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to retrieve file metadata:"
    Write-Host $result
    Read-Host -Prompt "Press Enter to exit"
    exit $LASTEXITCODE
} else {
    $response = $result | ConvertFrom-Json
    Write-Host "Last modified time of the uploaded file: $($response.LastModified)"
}

# Keep the window open
Read-Host -Prompt "Press Enter to exit"
