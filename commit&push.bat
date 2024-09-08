@echo off

set /p if_commit="Do you want to commit the changes? (yes/no): "

if /i "%if_commit%"=="yes" (
    git add .
    git commit -m "commit"
    git push -u origin main
) else (
    echo No commit made.
)

set /p commit_msg="Exit..."