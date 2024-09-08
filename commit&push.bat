@echo off

set /p if_commit="Press ENTER if you want to commit the changes: "

if ""=="" (
    git add .
    git commit -m "commit"
    git push -u origin main
) else (
    echo No commit made.
)

set /p commit_msg=""