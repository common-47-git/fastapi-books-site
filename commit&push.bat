@echo off
set /p if_commit="Do you want to commit the changes? (yes/no): "

if /i "%if_commit%"=="yes" (
    set /p commit_msg="Enter the commit message: "
    if "%commit_msg%"=="" (
        set commit_msg="commit"
    )
    git add .
    git commit -m "%commit_msg%"
    git push -u origin master
) else (
    echo No commit made.
)
set /p commit_msg="Exit..."