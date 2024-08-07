import reflex as rx
from ..ui.base import base_page
from . import forms

def blog_post_add_page() -> rx.Component:
    my_forms = forms.blog_post_add_form()
    my_child = rx.vstack(
        rx.heading("New Blog Post", size="9"),
        rx.desktop_only(
            rx.box(
                my_forms,
                width='50vw'
            )
        ),
         rx.tablet_only(
            rx.box(
                my_forms,
                width='75vw'
            )
        ),
        rx.mobile_only(
            rx.box(
                my_forms,
                width='77vw'
            )
        ),
        spacing="5",
        min_height="95vh",
        align="center",
        text_align="center",
    )
    return base_page(my_child)