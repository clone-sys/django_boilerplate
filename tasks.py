from invoke import task


@task
def deploy(c):
    c.run("pip freeze > requirements.txt")
    c.run("git add .")
    print("enter your git commit comment: ")
    comment = input()
    c.run(f"git commit -m {comment}")
    c.run("git push -u origin main")
    c.run("git push dokku main")
