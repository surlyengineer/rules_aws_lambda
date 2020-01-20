# Bazel AWS Lambda Rules

Borne of a desire to create lambda-compatible python packages, this ruleset is
designed to work with the existing language binary rules, and provide a
mechanism for deploying them to AWS lambda.  It's inspired by a mix of subpar
and rules_pkg, the former being a bit heavy for our use and not really lambda
compatible, while the latter isn't specialized enough.

This is very, very much a work in progress
