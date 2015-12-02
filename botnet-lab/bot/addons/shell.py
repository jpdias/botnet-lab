import subprocess


def shell(cmd):
    try:
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
        return output.replace("\r", " - ").replace("\n", " - ")
    except:
        output = "FAILED"
        return output
