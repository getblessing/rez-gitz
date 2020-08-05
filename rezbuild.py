
import os
import sys
import shutil


def copy(src, dst):
    shutil.copytree(
        src,
        dst,
        ignore=shutil.ignore_patterns(
            "*.pyc",
            "__pycache__"
        )
    )


def write_version(root, module_path):
    version = None

    with open(os.path.join(root, "package.py"), "r") as f:
        for line in f:
            if not line.startswith("version ="):
                continue

            locals_ = dict()
            exec(line, {}, locals_)
            version = locals_["version"]
            break

    assert version, "Couldn't figure out version from package.py"

    # Embed version into Python package
    with open(os.path.join(module_path, "__version__.py"), "w") as f:
        f.write("version = \"%s\"" % version)


def build(source_path, build_path, install_path, targets=None):
    targets = targets or []

    build_dir = build_path + "/payload"
    install_dir = install_path + "/payload"

    if os.path.isdir(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)

    gitz_dir = os.path.join(source_path, "src", "gitz")
    bin_dir = os.path.join(source_path, "src", "bin")

    gitz_dir_b = os.path.join(build_dir, "gitz")
    bin_dir_b = os.path.join(build_dir, "bin")

    copy(gitz_dir, gitz_dir_b)
    copy(bin_dir, bin_dir_b)

    write_version(source_path, gitz_dir_b)

    if "install" in targets:
        if os.path.isdir(install_dir):
            shutil.rmtree(install_dir)

        copy(build_dir, install_dir)


if __name__ == "__main__":
    build(source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
          build_path=os.environ["REZ_BUILD_PATH"],
          install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
          targets=sys.argv[1:])
