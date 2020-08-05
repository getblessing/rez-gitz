
name = "gitz"

description = "Install Rez packages via git clone."

authors = ["davidlatwe"]

version = "0.1.0"

requires = [
    "rez-2.29+",
]

tools = [
    "clone",
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    env.PATH.prepend("{root}/payload/bin")
    env.PYTHONPATH.prepend("{root}/payload/gitz")
