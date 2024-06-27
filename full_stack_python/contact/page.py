import reflex as rx

from ..ui.base import base_page
from .. import navigation

from . import form, state

def contact_page() -> rx.Component:
    # Welcome Page (Index)            
    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.cond(state.ContactState.did_submit, 
                state.ContactState.thank_you, ""), 
        rx.desktop_only(
            rx.box(
                form.contact_form(),
                width='50vw'
            )
        ),
         rx.tablet_only(
            rx.box(
                form.contact_form(),
                width='75vw'
            )
        ),
        rx.mobile_only(
            rx.box(
                form.contact_form(),
                width='77vw'
            )
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center",
        text_align="center",
        id="my_child",
    )
    return base_page(my_child)