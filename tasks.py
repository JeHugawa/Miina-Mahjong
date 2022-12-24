from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py")

@task
def startui(ctx):
    ctx.run("python3 src/mainui.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def pylint(ctx):
    ctx.run("pylint src")
