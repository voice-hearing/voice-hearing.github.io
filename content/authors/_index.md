---
# To publish author profile pages, remove all the `build` and `cascade` settings below.
build:
  render: never
cascade:
  build:
    render: never
    list: always
cascade:
  # Configure blog posts
  - _target:
      path: /authors/**
    pager: true
    editable: true
    reading_time: true
    commentable: true
    show_date: false
    hide_date: true
    show_related: true
    show_breadcrumb: true
    share: true
    header:
      navbar:
        enable: true
---
