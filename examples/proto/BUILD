load("//:defs.bzl", "lambda_python_pkg")

py_binary(
    name = "handler",
    srcs = [
        "handler.py",
    ],
    deps = [
        "//examples/proto/lib:core_python_proto",
    ],
)

lambda_python_pkg(
    name = "handler_func",
    out = "handler_func.zip",
    main = "handler.py",
    src = ":handler",
)
