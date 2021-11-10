name: Bug Report
description: File a Bug report
title: "[Bug]: "
labels: ["Bug"]

body:
  - type: markdown
    attributes: 
      value: "Please describe the bug you encountered in detail."
  - type: textarea
    attributes:
      label: What happened?
      description: Also tell us, what did you expect to happen?
      placeholder: Tell us what you see!
      value: "A bug happened!"
    validations:
      required: true



