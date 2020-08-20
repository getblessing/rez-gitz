
name = "gitz"

description = "Install Rez packages via git clone."

authors = ["davidlatwe"]

version = "1.0.0"

requires = [
    "rez-2.29+",
    "python",
]

tools = [
    "clone",
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    env = globals()["env"]
    env.PATH.prepend("{root}/payload/bin")
    env.PYTHONPATH.prepend("{root}/payload")
