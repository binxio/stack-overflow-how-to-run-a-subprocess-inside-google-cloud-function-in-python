import sys
import os
from flask import make_response
import logging as log
import subprocess


def exec(request):
    out = ""
    err = ""

    try:
        process = subprocess.Popen(
            [
                sys.executable,
                "./deploy.py",
                "-n",
                "myProxy",
                "-u",
                "myUserName:myPassword",
                "-o",
                "myOrgName",
                "-e",
                "test",
                "-d",
                "./my-proxy",
                "-p",
                "/",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        out, err = process.communicate()
        log.debug("returncode = %s", process.returncode)
        log.debug("stdout = %s", out)
        log.debug("stderr = %s", err)
        if process.returncode != 0:
            return make_response(f"{out}\n{err} failed", 500)

    except Exception as e:
        return make_response(str(e), 500)

    return make_response(f"{out}\n{err}", 200)
