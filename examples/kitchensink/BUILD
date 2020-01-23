load("//:defs.bzl", "lambda_python_pkg")
load("@example_py_deps//:requirements.bzl", "requirement")

py_binary(
    name = "handler",
    srcs = [
        "handler.py",
    ],
    deps = [
        "//examples/kitchensink/lib:core_python_proto",
        "//examples/kitchensink/lib:id_gen",
        "@pip3//silly",
        requirement("redis"),
    ],
)

lambda_python_pkg(
    name = "handler_func",
    out = "handler_func.zip",
    main = "handler.py",
    src = ":handler",
)
