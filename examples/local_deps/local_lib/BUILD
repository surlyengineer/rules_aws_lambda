load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "local_lib",
    srcs = [
        "bar.py",
    ],
    visibility = [
        "//examples:__subpackages__",
    ]
)
