load(
    "@build_stack_rules_proto//python:python_proto_library.bzl",
    "python_proto_library",
)

proto_library(
    name="core_proto",
    srcs=[
        "core_api.proto",
    ],
)

python_proto_library(
    name="core_python_proto",
    deps=[":core_proto"],
    visibility=[
        "//visibility:public"
    ]
)
